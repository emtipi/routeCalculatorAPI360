from typing import Optional
from sqlmodel import SQLModel, Field

class City(SQLModel, table=True):
    __tablename__ = "cities"
    name: str = Field(primary_key=True)

class Connection(SQLModel, table=True):
    __tablename__ = "connections"
    id: Optional[int] = Field(default=None, primary_key=True)
    origin: str = Field(foreign_key="cities.name")
    destination: str = Field(foreign_key="cities.name")
    type: str  # Car, Plane, Ship, Train
    plate: Optional[str] = None
    flight_number: Optional[str] = None
    seat: Optional[str] = None
    ship_number: Optional[str] = None
