from sqlalchemy.orm import Session
from app.repository.flights_repository import FlightRepository

class FlightService:
    def __init__(self, db: Session):
        self.flight_repository = FlightRepository(db)

    def create_flight(self, flight_data: dict):
        return self.flight_repository.create_flight(flight_data)

    def get_nearby_flights(self, flight_id: int):
        return self.flight_repository.get_nearby_flights(flight_id)
