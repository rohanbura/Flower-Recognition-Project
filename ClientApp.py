from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS, cross_origin
from decode_utils.utils import decodeImage
from predict import flower

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app = Flask(__name__)
CORS(app)

#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = flower(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictionflower()
    return jsonify(result)


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    app.run(debug = True )