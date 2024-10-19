from dataclasses import dataclass


@dataclass
class PlaceDescription:
    display_name: str
    types: list[str]
