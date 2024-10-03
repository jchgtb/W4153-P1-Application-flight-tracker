from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.flights_service import FlightService
from app.utils.dependencies import get_db
from app.models.flight_model import FlightCreate

router = APIRouter()

@router.post("/flights", tags=["flights"])
def create_flight(flight_data: FlightCreate, db: Session = Depends(get_db)):
    flight_service = FlightService(db)
    created_flight = flight_service.create_flight(flight_data.dict())
    return created_flight

@router.get("/flights/{user_id}", tags=["flights"])
def get_flight_by_user_id(user_id: int, db: Session = Depends(get_db)):
    flight_service = FlightService(db)

    flight = flight_service.get_flight_by_user_id(user_id)

    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    return flight

@router.post("/flights/nearby", tags=["flights"])
def get_nearby_flights(flight_id: int, db: Session = Depends(get_db)):
    flight_service = FlightService(db)

    flights = flight_service.get_nearby_flights(flight_id)

    if not flights:
        raise HTTPException(status_code=404, detail="No nearby flights found")

    return {"nearby_flights": flights}
