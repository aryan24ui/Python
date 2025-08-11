from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)