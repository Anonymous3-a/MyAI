import openai
import json

openai.api_key = "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"
p4ai = input("prompt: ")

response = str(openai.Completion.create(
  model="text-davinci-002",
  prompt=p4ai,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
))

print(aip + response.split("t\": \"")[1].split("\"")[0].replace("\\n", "\n")
