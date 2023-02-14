# Microservice for getting Pokemon locations in the Red, Blue, and Yellow games

## Setting up the microservice server
1. Clone repository and navigate to project directory.
2. Create and activate virtual environment:
```
python3 -m venv venv
. venv/bin/activate
```
3. Install packages: `pip install -r requirements.txt`.
4. Start the microservice with `flask run`. The server will run on port 5000 by default. Change server to a different port with the `-p` option. For example: `flask run -p 3000`.

## Requesting data
Request location data using the URL path `/location/<pokemon>`, using either the [PokeAPI](https://pokeapi.co/) Pokemon ID or the Pokemon name. For example, both `/location/25` and `/location/pikachu` will send a request for Pikachu.

## Receiving data
The microservice will respond with a JSON file containing the location data as a HTTP response. This the response for Pikachu:
```json
[
  {
    "location": "Pallet Town Area",
    "versions": [
      "Yellow"
    ]
  },
  {
    "location": "Viridian Forest Area",
    "versions": [
      "Red",
      "Blue"
    ]
  },
  {
    "location": "Power Plant Area",
    "versions": [
      "Red",
      "Blue"
    ]
  }
]
```

In a Node.js application, getting the JSON data could look something like this:

```javascript
const response = await fetch(`http://127.0.0.1:5000/location/pikachu`);
const json = await response.json();
```
## UML sequence diagram
<img width="636" alt="UML sequence diagram" src="https://user-images.githubusercontent.com/65578899/218656192-93d99df6-33b4-4bd4-b43f-70f4909c5ceb.png">

