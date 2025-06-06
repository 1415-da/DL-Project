# Chicken Disease Detection System

A deep learning-based web application for detecting diseases in chickens using computer vision. This system uses a CNN (Convolutional Neural Network) model to analyze images of chickens and identify potential health issues.

## Features

- **Real-time Disease Detection**: Upload images of chickens to instantly detect potential diseases
- **Comprehensive Disease Information**: Get detailed information about detected diseases including:
  - Symptoms
  - Transmission methods
  - Risk factors
  - Economic impact
  - Incubation period
  - Diagnostic methods
- **Recommended Remedies**: Receive specific treatment recommendations for detected diseases
- **User-friendly Interface**: 
  - Drag and drop image upload
  - Real-time image preview
  - Confidence score visualization
  - Responsive design
  - Modern UI with animations

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

## Technical Stack

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - Font Awesome
  - Animate.css
  - jQuery

- **Backend**:
  - Python
  - Flask
  - TensorFlow/Keras
  - OpenCV
  - NumPy

## Project Structure

```
├── app.py                 # Flask application entry point
├── main.py               # Training pipeline entry point
├── src/
│   └── cnnClassifier/
│       ├── components/   # ML pipeline components
│       ├── config/       # Configuration files
│       ├── constants/    # Constants and disease information
│       ├── entity/       # Data entities
│       ├── pipeline/     # ML pipeline stages
│       └── utils/        # Utility functions
├── artifacts/            # Model artifacts and training data
├── templates/            # HTML templates
└── static/              # Static files (CSS, JS, images)
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd chicken-disease-detection
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8080
```

3. Upload an image of a chicken using either:
   - Drag and drop
   - Click to browse files

4. Click "Analyze Image" to get the detection results

## Model Training

To train the model with new data:

1. Place your training images in the appropriate directory
2. Run the training pipeline:
```bash
python main.py
```

## Disease Information

The system currently supports detection of:
- Coccidiosis
- Normal/Healthy state

Each disease detection includes:
- Detailed description
- Severity level
- Symptoms
- Transmission methods
- Risk factors
- Economic impact
- Incubation period
- Diagnostic methods
- Treatment recommendations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or support, please contact:
[kg15072004@gmail.com]
