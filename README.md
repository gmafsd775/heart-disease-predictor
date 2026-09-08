## 🌐 Live Demo

**Try the live application here:**
👉 [https://heart-disease-predictor-ccfg.onrender.com](https://heart-disease-predictor-ccfg.onrender.com)

No installation required. Just open the link and start using it!

---

## 📂 GitHub Repository

**Source Code:**
👉 [https://github.com/gmafsd775/heart-disease-predictor](https://github.com/gmafsd775/heart-disease-predictor)

# Heart Disease Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-green.svg)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.0-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered web application that predicts the likelihood of heart disease based on patient health parameters. This system uses a Random Forest Classifier trained on real patient data to provide accurate risk assessments.

---

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Input Parameters Explained](#input-parameters-explained)
- [Technical Architecture](#technical-architecture)
- [Installation and Setup](#installation-and-setup)
- [Usage Guide](#usage-guide)
- [API Documentation](#api-documentation)
- [Model Performance](#model-performance)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Connect with Me](#connect-with-me)

---

## Overview

Heart disease is one of the leading causes of death worldwide. Early detection and risk assessment can save lives. This project provides a user-friendly interface where anyone can input their health metrics and get an instant, AI-driven risk assessment.

### Purpose
- For Patients: Quick, accessible risk assessment from home
- For Doctors: Decision support tool for clinical evaluation
- For Researchers: Open-source baseline for cardiovascular studies

### Dataset
The model was trained on 918 patient records with 11 clinical features:
- Source: Heart Failure Prediction Dataset
- Features: Age, Blood Pressure, Cholesterol, ECG results, etc.
- Target: Heart Disease (0 = No, 1 = Yes)

---

## How It Works

The application follows a simple workflow:

1. Patient fills the form with health parameters
2. Data is sent to Flask API (Backend)
3. Random Forest Model analyzes the data
   - Checks patterns in the input
   - Compares with training data
   - Calculates probability
4. Result displayed to user:
   - Risk Level (High/Low)
   - Probability Percentage
   - Clinical Recommendations

### Machine Learning Model
- Algorithm: Random Forest Classifier
- Why Random Forest?
  - Handles both numerical and categorical data well
  - Provides feature importance insights
  - Resistant to overfitting
  - Excellent for medical diagnosis tasks

---

## Features

### For End Users

| Feature | Description |
|---------|-------------|
| Easy-to-Use Form | Simple input fields with clear labels and hints |
| Real-time Validation | Instant feedback if values are out of range |
| Visual Risk Assessment | Animated probability bars for easy understanding |
| Clinical Recommendations | Personalized health advice based on risk level |
| Assessment History | Track your past predictions (saved locally) |
| Live API Status | Shows if the system is connected and ready |

### For Developers

| Feature | Description |
|---------|-------------|
| RESTful API | Well-documented endpoints for integration |
| Model Persistence | Saved model file for quick loading |
| Deployment Ready | Configured for Render, Heroku, etc. |
| CORS Enabled | Can be integrated with any frontend |
| Batch Prediction | Support for multiple predictions at once |

---

## Input Parameters Explained

### For Common Users (Simple Explanation)

#### 1. Age (20-100 years)
Your current age in years. Age is a significant risk factor for heart disease.

*Example: 55 years*

#### 2. Resting Blood Pressure (80-250 mm Hg)
Blood pressure when you are at rest (sitting calmly). Lower numbers are generally better.

- Normal: Below 120/80 mm Hg
- Elevated: 120-129/80 mm Hg
- High (Stage 1): 130-139/80-89 mm Hg

*Example: 130 mm Hg*

#### 3. Cholesterol (100-600 mg/dL)
Total cholesterol level in your blood. High cholesterol can lead to blocked arteries.

- Desirable: Below 200 mg/dL
- Borderline: 200-239 mg/dL
- High: 240 mg/dL and above

*Example: 250 mg/dL*

#### 4. Fasting Blood Sugar (<= 120 mg/dL or > 120 mg/dL)
Blood sugar level after not eating for at least 8 hours.

- <= 120 mg/dL: Normal (Low risk)
- > 120 mg/dL: Elevated (High risk - indicates possible diabetes)

*Example: No (<= 120 mg/dL)*

#### 5. Maximum Heart Rate (60-220 bpm)
Highest heart rate you can achieve during exercise. Calculated roughly as: 220 - Age.

- Higher heart rate: Generally indicates better heart function
- Lower than expected: May indicate heart issues

*Example: 150 bpm*

#### 6. ST Depression (Oldpeak) (-5.0 to 10.0)
A measure from ECG test showing how much the ST segment dips below the baseline.

- Negative or Low: Generally normal
- Higher values: May indicate reduced blood flow to heart

*Example: 2.0*

#### 7. Sex
- Male: Higher baseline risk for heart disease
- Female: Lower baseline risk (but risk increases after menopause)

*Example: Male*

#### 8. Chest Pain Type

| Type | Full Form | Description |
|------|-----------|-------------|
| ATA | Typical Angina | Classic chest pain during physical activity |
| NAP | Non-Anginal Pain | Chest pain not related to heart (muscle pain, etc.) |
| ASY | Asymptomatic | No chest pain at all |
| TA | Atypical Angina | Chest pain that doesn't follow typical patterns |

*Example: ATA (Typical Angina)*

#### 9. Resting ECG

| Type | Description |
|------|-------------|
| Normal | Healthy heart rhythm and electrical activity |
| ST | ST-T wave abnormality - may indicate heart damage |
| LVH | Left Ventricular Hypertrophy - enlarged heart muscle |

*Example: Normal*

#### 10. Exercise Angina
Does chest pain occur during physical activity?

- No: No chest pain during exercise (Good)
- Yes: Chest pain during exercise (Warning sign)

*Example: No*

#### 11. ST Segment Slope
The slope of the ST segment during exercise:

| Type | Description |
|------|-------------|
| Up | Upsloping - Generally normal |
| Flat | Flat - May indicate reduced blood flow |
| Down | Downsloping - Often indicates heart disease |

*Example: Flat*

---

## Technical Architecture

The system is built with a three-layer architecture:

### Frontend Layer
- HTML5, CSS3, Vanilla JavaScript
- Responsive Design
- Local Storage for History

### Backend Layer
- Flask Web Framework
- RESTful API Endpoints
- CORS Enabled
- Request Validation

### Model Layer
- Random Forest Classifier
- Trained on 918 patient records
- 15 features after encoding
- 87.5% Accuracy

### Tech Stack

| Layer | Technologies |
|-------|-------------|
| Frontend | HTML5, CSS3, JavaScript, Font Awesome |
| Backend | Flask 2.3.2, Flask-CORS |
| ML Model | Scikit-learn 1.9.0 (Random Forest) |
| Data Processing | Pandas 2.0.3, NumPy 1.24.3 |
| Model Serialization | Joblib 1.3.1 |
| Deployment | Gunicorn 21.2.0, Render |

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning repository)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/gmafsd775/heart-disease-predictor.git
cd heart-disease-predictor

## Connect with Me

### Ahmed Nawaz
- Machine Learning and Data Science Enthusiast
- Passionate about AI in Healthcare

| Platform | Link |
|----------|------|
| GitHub | [github.com/gmafsd775](https://github.com/gmafsd775) |
| LinkedIn | [linkedin.com/in/ahmed-nawaz-52134733b](https://www.linkedin.com/in/ahmed-nawaz-52134733b) |

Feel free to reach out for questions, collaboration, feedback, or opportunities!