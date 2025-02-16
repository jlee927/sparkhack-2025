from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import os, psycopg2, objecttier, random


class InterviewAI:
    # Initializes OpenAI object, and Database connection
    def __init__(self, category):
        load_dotenv()

        # Open AI intialization
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        self.client = OpenAI(api_key=api_key)

        # Initialize database object
        database, host, username, password, port = map(os.getenv, ["DATABASE", "HOST", "USERNAME", "PASSWORD", "PORT"])
        dbConn = psycopg2.connect(database=database,
                                 host=host,
                                 user=username,
                                 password=password,
                                 port=port,
                                 )
    
        # Class variables
        self.questions = objecttier.all_category_questions(dbConn, category)

        # Private variables 
        self._AI_PROMPT = "ERROR" 

    # Returns a list of the questions from .txt file
    def read_txt(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return [line.strip() for line in file if line.strip()]  # Store non-empty lines
        except Exception as e:
            print(f"An error occurred while reading the text file: {e}")
            return []

    # Used to get users response to the question asked by the AI
    def ask_question(self, userResponse, question):
        # self.pick_random_question()
        self.AI_PROMPT = question

        # Checks for error before runnig ai
        if self.AI_PROMPT != "ERROR":
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system", "content": self.AI_PROMPT
                    },
                    {
                        "role": 'user', "content": userResponse +
                            """
                                Can you give specific advice on where i can improve on my response pretend like this sentence didnt exist while answering the question. 
                                Just respond dont say anything saying like Sure or I can answer that for you. This will be the only response, do not expect any follow up clarification.
                                If the prompt i gave you did not even closely answer the prompt say that.
                            """
                    }
                ],
                model="gpt-3.5-turbo"
            )
            return chat_completion.choices[0].message.content 

        # Error happened if this return occurs
        return "ask_question: ERROR WITH AI_PROMPT"

    # Used to pick a random question and keep track of questions chosen
    # [0, 1, 2, 3, 4, 5, 6]
    def pick_random_question(self):
        random.shuffle(self.questions)

        if len(self.questions) != 0:
            self.AI_PROMPT = self.questions.pop().Question
        else:
            print("pick_random_question: Length of questions is 0")
            self.AI_PROMPT = "ERROR"

    @property
    def AI_PROMPT(self):
        return self._AI_PROMPT
    
    # Insures that AI_PROMPT is given the whole prompt whenever the question is updated
    @AI_PROMPT.setter
    def AI_PROMPT(self, question):
        self._AI_PROMPT = "You are an interviewer asking this question: " + question + ". You should judge the users response based on this and give appropriate feedback like a real interviewer/coach would give"

# main


# aiPrompt = "You are an interviewer asking this question: " + cs.questions[0] + ". You should judge the users response based on this and give appropriate feedback like a real interviewer/coach would give" 
# userResponse = "During my time at the University of Illinois at Chicago, I worked on a team project for a software development course where we built a finance tracking web application using the MERN stack. My role involved implementing the backend API using Express and MongoDB, ensuring secure data retrieval and authentication. We followed an Agile workflow, conducting regular stand-up meetings to discuss progress and roadblocks. One challenge we faced was integrating the frontend with the backend efficiently. To resolve this, I collaborated closely with the frontend developer, debugging API responses and refining request structures. Through clear communication and teamwork, we successfully deployed a fully functional application that allowed users to track expenses, savings, and revenue. This experience reinforced the importance of adaptability, proactive problem-solving, and effective collaboration within a development team."

if __name__ == "__main__":
    cs = InterviewAI("Computer Science")
    print(cs.questions.pop().Question)
    print("Length: ", len(cs.questions))
    cs.AI_PROMPT = cs.questions.pop().Question
    print("AI_PROMPT: ", cs.AI_PROMPT)
