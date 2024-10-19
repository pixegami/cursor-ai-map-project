import time
from map_utils import get_static_map_url, find_places_of_interest
from place_description import PlaceDescription

ADDRESS = "2 Park Street, NSW, 2000"


def main():
    map_url = get_static_map_url(ADDRESS)
    print(f"Static map URL for the address: {map_url}")

    places_of_interest_descriptions = [
        PlaceDescription(
            display_name="Supermarket",
            types=["supermarket"],
        ),
        PlaceDescription(
            display_name="Cafe",
            types=["cafe"],
        ),
        PlaceDescription(
            display_name="Park",
            types=["park"],
        ),
        PlaceDescription(
            display_name="Fitness",
            types=["gym"],
        ),
    ]

    places = find_places_of_interest(ADDRESS, places_of_interest_descriptions)
    print(f"\nNearby places of interest:")
    for place in places:
        print(f"\nType: {place.type_name}")
        print(f"Name: {place.display_name}")
        print(f"Map URL: {place.map_url}")
        print(f"Walking time: {place.walking_time} minutes")
        print(f"Transit time: {place.transit_time} minutes")
        print(f"Driving time: {place.driving_time} minutes")


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    print(f"\nExecution time: {execution_time_ms:.2f} ms")
