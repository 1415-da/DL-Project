import numpy as np
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import os
import base64
from io import BytesIO
import tensorflow as tf
from ..constants.disease_info import DISEASE_INFO
tf.config.run_functions_eagerly(True)



class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        print(f"Initializing PredictionPipeline with filename: {filename}")

    def predict(self):
        try:
            model_path = os.path.join("artifacts", "training", "model.h5")
            print(f"Loading model from: {model_path}")
            
            # Check if model file exists
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found at {model_path}")
            
            # load model
            model = load_model(model_path)
            print("Model loaded successfully")

            # Handle base64 image data
            if isinstance(self.filename, str) and self.filename.startswith('data:image'):
                print("Processing base64 image data")
                # Remove the data URL prefix
                base64_data = self.filename.split(',')[1]
                # Convert base64 to image
                image_data = base64.b64decode(base64_data)
                image_stream = BytesIO(image_data)
                test_image = image.load_img(image_stream, target_size=(224, 224))
            else:
                print(f"Processing file from path: {self.filename}")
                # Handle regular file path
                test_image = image.load_img(self.filename, target_size=(224, 224))

            print("Image loaded and resized successfully")

            # Convert image to array and preprocess
            test_image = image.img_to_array(test_image)
            test_image = test_image / 255.0  # Normalize the image
            test_image = np.expand_dims(test_image, axis=0)
            print("Image preprocessed successfully")

            # Make prediction
            result = model.predict(test_image)
            print("Raw model output:", result)
            
            # Get prediction probability
            probability = float(result[0][0])
            
            # For binary classification with sigmoid output
            # If probability > 0.5, predict Coccidiosis (class 1)
            # If probability <= 0.5, predict Normal (class 0)
            prediction = 'Coccidiosis' if probability > 0.5 else 'Normal'
            confidence = probability if prediction == 'Coccidiosis' else 1 - probability
            
            print(f"Final prediction: {prediction}")
            print(f"Confidence: {confidence}")
            print(f"Raw probability: {probability}")

            # Get disease information
            disease_info = DISEASE_INFO.get(prediction, DISEASE_INFO["Normal"])

            return [{
                "class": prediction,
                "confidence": confidence,
                "probability": float(probability),
                "disease_info": disease_info
            }]

        except Exception as e:
            print("Error in prediction:", str(e))
            import traceback
            print("Full error traceback:")
            print(traceback.format_exc())
            return [{"error": str(e)}]