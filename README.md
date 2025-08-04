# 🌱 Soil Quality Predictor

This project is a **Flask-based web application** that predicts **Soil Quality Index** using a **Ridge Regression** machine learning model. Farmers and agricultural experts can input soil properties such as **pH, Nitrogen, Phosphorus, Potassium**, and other factors to assess soil quality for better crop planning.

## 🚀 Features
- 🧠 Ridge Regression ML model for accurate soil quality prediction
- 🧹 Data preprocessing and scaling
- 🌐 Flask web interface for user-friendly data entry
- 📊 Interactive visualization of predictions
- ☁️ Easily deployable on cloud platforms (Render, Heroku, AWS)

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (Responsive UI)
- **Backend:** Flask (Python)
- **Machine Learning:** Ridge Regression (Scikit-learn)
- **Visualization:** Matplotlib / Chart.js
- **Deployment:** Gunicorn, Render/Heroku

## 📂 Project Structure
```
soil-quality-predictor/
│── app.py                 # Flask backend
│── model.ipynb             # Model training notebook
│── ridge_model.pkl         # Saved Ridge Regression model
│── scaler.pkl              # Data scaler
│── templates/
│     └── index.html        # Frontend HTML
│── static/
│     └── style.css         # Styling
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## ⚡ Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/soil-quality-predictor.git
   cd soil-quality-predictor
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask app**
   ```bash
   python app.py
   ```
4. **Access the app**
   Open your browser → `http://127.0.0.1:5000`

## 🧑‍🌾 Usage
- Enter soil properties (pH, Nitrogen, Potassium, Phosphorus, etc.)
- Click **Predict** to get the soil quality index
- View results and charts for better decision-making

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue to discuss what you’d like to improve.

## 📜 License
This project is licensed under the **MIT License**.
