from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/rickandmorty')
def rick_and_morty():
    response = requests.get('https://rickandmortyapi.com/api/character')
    return jsonify(response.json())

@app.route('/api/openweather')
def openweather():
    city = request.args.get('city', 'Quito')
    api_key = '4ea4f5947c7cf0b7193312dcfcdccb98'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es'
    response = requests.get(url)
    return jsonify(response.json())

# NASA photos API
@app.route("/get_nasa_photos")
def nasaphotosAPI():
    url = "https://api.nasa.gov/EPIC/api/natural?api_key=DEMO_KEY"

    response = requests.get(url)
    json = response.json()

    return jsonify(json)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=666)