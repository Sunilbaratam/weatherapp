from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

API_KEY = '993ca12c6579f859043ffb9b9844afd5'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods = ['POST'])
def get_weather():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = json.loads(response.text)

    return render_template('weather.html', weather = weather_data)

if __name__ == '__main__':
    app.run(debug = True) 