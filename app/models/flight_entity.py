from sqlalchemy import Column, Integer, String, Date, Time, Enum
from app.utils.dependencies import Base

class Flight(Base):
    __tablename__ = "flights"

    flight_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    flight_number = Column(String(10), nullable=False)
    flight_date = Column(Date, nullable=False)
    flight_time = Column(Time, nullable=False)
    departure_location = Column(Enum('EWR', 'LGA', 'JFK'), nullable=False)
