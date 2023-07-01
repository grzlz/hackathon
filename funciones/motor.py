import openai
from api_call import get_gpt_response

# Replace with your own API key
openai.api_key = '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'


def chatbunny():
    print("Hola, soy ChatBunny yeyeye!")
    while True:
        user_input = input(">>")
        if user_input == "Adios":
            break
        else:
            response = get_gpt_response(user_input)
            print(response)
chatbunny()