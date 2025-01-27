# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Airport(Base):
    """description: Stores airport details."""
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)
    code = Column(String, nullable=False)

class Flight(Base):
    """description: Details of flights including departure and arrival airports."""
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False)
    departure_id = Column(Integer, ForeignKey('airport.id'))
    arrival_id = Column(Integer, ForeignKey('airport.id'))
    date = Column(Date)

class Passenger(Base):
    """description: Details of passengers."""
    __tablename__ = 'passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    passport_number = Column(String)

class Booking(Base):
    """description: Stores ticket booking information linking passengers to flights."""
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_id = Column(Integer, ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    date_of_booking = Column(DateTime)
    seat_number = Column(String)

class Aircraft(Base):
    """description: Details of aircraft operated by the airline."""
    __tablename__ = 'aircraft'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    max_capacity = Column(Integer)
    aviation_serial_number = Column(String)

class Airline(Base):
    """description: Airline operator details."""
    __tablename__ = 'airline'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    iata_code = Column(String)

class CrewMember(Base):
    """description: Stores crew member details associated with airlines."""
    __tablename__ = 'crew_member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    airline_id = Column(Integer, ForeignKey('airline.id'))

class MaintenanceRecord(Base):
    """description: Records maintenance details of aircraft."""
    __tablename__ = 'maintenance_record'
    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'), nullable=False)
    last_maintenance_date = Column(DateTime)
    description = Column(String)

class Luggage(Base):
    """description: Details luggage carried by passengers."""
    __tablename__ = 'luggage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    weight = Column(Float)
    dimensions = Column(String)

class CheckIn(Base):
    """description: Check-in details for flights."""
    __tablename__ = 'check_in'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('booking.id'), nullable=False)
    check_in_time = Column(DateTime)
    gate_number = Column(String)

class Route(Base):
    """description: Flight route details for airlines."""
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airline_id = Column(Integer, ForeignKey('airline.id'))
    from_airport_id = Column(Integer, ForeignKey('airport.id'))
    to_airport_id = Column(Integer, ForeignKey('airport.id'))
    duration = Column(Integer)

