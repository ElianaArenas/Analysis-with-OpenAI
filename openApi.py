import openai
from config import api_key
from dbInit import db

openai.api_key  = api_key
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

data_cursor = db.inventario.find()

data_list = list(data_cursor)

prompt = f"""
    Take this data and give me an explanation and analysis from it.
    ```{data_list}```
    """
response = get_completion(prompt)
print(response)
