from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import tensorflow as tf
from tensorflow import keras
import pickle

app = Flask(__name__)
api = Api(app)

load AI model (pretrained)
model = keras.models.load_model('model/model.h5')

file = open('model/model.h5', 'r')
file_data = file.read()

model = pickle.loads(file_data)
print(model.summary)

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

        # these are placeholder values
        # TODO: use model.predict() to get emotion values
        return {"angry": 0.1, "disgusted": 0, "fearful": 0, "happy": 0.4, "sad": 0.2, "surprised": 0.3, "neutral": 0}


api.add_resource(Emotions, '/v1/emotions')

if __name__ == '__main__':
    app.run(port = 80, debug=True)