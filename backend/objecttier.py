#
# objecttier
#
# Builds Question-related objects from data retrieved through 
# the data tier.
#

import datatier

#######################################################
# Question:
#
# CREATE TABLE Question (
#     Question_ID SERIAL PRIMARY KEY,
#     question VARCHAR(255) NOT NULL,
#     difficulty VARCHAR(255) CHECK (difficulty IN ('Easy', 'Medium', 'Hard'))
#     category VARCHAR(255);
# );

class Question():
    def __init__(self, id: int, question: str, difficulty: str, category: str):
        self._Question_ID = id
        self._Question = question
        self._Difficulty = difficulty
        self._Category = category

    @property
    def Question_ID(self):
        return self._Question_ID

    @property
    def Question(self):
        return self._Question

    @property
    def Difficulty(self):
        return self._Difficulty

    @property
    def Category(self):
        return self._Category

# Creates a query towards all questions within the bound of category
def all_category_questions(dbConn, question_category: str):
    try:
        sql = """
            SELECT * FROM Question 
            WHERE Question.category = %s
        """

        rows = datatier.select_n_rows(dbConn, sql, (question_category,))
        if len(rows) == 0:
            return []

        questions = []

        for r in rows:
            questions.append(Question(r[0], r[1], r[2], r[3]))

        return questions 
    except Exception as err:
        print("Error inside all_category_questions: ", err)
        return [] 

def add_category_question(dbConn, question: str, difficulty: str, category: str):
    try:
        sql = """
            INSERT INTO Question (question, difficulty, category) 
            VALUES (%s, %s, %s)
        """
        res = datatier.perform_action(dbConn, sql, (question, difficulty, category)) 

        # Checks if the insert was unsuccessful
        if res == -1: 
            return 0
 
        return 1

    except Exception as err:
        print("Error inside of add_category_question: ", err) 
        return 0
            

