import os
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not found. API key must be set as an environment variable manually.")

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def chatbot(prompt):
    # The API call structure was incorrect. This is the correct usage for chat models.
    try:
    #     response = client.responses.create(
    #     model="gpt-5-nano",
    #     input= prompt,
    #     store=True,
    # )
    # return response.output_text
        response = client.chat.completions.create(
            # "gpt-5-nano" is not a real model. Using a standard model instead.
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if not client.api_key:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please create a .env file with OPENAI_API_KEY='your-key' or set it as an environment variable.")
        return

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()