from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# Load the scaler and model
scaler = None
model = None
try:
    scaler = pickle.load(open("model/standardScalar.pkl", "rb"))
    print("Scaler loaded successfully.")
except FileNotFoundError as e:
    print(f"Error loading scaler file: {e}")
except Exception as e:
    print(f"Unexpected error loading scaler file: {e}")

try:
    model = pickle.load(open('model/ModelForTesting.pkl', "rb"))
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(f"Error loading model file: {e}")
except Exception as e:
    print(f"Unexpected error loading model file: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'message': request.form.get('message')
        }
        name = str(form_data['name'])
        email = str(form_data['email'])
        message = str(form_data['message'])
        data = {
            "Name": name,
            "E-mail": email,
            "message": message
        }
        uri = "mongodb+srv://technorohitpaul:technorohitpaul@cluster0.a3emict.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)
        db = client['ArogyaBHARAT']
        coll_create = db['contact']
        coll_create.insert_one(data)
        return render_template('thankyou.html')
    return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect form data
            form_data = {
                'age': request.form.get('age'),
                'sex': request.form.get('sex'),
                'cp': request.form.get('cp'),
                'trestbps': request.form.get('trestbps'),
                'cholesterol': request.form.get('cholesterol'),
                'fbs': request.form.get('fbs'),
                'restecg': request.form.get('restecg'),
                'thalach': request.form.get('thalach'),
                'exang': request.form.get('exang'),
                'oldpeak': request.form.get('oldpeak'),
                'slope': request.form.get('slope'),
                'ca': request.form.get('ca'),
                'thal': request.form.get('thal')
            }

            # Log received form data
            print("Form data received:")
            for key, value in form_data.items():
                print(f"{key}: {value}")

            # Check for missing values
            for key, value in form_data.items():
                if value is None:
                    raise ValueError(f"Missing value for {key}")

            # Convert form data to appropriate types
            age = int(form_data['age'])
            sex = int(form_data['sex'])
            cp = int(form_data['cp'])
            trestbps = int(form_data['trestbps'])
            cholesterol = int(form_data['cholesterol'])
            fbs = int(form_data['fbs'])
            restecg = int(form_data['restecg'])
            thalach = int(form_data['thalach'])
            exang = int(form_data['exang'])
            oldpeak = float(form_data['oldpeak'])
            slope = int(form_data['slope'])
            ca = int(form_data['ca'])
            thal = int(form_data['thal'])

            # Check if scaler and model are loaded
            if scaler is None or model is None:
                raise ValueError("Model or scaler not loaded properly.")

            # Prepare the input data for the model
            input_data = np.array([[age, sex, cp, trestbps, cholesterol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            input_data_scaled = scaler.transform(input_data)

            # Make a prediction
            result = model.predict(input_data_scaled)

            if result[0] == 1.0:
                result = "You have Heart Disease"
                return render_template('out_page.html', result=result)
            else:
                result = "You don't have Heart Disease"
                return render_template('output.html', result=result)

        except ValueError as ve:
            print(f"ValueError: {ve}")
            return render_template('predict.html', error=f"Input error: {ve}")
        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template('predict.html', error="There was an error processing your input. Please check the values and try again.")
    else:
        return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)