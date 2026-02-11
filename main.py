import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt




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
    generate_content_response =  client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0),
        )
    
    if args.verbose:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {generate_content_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generate_content_response.usage_metadata.candidates_token_count}")
        
        print(f"Model Used: gemini-2.5-flash")
        print(f"total tokens: {generate_content_response.usage_metadata.total_token_count}")

    print(f"Response: {generate_content_response.text}")
    
   



if __name__ == "__main__":
    main()
