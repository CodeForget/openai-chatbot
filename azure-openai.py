import os
from openai import AzureOpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not found. API key must be set as an environment variable manually.")

client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_BASE_URL"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2025-01-01-preview",
    )

def chatbot(prompt):
    # The API call structure was incorrect. This is the correct usage for chat models.
    try:
        response = client.chat.completions.create(
            model=os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo"),
            messages=[
                {"role": "system", "content": "You are a hindi language helpful assistant. reply in hindi only user can ask in any language"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600, #Set a limit on the number of tokens per model response. The supported number of tokens are shared between the prompt (including system message, examples, message history, and user query) and the model's response. One token is roughly 4 characters for typical English text
            temperature=0.7, #Controls randomness. Lowering the temperature means that the model will produce more repetitive and deterministic responses. Increasing the temperature will result in more unexpected or creative responses. Try adjusting temperature or Top P but not both.
            top_p=0.95, #Similar to temperature, this controls randomness but uses a different method. Lowering Top P will narrow the model’s token selection to likelier tokens. Increasing Top P will let the model choose from tokens with both high and low likelihood. Try adjusting temperature or Top P but not both.
            frequency_penalty=0, #Reduce the chance of repeating a token proportionally based on how often it has appeared in the text so far. This decreases the likelihood of repeating the exact same text in a response.
            presence_penalty=0, #Reduce the chance of repeating any token that has appeared in the text at all so far. This increases the likelihood of introducing new topics in a response.
            stop=None, #Make the model end its response at a desired point. The model response will end before the specified sequence, so it won't contain the stop sequence text. For ChatGPT, using <|im_end|> ensures that the model response doesn't generate a follow-up user query. You can include as many as four stop sequences.
            stream=False
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
        if user_input.lower() == 'exit' | 'q':
            break
        response = chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()