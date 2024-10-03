from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class FlightCreate(BaseModel):
    user_id: int
    flight_number: str
    flight_date: date
    flight_time: time
    departure_location: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": 123,
                "flight_number": "UA1234",
                "flight_date": "2024-10-02",
                "flight_time": "15:30:00",
                "departure_location": "JFK"
            }
        }
