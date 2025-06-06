from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.pipeline.predict import PredictionPipeline
import base64
from io import BytesIO
from PIL import Image


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        
        # Handle base64 image data
        if isinstance(image, str) and image.startswith('data:image'):
            # Remove the data URL prefix
            base64_data = image.split(',')[1]
            # Convert base64 to image
            image_data = base64.b64decode(base64_data)
            
            # Save the image
            with open(clApp.filename, 'wb') as f:
                f.write(image_data)
            
            # Make prediction
            result = clApp.classifier.predict()
            return jsonify(result)
        else:
            return jsonify([{"error": "Invalid image data format"}])
            
    except Exception as e:
        print("Error in predictRoute:", str(e))
        import traceback
        print("Full error traceback:")
        print(traceback.format_exc())
        return jsonify([{"error": str(e)}])


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) #local host