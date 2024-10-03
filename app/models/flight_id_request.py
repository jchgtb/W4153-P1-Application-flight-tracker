from pydantic import BaseModel

class FlightIDRequest(BaseModel):
    flight_id: int
