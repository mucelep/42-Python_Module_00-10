from pydantic import BaseModel, ValidationError, model_validator, Field
from enum import Enum
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def misson_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        leader = False
        for c in self.crew:
            if c.rank == Rank.COMMANDER or c.rank == Rank.CAPTAIN:
                leader = True
        if not leader:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            count = sum(
                    1 for member in self.crew
                    if member.years_experience >= 5
                    )
            if count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        if not all(c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    try:
        sarah = CrewMember(
            member_id="CM_01",
            name="Sarah Conor",
            rank=Rank.COMMANDER,
            age=52,
            specialization="Mission Command",
            years_experience=30
            )
        jhon = CrewMember(
                member_id="CM_02",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=47,
                specialization="Navigation",
                years_experience=23
                )
        alice = CrewMember(
                member_id="CM_03",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=42,
                specialization="Engineering",
                years_experience=20
                )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500,
            crew=[sarah, jhon, alice]
        )

        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for c in mission.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialization}")
    except ValidationError as error:
        print(error)

    print("\n=========================================")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_millions=2500,
            crew=[jhon, alice]
        )
        print(invalid_mission)
    except ValidationError as error:
        for e in error.errors():
            print(e['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
