from flask import Flask, render_template, request
from map_utils import get_static_map_url, find_places_of_interest
from place_description import PlaceDescription

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map", methods=["POST"])
def map():
    address = request.form["address"]
    map_url = get_static_map_url(address)

    places_of_interest_descriptions = [
        PlaceDescription(display_name="Supermarket", types=["supermarket"]),
        PlaceDescription(display_name="Cafe", types=["cafe"]),
        PlaceDescription(display_name="Park", types=["park"]),
        PlaceDescription(display_name="Fitness", types=["gym"]),
    ]

    places = find_places_of_interest(address, places_of_interest_descriptions)
    return render_template("map.html", address=address, map_url=map_url, places=places)


if __name__ == "__main__":
    app.run(debug=True)
