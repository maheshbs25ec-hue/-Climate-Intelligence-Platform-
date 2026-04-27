from flask import Flask, jsonify, request
import requests
from model import predict_temperature

app = Flask(__name__)

API_KEY = "YOUR_OPENWEATHER_API_KEY"

@app.route("/")
def home():
    return "Climate Intelligence Backend Running"

@app.route("/climate", methods=["GET"])
def get_climate():
    city = request.args.get("city")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]

    prediction = predict_temperature(temp)

    return jsonify({
        "city": city,
        "current_temp": temp,
        "humidity": humidity,
        "predicted_temp": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
