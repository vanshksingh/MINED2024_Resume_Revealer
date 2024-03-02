# gemini_conversation.py

import google.generativeai as genai


def to_markdown(text):
    return f"> {text}"


def start_gemini_conversation( initial_input):
    print("Initializing Gemini model...")

    api_key = "AIzaSyAvh9AbDKJ6E0DdOUll0f1p4qCSlerGvfs"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    # Send the initial input to the model to discard the first response

    chat.send_message(initial_input)


    print("Model ready! Ask away.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chat.send_message(user_input)
        print("Gemini:", response.text)

'''
if __name__ == "__main__":
    print("Welcome to the Gemini Conversation!")

    # Get API key from the user
    api_key = "AIzaSyAvh9AbDKJ6E0DdOUll0f1p4qCSlerGvfs"

    # Pass the initial input to the function
    initial_input = "My name is vks"

    # Start the conversation with the provided API key and initial input
    start_gemini_conversation( initial_input)
    
    
    '''