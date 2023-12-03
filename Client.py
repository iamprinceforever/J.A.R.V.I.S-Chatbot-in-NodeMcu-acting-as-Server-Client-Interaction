import openai

openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Continuous interaction loop
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break  # Exit the loop if the user enters 'exit'

    prompt = f"User: {user_input}\nChatbot:"
    response = generate_response(prompt)
    print("Chatbot:", response)
