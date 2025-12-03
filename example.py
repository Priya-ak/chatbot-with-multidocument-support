from openai import OpenAI

client = OpenAI(api_key="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")



def chat_loop():
    print("🤖 ChatGPT Interactive Mode Started!")
    print("Type 'exit' or 'quit' to stop.\n")
    
    while True:
        # Safe prompt
        print("🟢 You: ", end="")
        user_query = input()

        if user_query.lower() in ["exit", "quit"]:
            print("👋 ChatGPT: Goodbye!")
            break

        response = client.responses.create(
            model="gpt-5-nano",
            input=user_query
        )

        print("\n🤖 ChatGPT:", response.output_text, "💬\n")

chat_loop()


