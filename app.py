from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("ridge_model.joblib")
scaler = joblib.load("scaler.joblib")

# Define feature names in correct order
feature_names = [
    'lat', 'lon', 'elevation',
    'slope1', 'slope2', 'slope3', 'slope4', 'slope5', 'slope6', 'slope7', 'slope8',
    'aspectN', 'aspectE', 'aspectS', 'aspectW', 'aspectUnknown',
    'WAT_LAND', 'NVG_LAND', 'URB_LAND', 'GRS_LAND', 'FOR_LAND',
    'CULTRF_LAND', 'CULTIR_LAND', 'CULT_LAND'
]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get values from form
            input_values = [float(request.form[feature]) for feature in feature_names]
            input_array = np.array([input_values])
            input_scaled = scaler.transform(input_array)
            prediction = model.predict(input_scaled)[0]
            prediction = round(prediction, 2)
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction, features=feature_names)

if __name__ == '__main__':
    app.run(debug=True)
