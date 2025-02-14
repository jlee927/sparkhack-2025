from dotenv import load_dotenv
from openai import OpenAI
import os

class InterviewAI:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        self.client = OpenAI(api_key=api_key)

    def ask_question(self, question):
        chat_completion = self.client.chat.completions.create(
            messages=[{"role": "user", "content": question}],
            model="gpt-4o-mini"
        )
        return chat_completion.choices[0].message.content

