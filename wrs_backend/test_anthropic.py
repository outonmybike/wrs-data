import anthropic
import creds as creds


API_KEY = creds.anthropic_api_key_2

client = anthropic.Anthropic(
    api_key=API_KEY, 
)


# this lets you call claude
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What are the first 3 words you can think of?"}
    ]
)
print(message.content[0].text)







