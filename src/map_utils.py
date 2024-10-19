import os
import googlemaps
from urllib.parse import urlencode
from point_of_interest import PointOfInterest
from place_description import PlaceDescription
import concurrent.futures


def get_static_map_url(address, zoom=15, size="600x300"):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    api_key = os.environ.get("GOOGLE_CLOUD_API_KEY")

    params = {
        "center": address,
        "zoom": zoom,
        "size": size,
        "key": api_key,
        "markers": f"color:red|{address}",
    }

    return base_url + urlencode(params)


def find_places_of_interest(
    address: str, place_descriptions: list[PlaceDescription], limit=1
):
    api_key = os.environ.get("GOOGLE_CLOUD_API_KEY")
    gmaps = googlemaps.Client(key=api_key)

    # Geocode the address to get its coordinates
    geocode_result = gmaps.geocode(address)
    if not geocode_result:
        raise ValueError("Invalid address")

    location = geocode_result[0]["geometry"]["location"]

    def process_place_description(place_description):
        places_result = gmaps.places_nearby(
            location=location,
            type=place_description.types[0],
            rank_by="distance",
        )

        pois = []
        for place in places_result.get("results", [])[:limit]:
            poi_location = place["geometry"]["location"]

            # Get directions for different travel modes
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                future_to_mode = {
                    executor.submit(
                        get_travel_time, gmaps, address, poi_location, mode
                    ): mode
                    for mode in ["walking", "transit", "driving"]
                }
                travel_times = {
                    future_to_mode[future]: future.result()
                    for future in concurrent.futures.as_completed(future_to_mode)
                }

            maps_url = (
                f"https://www.google.com/maps/place/?q=place_id:{place['place_id']}"
            )

            poi = PointOfInterest(
                type_name=place_description.display_name,
                display_name=place["name"],
                map_url=maps_url,
                walking_time=travel_times["walking"],
                transit_time=travel_times["transit"],
                driving_time=travel_times["driving"],
            )
            pois.append(poi)
        return pois

    with concurrent.futures.ThreadPoolExecutor() as executor:
        places_of_interest = list(
            executor.map(process_place_description, place_descriptions)
        )

    return [poi for sublist in places_of_interest for poi in sublist]


def get_travel_time(gmaps, origin, destination, mode):
    directions_result = gmaps.directions(
        origin, f"{destination['lat']},{destination['lng']}", mode=mode
    )
    return directions_result[0]["legs"][0]["duration"]["value"] // 60
