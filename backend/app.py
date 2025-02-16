import interview_ai 
from flask import Flask, json, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class AI_ROUTE(Resource):
    def get(self):
        # csAI = interview_ai.InterviewAI("Computer Science")
        # userResponse = "During my time at the University of Illinois at Chicago, I worked on a team project for a software development course where we built a finance tracking web application using the MERN stack. My role involved implementing the backend API using Express and MongoDB, ensuring secure data retrieval and authentication. We followed an Agile workflow, conducting regular stand-up meetings to discuss progress and roadblocks. One challenge we faced was integrating the frontend with the backend efficiently. To resolve this, I collaborated closely with the frontend developer, debugging API responses and refining request structures. Through clear communication and teamwork, we successfully deployed a fully functional application that allowed users to track expenses, savings, and revenue. This experience reinforced the importance of adaptability, proactive problem-solving, and effective collaboration within a development team."
        # aiResponse = csAI.ask_question(userResponse)

        aiResponse = "CHAT DOWN BECAUSE I DONT WANT TO WASTE MONEY"

        return jsonify({'ai-test': aiResponse})

    def post(self):
        response = request.get_json()
        question = response['question']
        userResponse = response['userResponse']

        # userResponse = userResponse['userAnswer']

        AI = interview_ai.InterviewAI("")
        aiResponse = AI.ask_question(userResponse, question)
        # aiResponse = "Testing post request"
        return jsonify({'aiResponse': aiResponse})

class METADATA_ROUTE(Resource):
    def get(self):
        return "This is METADATA route" 


    # This route will receive the users meta data about the sample interview and return the questions the frontend should ask the user
    def post(self):
        profession = request.get_json()["profession"] # should include [experience, question_amt, complexity, profession]
        AI  = interview_ai.InterviewAI(profession)

        res = []
        for q in AI.questions:
            res.append(q.Question)


        return {'questions': res} # Want to return questions based on the meta data



api.add_resource(AI_ROUTE, '/ai')
api.add_resource(METADATA_ROUTE, '/metadata')

if __name__ == '__main__':
    #AI  = interview_ai.InterviewAI("Computer Science")
    #print(AI.questions[1].Question)
    app.run(debug=True)
