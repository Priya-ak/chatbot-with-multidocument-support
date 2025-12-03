def chatgpt_response():
    user_query = input("Enter your question for ChatGPT: ")
    response = client.responses.create(
        model="gpt-5-nano",
        input=user_query
)
    print("\nChatGPT Response:")

    print(response.output_text)
chatgpt_response()



from openai import OpenAI

client = OpenAI(api_key="sk-proj-xxxxxxxxxxxxxxxx")

def chat_loop():
    print("ChatGPT Interactive Mode Started!")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        # Ask user for input
        user_query = input("You: ")

        # Exit condition
        if user_query.lower() in ["exit", "quit"]:
            print("ChatGPT: Goodbye! 👋")
            break

        # Send query to GPT
        response = client.responses.create(
            model="gpt-5-nano",
            input=user_query
        )

        # Print model response
        print("\nChatGPT:", response.output_text, "\n")

# Run the chat loop
chat_loop()
