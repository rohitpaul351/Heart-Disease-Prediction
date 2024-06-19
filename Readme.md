# Heart Disease Prediction Project
## Overview
The Heart Disease Prediction Project is a machine learning initiative aimed at predicting the likelihood of heart disease in patients. Utilizing a variety of medical and demographic features, the model provides a probabilistic prediction to aid healthcare professionals in early diagnosis and intervention.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Datasets](#datasets)
3. [Models and Evaluation](#models-and-evaluation)
4. [Results](#results)
5. [Acknowledgements](#acknowledgements)

## Project Structure

```bash
heart-disease-prediction/
│
├── data/
│   ├── Heart.csv                 # Raw data files
│
├── notebooks/                    # Jupyter notebooks for analysis and experimentation
│   ├── Heart.ipynb
│
├── models/                       # Trained models and model summaries
│   ├── ModelForTesting.pkl       # Trained model
│   ├── standardScalar.pkl        # Scaled Dataset
│
├── requirements.txt              # Required dependencies
│
└── README.md                     # Project overview and instructions
```
## Datasets
The dataset used in this project is the Heart Disease UCI dataset. It consists of 14 attributes such as age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise-induced angina, oldpeak, the slope of the peak exercise ST segment, number of major vessels, and thalassemia.

## Models and Evaluation
The project utilizes several machine learning models, including:

1. Logistic Regression
2. Random Forest
3. Support Vector Machines

Each model is evaluated using metrics such as accuracy, precision, recall, F1-score

## Results
The results of the model evaluations are documented in the reports/ directory. Detailed analysis, including confusion matrices

## Acknowledgements
The UCI Machine Learning Repository for providing the Heart Disease dataset.
The contributors and maintainers of open-source libraries such as NumPy, Pandas, Scikit-learn, and Matplotlib.