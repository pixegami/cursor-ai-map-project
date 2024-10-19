from dataclasses import dataclass
from typing import Dict


@dataclass
class PointOfInterest:
    type_name: str
    display_name: str
    map_url: str
    walking_time: int
    transit_time: int
    driving_time: int

    def __post_init__(self):
        # Ensure all travel times are non-negative
        if any(
            time < 0
            for time in [self.walking_time, self.transit_time, self.driving_time]
        ):
            raise ValueError("Travel times must be non-negative")
