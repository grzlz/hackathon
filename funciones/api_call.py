# En este archivo estará todo lo relevante para hacer el API call a GPT3
import openai

openai.api_key = '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'

context = ""
def get_gpt_response(prompt_usuario):
    global context
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt =  f"{context} + {prompt_usuario}",
    max_tokens=60)
    respuesta = response.choices[0].text.strip()
    context = f"{context} + {prompt_usuario}: {respuesta}"
    return respuesta
 