class BoardingPass(Base):
    """description: Details of boarding passes issued to passengers."""
    __tablename__ = 'boarding_pass'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('booking.id'), nullable=False)
    issued_time = Column(DateTime)
    seat_number = Column(String)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    airport1 = Airport(id=1, name="John F. Kennedy International Airport", location="New York, USA", code="JFK")
    airport2 = Airport(id=2, name="Los Angeles International Airport", location="Los Angeles, USA", code="LAX")
    airport3 = Airport(id=3, name="Narita International Airport", location="Narita, Japan", code="NRT")
    airport4 = Airport(id=4, name="Heathrow Airport", location="London, UK", code="LHR")
    flight1 = Flight(id=1, number="AA101", departure_id=1, arrival_id=2, date=date(2023, 7, 15))
    flight2 = Flight(id=2, number="BA202", departure_id=4, arrival_id=3, date=date(2023, 8, 16))
    flight3 = Flight(id=3, number="JL303", departure_id=3, arrival_id=1, date=date(2023, 9, 17))
    flight4 = Flight(id=4, number="AA404", departure_id=2, arrival_id=4, date=date(2023, 10, 18))
    passenger1 = Passenger(id=1, first_name="John", last_name="Doe", passport_number="A1234567")
    passenger2 = Passenger(id=2, first_name="Jane", last_name="Doe", passport_number="B1234567")
    passenger3 = Passenger(id=3, first_name="Alice", last_name="Smith", passport_number="C1234567")
    passenger4 = Passenger(id=4, first_name="Bob", last_name="Johnson", passport_number="D1234567")
    booking1 = Booking(id=1, flight_id=1, passenger_id=1, date_of_booking=datetime(2023, 7, 1, 15, 45), seat_number="12A")
    booking2 = Booking(id=2, flight_id=2, passenger_id=2, date_of_booking=datetime(2023, 8, 2, 16, 50), seat_number="14B")
    booking3 = Booking(id=3, flight_id=3, passenger_id=3, date_of_booking=datetime(2023, 9, 3, 17, 55), seat_number="16C")
    booking4 = Booking(id=4, flight_id=4, passenger_id=4, date_of_booking=datetime(2023, 10, 4, 18, 60), seat_number="18D")
    aircraft1 = Aircraft(id=1, model="Boeing 737", max_capacity=120, aviation_serial_number="SN737001")
    aircraft2 = Aircraft(id=2, model="Airbus A320", max_capacity=150, aviation_serial_number="SN320002")
    aircraft3 = Aircraft(id=3, model="Boeing 777", max_capacity=300, aviation_serial_number="SN777003")
    aircraft4 = Aircraft(id=4, model="Airbus A380", max_capacity=500, aviation_serial_number="SN380004")
    airline1 = Airline(id=1, name="American Airlines", iata_code="AA")
    airline2 = Airline(id=2, name="British Airways", iata_code="BA")
    airline3 = Airline(id=3, name="Japan Airlines", iata_code="JL")
    airline4 = Airline(id=4, name="Emirates", iata_code="EK")
    crew_member1 = CrewMember(id=1, first_name="James", last_name="Brown", position="Pilot", airline_id=1)
    crew_member2 = CrewMember(id=2, first_name="Emily", last_name="Clark", position="Flight Attendant", airline_id=2)
    crew_member3 = CrewMember(id=3, first_name="Michael", last_name="Scott", position="Co-Pilot", airline_id=3)
    crew_member4 = CrewMember(id=4, first_name="Sarah", last_name="Doe", position="Ground Staff", airline_id=4)
    maintenance_record1 = MaintenanceRecord(id=1, aircraft_id=1, last_maintenance_date=datetime(2023, 5, 20, 14, 0), description="Engine Check")
    maintenance_record2 = MaintenanceRecord(id=2, aircraft_id=2, last_maintenance_date=datetime(2023, 6, 21, 15, 0), description="Landing Gear Check")
    maintenance_record3 = MaintenanceRecord(id=3, aircraft_id=3, last_maintenance_date=datetime(2023, 7, 22, 16, 0), description="Cabin Pressure Test")
    maintenance_record4 = MaintenanceRecord(id=4, aircraft_id=4, last_maintenance_date=datetime(2023, 8, 23, 17, 0), description="Fuel System Check")
    luggage1 = Luggage(id=1, passenger_id=1, weight=23.5, dimensions="55x40x20")
    luggage2 = Luggage(id=2, passenger_id=2, weight=18.0, dimensions="50x35x25")
    luggage3 = Luggage(id=3, passenger_id=3, weight=30.0, dimensions="60x45x30")
    luggage4 = Luggage(id=4, passenger_id=4, weight=15.0, dimensions="40x30x15")
    check_in1 = CheckIn(id=1, booking_id=1, check_in_time=datetime(2023, 7, 15, 10, 30), gate_number="G1")
    check_in2 = CheckIn(id=2, booking_id=2, check_in_time=datetime(2023, 8, 16, 11, 45), gate_number="G2")
    check_in3 = CheckIn(id=3, booking_id=3, check_in_time=datetime(2023, 9, 17, 12, 50), gate_number="G3")
    check_in4 = CheckIn(id=4, booking_id=4, check_in_time=datetime(2023, 10, 18, 13, 55), gate_number="G4")
    route1 = Route(id=1, airline_id=1, from_airport_id=1, to_airport_id=2, duration=360)
    route2 = Route(id=2, airline_id=2, from_airport_id=4, to_airport_id=3, duration=420)
    route3 = Route(id=3, airline_id=3, from_airport_id=3, to_airport_id=1, duration=480)
    route4 = Route(id=4, airline_id=4, from_airport_id=2, to_airport_id=4, duration=540)
    boarding_pass1 = BoardingPass(id=1, booking_id=1, issued_time=datetime(2023, 7, 15, 9, 0), seat_number="12A")
    boarding_pass2 = BoardingPass(id=2, booking_id=2, issued_time=datetime(2023, 8, 16, 10, 15), seat_number="14B")
    boarding_pass3 = BoardingPass(id=3, booking_id=3, issued_time=datetime(2023, 9, 17, 11, 30), seat_number="16C")
    boarding_pass4 = BoardingPass(id=4, booking_id=4, issued_time=datetime(2023, 10, 18, 12, 45), seat_number="18D")
    
    
    
    session.add_all([airport1, airport2, airport3, airport4, flight1, flight2, flight3, flight4, passenger1, passenger2, passenger3, passenger4, booking1, booking2, booking3, booking4, aircraft1, aircraft2, aircraft3, aircraft4, airline1, airline2, airline3, airline4, crew_member1, crew_member2, crew_member3, crew_member4, maintenance_record1, maintenance_record2, maintenance_record3, maintenance_record4, luggage1, luggage2, luggage3, luggage4, check_in1, check_in2, check_in3, check_in4, route1, route2, route3, route4, boarding_pass1, boarding_pass2, boarding_pass3, boarding_pass4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
