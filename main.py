import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function
import time



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    for i in range(20):
        if i > 0:
            time.sleep(2)
        generate_content_response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )

        # 1. Add model's candidates to history so it remembers its own thoughts/calls
        if generate_content_response.candidates:
            for candidate in generate_content_response.candidates:
                messages.append(candidate.content)
        else:
            print("No candidates returned from the model.")
            break

        # Grab the parts from the first candidate to check for work to do
        curr_candidate_parts = generate_content_response.candidates[0].content.parts
        function_responses = []
        
        # 2. Process parts (Function Calls or Text)
        for part in curr_candidate_parts:
            if part.function_call:
                if args.verbose:
                    print(f"- Calling function: {part.function_call.name}")
                
                # Execute the tool
                function_call_result = call_function(part.function_call, verbose=args.verbose)
                
                # Validation checks as requested
                if not function_call_result.parts:
                    raise RuntimeError("Function call result has no parts.")
                
                function_responses.append(function_call_result.parts[0])
            
            elif part.text:
                # If the model gives us text, it's likely the final answer
                print(f"Final response: {part.text}")
                return # Exit successfully

        # 3. If we have tool results, feed them back to the model in the next iteration
        if function_responses:
            messages.append(types.Content(role="user", parts=function_responses))
        else:
            # No function calls and no text part handled above? Safety break.
            break

    # If the loop finishes without returning, we hit the iteration limit
    print(f"Error: Maximum iterations (20) reached without a final response.")
    sys.exit(1)

if __name__ == "__main__":
    main()