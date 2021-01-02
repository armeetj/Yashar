from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# model = tf.load()

class Emotions(Resource):
    def get(self):
        if 'file' not in request.files:
            return {"error": "You have not passed any files!"}

        file = request.files['file']
        print(file.filename)

        if file.filename == '':
            return {"error": "No image selected for uploading!"}

        if (str.__contains__(file.filename, ".png") == False) and (str.__contains__(file.filename, ".jpg") == False):
            return {"error": "Files must be of format png or jpg!"}
        return {"result": [{"happy": 0.1}, {"angry": 0.2}]}


api.add_resource(Emotions, '/v1/emotions')

if __name__ == '__main__':
    app.run(port = 80, debug=True)