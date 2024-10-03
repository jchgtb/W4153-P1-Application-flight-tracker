from sqlalchemy.orm import Session
from app.models.flight_entity import Flight
from datetime import datetime, timedelta

class FlightRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_flight(self, flight_data: dict) -> Flight:
        new_flight = Flight(
            user_id=flight_data["user_id"],
            flight_number=flight_data["flight_number"],
            flight_date=flight_data["flight_date"],
            flight_time=flight_data["flight_time"],
            departure_location=flight_data["departure_location"]
        )
        self.db.add(new_flight)
        self.db.commit()
        self.db.refresh(new_flight)
        return new_flight

    def get_nearby_flights(self, flight_id: int):
        current_flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()

        if not current_flight:
            return None

        current_flight_datetime = datetime.combine(current_flight.flight_date, current_flight.flight_time)
        three_hours_before = current_flight_datetime - timedelta(hours=3)
        three_hours_after = current_flight_datetime + timedelta(hours=3)

        all_flights = self.db.query(Flight).filter(Flight.flight_id != flight_id).all()
        nearby_flights = []
        for flight in all_flights:
            flight_datetime = datetime.combine(flight.flight_date, flight.flight_time)
            if three_hours_before <= flight_datetime <= three_hours_after:
                nearby_flights.append(flight)

        return nearby_flights

    def get_flight_by_user_id(self, user_id: int) -> Flight:
        return self.db.query(Flight).filter(Flight.user_id == user_id).first()