import openai
from api_call import get_gpt_response

# Replace with your own API key
openai.api_key = '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'


def chatbunny():
    print("Hola, soy ChatBunny yeyeye!")
    while True:
        user_input = input(">> ")
        if user_input == "Adios":
            break
        else:
            response = get_gpt_response(user_input)
            print(response)
chatbunny()