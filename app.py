# app.py
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import warnings

# Suppress all warnings (including scikit-learn version mismatch)
warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = 'model.joblib'

if not os.path.exists(model_path):
    print(f"Error: {model_path} not found!")
    print("Please make sure you have saved your trained model as 'model.joblib'")
    exit(1)

try:
    model = joblib.load(model_path)
    print("✅ Model loaded successfully!")
    print(f"📋 Expected features: {model.feature_names_in_.tolist()}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Heart Disease Prediction API is running!',
        'endpoints': {
            '/predict': 'POST - Send patient data to get prediction',
            '/features': 'GET - Get list of required features'
        }
    })

@app.route('/features', methods=['GET'])
def get_features():
    """Return the list of features expected by the model"""
    return jsonify({
        'features': model.feature_names_in_.tolist()
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        input_df = pd.DataFrame([data])
        required_features = model.feature_names_in_
        missing_features = set(required_features) - set(input_df.columns)
        
        if missing_features:
            return jsonify({
                'error': f'Missing features: {list(missing_features)}',
                'required_features': required_features.tolist()
            }), 400
        
        input_df = input_df[required_features]
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        return jsonify({
            'prediction': int(prediction[0]),
            'probability_no_disease': float(probability[0][0]),
            'probability_disease': float(probability[0][1]),
            'message': 'No Heart Disease' if prediction[0] == 0 else 'Heart Disease Detected'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("🚀 Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)