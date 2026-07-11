# Titanic Survival Prediction - Flask ML API

A Machine Learning project that predicts whether a passenger survived the Titanic disaster using a trained classification model deployed through a Flask web application.

## Project Overview

This project uses the Titanic dataset to build a machine learning model that predicts passenger survival based on passenger information such as age, gender, passenger class, fare, and family details.

The trained model is integrated with a Flask web application, allowing users to enter passenger details and receive survival predictions.

## Features

- Machine Learning survival prediction
- Flask web application
- User-friendly prediction interface
- Pre-trained model integration

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML/CSS

## Project Structure

Titanic-ML-Flask/

- app.py
- titanic_model.pkl
- requirements.txt
- README.md
- templates/index.html

## Installation

Install required libraries:

pip install -r requirements.txt

## Running the Application

Run the Flask application:

python app.py

Open in browser:

http://127.0.0.1:5000

## Machine Learning Model

The model is trained on the Titanic dataset and predicts survival outcomes for new passenger data.

## Model Performance

Validation Accuracy (Random Forest): 84.36%

Kaggle Competition:
Titanic - Machine Learning from Disaster

Public Leaderboard Score:
0.76794

Number of Submissions:
3

## Repository Contents

- EDA and Feature Engineering
- Model Comparison (Logistic Regression, Decision Tree, Random Forest)
- Hyperparameter Tuning using GridSearchCV
- Trained Model (.pkl)
- Flask Web Application
- REST API (/api/predict)

## Future Improvements

- Deploy the application online
- Add model accuracy metrics
- Improve user interface

## Author

Muhammad Hussain
