from openai import OpenAI

# Hardcoded OpenAI API Key (for development only)
OPENAI_API_KEY = ""  # TODO: Replace with your actual key
client = OpenAI(api_key=OPENAI_API_KEY)

# Stores ongoing chat conversation history
chat_history = [{"role": "user", "content": "Please act like Eddie from Lab Rats."}]

def chat_with_gpt(user_text: str) -> str:
    chat_history.append({"role": "user", "content": user_text})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=0.7
    )
    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})
    return reply
