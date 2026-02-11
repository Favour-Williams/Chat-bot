import os
from dotenv import load_dotenv
from google import genai
import argparse





def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    generate_content_response =  client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=args.user_prompt
        )
    print(f"User Prompt: {args.user_prompt}")
    print(f"Model Used: gemini-2.5-flash")

    print(f"Prompt tokens: {generate_content_response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {generate_content_response.usage_metadata.candidates_token_count}")
    print(f"total tokens: {generate_content_response.usage_metadata.total_token_count}")

    print(f"Response: {generate_content_response.text}")
    
   



if __name__ == "__main__":
    main()
