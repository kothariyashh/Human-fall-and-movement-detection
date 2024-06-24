## Project Structure

|-- README.md

|-- app.py

|-- train.py

|-- predict.py

|-- model/

|   |-- insurance_claim_prediction_model.joblib

|-- dataset/

|   |-- insurance2.csv

|-- requirements.txt


# Insurance Claim Prediction App

This project implements a Streamlit web application for predicting whether an individual is likely to make an insurance 
claim based on various input parameters. The prediction model is trained using a decision tree classifier.

## Project Structure

- **`app.py`**: Streamlit web application code for user interface.
- **`train_model.py`**: Python script for training the machine learning model and saving it.
- **`predict_model.py`**: Python script for loading the trained model and making predictions.
- **`model/insurance_claim_prediction_model.joblib`**: Saved trained model using joblib.
- **`dataset/insurance2.csv`**: Dataset used for training and testing the model.
- **`requirements.txt`**: List of Python dependencies required to run the application.

## Getting Started

### Prerequisites

Ensure you have Python installed. You can install it from [python.org](https://www.python.org).

### Installation
```bash
pip install -r requirements.txt
```
### Running the App
To run the Streamlit app, execute the following command:
```bash
streamlit run app.py
```
This will start a local server and open your default web browser to the app.

### Usage
User Input Parameters: Adjust the sliders and dropdowns in the sidebar to input different values for age, sex, BMI, 
children, smoker status, region, and medical charges.
Predict Button: Click on the "Predict" button in the sidebar to see whether the individual is likely to make an insurance 
claim.
Analysis Dashboard: View average medical charges for claims made and not made based on demo data.

### Examples
#### Example 1: Predicting Insurance Claim Likelihood

Suppose a 40-year-old male with a BMI of 25.3, 2 children, non-smoker from the southeast region, and medical charges of $2900.0 wants to predict the likelihood of making an insurance claim. After inputting these details and clicking "Predict," the app predicts whether this individual is likely to make an insurance claim.

### Dependencies

Python 3.x

pandas

joblib

scikit-learn

streamlit
