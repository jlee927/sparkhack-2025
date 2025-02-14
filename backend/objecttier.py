#
# objecttier
#
# Builds Question-related objects from data retrieved through 
# the data tier.
#


#######################################################
# Question:
#
# CREATE TABLE Question (
#     ID SERIAL PRIMARY KEY,
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
        return self.Question_ID

    @property
    def Question(self):
        return self._Question

    @property
    def Difficulty(self):
        return self._Difficulty

    @property
    def Category(self):
        return self._Category

