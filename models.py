from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trips'
    
    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    date = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, nullable=False)
    customer_name = Column(String, nullable=False)
