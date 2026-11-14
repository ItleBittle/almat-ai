from load_key import load_key
from groq import Groq

API_KEY = load_key()

prompt = input("prompt: ")

print(API_KEY)

client = Groq(api_key=API_KEY)
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
