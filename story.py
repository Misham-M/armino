from openai import OpenAI
from openai import OpenAI
client = OpenAI(api_key ="sk-proj-CsfVqtRUvuKajjaoyOPXT3BlbkFJmkUp1xtiaMgqpFVtfB4a")
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop."
)
print(response)