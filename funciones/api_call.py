# En este archivo estará todo lo relevante para hacer el API call a GPT3
import openai

openai.api_key = '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'

def get_gpt_response(prompt_usuario):
    context = ""
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt =  f"{context} + {prompt_usuario}",
    max_tokens=60)
    respuesta = response.choices[0].text.strip()
    context = f"{context} + {prompt_usuario}: {respuesta}"
    print(context)
    return respuesta
 