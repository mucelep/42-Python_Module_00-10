from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional, Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, min_length=0, max_length=200)


def main() -> None:
    station_info: dict[str, Any] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": "6",
        "power_level": "85.5",
        "oxygen_level": "92.3",
        "last_maintenance": "2026-01-01",
        "is_operational": "True",
        "notes": ""
    }

    space_station = SpaceStation(**station_info)
    status = (
        "Operational" if space_station.is_operational
        else "Non Operational")

    print("Space Station Data Validation\n"
          "========================================")
    print(
        f"""Valid station created:
    ID: {space_station.station_id}
    Name: {space_station.name}
    Crew: {space_station.crew_size} people
    Power: {space_station.power_level}%
    Oxygen: {space_station.oxygen_level}%
    Status: {status}
    """
    )
    print("========================================")

    station_info["crew_size"] = "25"
    try:
        space_station2 = SpaceStation.model_validate(station_info)
        print(space_station2)
    except ValidationError as error:
        for e in error.errors():
            print(e['msg'])


if __name__ == "__main__":
    main()
