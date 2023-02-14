from flask import *
import requests


app = Flask(__name__)


@app.route('/location/<pokemon>')
def send_locations(pokemon):
    """Send location JSON for a `pokemon` ID or name."""
    pokeapi_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/encounters'
    pokemon_json = requests.get(pokeapi_url).json()
    locations = parse_locations(pokemon_json)
    return locations


def parse_locations(pokemon_json):
    """Get pokemon locations from Red, Yellow, and Blue versions."""
    locations = []
    for encounter in pokemon_json:
        location_name = encounter['location_area']['name']
        location_dict = {}
        version_details = encounter['version_details']
        versions = []
        for version_detail in version_details:
            version = version_detail['version']['name']
            if version in ['red', 'blue', 'yellow']:
                versions.append(version.title())
        if versions:
            location_name = location_name.title().replace('-', ' ')
            location_dict['location'] = location_name
            location_dict['versions'] = versions
            locations.append(location_dict)
    return locations
