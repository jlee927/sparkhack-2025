from dotenv import load_dotenv
from openai import OpenAI
import os, psycopg2, objecttier


class InterviewAI:
    # Initializes OpenAI object, and Database connection
    def __init__(self, filepath):
        load_dotenv()

        # Open AI intialization
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        self.client = OpenAI(api_key=api_key)

        self.questions = self.read_txt(filepath) # stores 

        # Initialize database object
        database, host, username, password, port = map(os.getenv, ["DATABASE", "HOST", "USERNAME", "PASSWORD", "PORT"])
        conn = psycopg2.connect(database=database,
                                 host=host,
                                 user=username,
                                 password=password,
                                 port=port,
                                 )




    


    # Returns a list of the questions from .txt file
    def read_txt(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return [line.strip() for line in file if line.strip()]  # Store non-empty lines
        except Exception as e:
            print(f"An error occurred while reading the text file: {e}")
            return []

    def ask_question(self, aiPrompt, userResponse):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system", "content": aiPrompt 
                },
                {
                    "role": 'user', "content": userResponse + 'Can you give specific advice on where i can improve on my response pretend like this sentence didnt exist while answering the question'
                }
            ],
            model="gpt-3.5-turbo"
        )
        return chat_completion.choices[0].message.content

    def pick_random_question(self):
        pass

# main

cs = InterviewAI("./questions/csquestions.txt")

aiPrompt = "You are an interviewer asking this question: " + cs.questions[0] + ". You should judge the users response based on this and give appropriate feedback like a real interviewer/coach would give" 
userResponse = "During my time at the University of Illinois at Chicago, I worked on a team project for a software development course where we built a finance tracking web application using the MERN stack. My role involved implementing the backend API using Express and MongoDB, ensuring secure data retrieval and authentication. We followed an Agile workflow, conducting regular stand-up meetings to discuss progress and roadblocks. One challenge we faced was integrating the frontend with the backend efficiently. To resolve this, I collaborated closely with the frontend developer, debugging API responses and refining request structures. Through clear communication and teamwork, we successfully deployed a fully functional application that allowed users to track expenses, savings, and revenue. This experience reinforced the importance of adaptability, proactive problem-solving, and effective collaboration within a development team."

print(cs.questions[0])

# print(cs.ask_question(aiPrompt, userResponse))
