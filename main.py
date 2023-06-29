# from funciones.saludo import saludo

# saludo()

import openai

# Replace with your own API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def begin_conversation():
    # response = openai.Completion.create(
    #   engine="text-davinci-003",
    #   prompt="Hello, how can I help you today?",
    #   temperature=0.5,
    #   max_tokens=100
    # )
    return "Yeyeye bienvenido"

def continue_conversation(user_input):
    response = get_gpt_response(user_input)
    return response

def get_gpt_response(prompt):
    # response = openai.Completion.create(
    #   engine="text-davinci-003",
    #   prompt=prompt,
    #   temperature=0.5,
    #   max_tokens=100
    # )
    return "Respuesta de GPT"

def main():
    print(begin_conversation())
    while True:
        user_input = input(">> ")
        if user_input == "Adios":
            break
        else:
            print(continue_conversation(user_input))

if __name__ == "__main__":
    main()
