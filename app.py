from flask import *
import requests
import sys
import json

app = Flask(__name__)

@app.route('/location/<pokemon>')
def send_location(pokemon):
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/encounters'
    pokemon_json = requests.get(pokeapi_url).json()
    return pokemon_json
