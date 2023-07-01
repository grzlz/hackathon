# En este archivo estará todo lo relevante para hacer el API call a GPT3
import openai

openai.api_key = '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'

def get_gpt_response(prompt):
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt = prompt ,
    max_tokens=60)
    return(response.choices[0].text.strip())
 