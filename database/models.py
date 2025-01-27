# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 27, 2025 15:25:36
# Database: sqlite:////tmp/tmp.bmHWpc7TbJ-01JJM5V9Y2BD8D738N4WQZKZJY/AirportFlightMgmt/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Aircraft(Base):  # type: ignore
    """
    description: Details of aircraft operated by the airline.
    """
    __tablename__ = 'aircraft'
    _s_collection_name = 'Aircraft'  # type: ignore

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    max_capacity = Column(Integer)
    aviation_serial_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    MaintenanceRecordList : Mapped[List["MaintenanceRecord"]] = relationship(back_populates="aircraft")



class Airline(Base):  # type: ignore
    """
    description: Airline operator details.
    """
    __tablename__ = 'airline'
    _s_collection_name = 'Airline'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    iata_code = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CrewMemberList : Mapped[List["CrewMember"]] = relationship(back_populates="airline")
    RouteList : Mapped[List["Route"]] = relationship(back_populates="airline")



class Airport(Base):  # type: ignore
    """
    description: Stores airport details.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    code = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    FlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.arrival_id]', back_populates="arrival")
    departureFlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.departure_id]', back_populates="departure")
    RouteList : Mapped[List["Route"]] = relationship(foreign_keys='[Route.from_airport_id]', back_populates="from_airport")
    toRouteList : Mapped[List["Route"]] = relationship(foreign_keys='[Route.to_airport_id]', back_populates="to_airport")



class Passenger(Base):  # type: ignore
    """
    description: Details of passengers.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    passport_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    LuggageList : Mapped[List["Luggage"]] = relationship(back_populates="passenger")
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="passenger")



class CrewMember(Base):  # type: ignore
    """
    description: Stores crew member details associated with airlines.
    """
    __tablename__ = 'crew_member'
    _s_collection_name = 'CrewMember'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    airline_id = Column(ForeignKey('airline.id'))

    # parent relationships (access parent)
    airline : Mapped["Airline"] = relationship(back_populates=("CrewMemberList"))

    # child relationships (access children)



class Flight(Base):  # type: ignore
    """
    description: Details of flights including departure and arrival airports.
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore

    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)
    departure_id = Column(ForeignKey('airport.id'))
    arrival_id = Column(ForeignKey('airport.id'))
    date = Column(Date)

    # parent relationships (access parent)
    arrival : Mapped["Airport"] = relationship(foreign_keys='[Flight.arrival_id]', back_populates=("FlightList"))
    departure : Mapped["Airport"] = relationship(foreign_keys='[Flight.departure_id]', back_populates=("departureFlightList"))

    # child relationships (access children)
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="flight")



class Luggage(Base):  # type: ignore
    """
    description: Details luggage carried by passengers.
    """
    __tablename__ = 'luggage'
    _s_collection_name = 'Luggage'  # type: ignore

    id = Column(Integer, primary_key=True)
    passenger_id = Column(ForeignKey('passenger.id'))
    weight = Column(Float)
    dimensions = Column(String)

    # parent relationships (access parent)
    passenger : Mapped["Passenger"] = relationship(back_populates=("LuggageList"))

    # child relationships (access children)



class MaintenanceRecord(Base):  # type: ignore
    """
    description: Records maintenance details of aircraft.
    """
    __tablename__ = 'maintenance_record'
    _s_collection_name = 'MaintenanceRecord'  # type: ignore

    id = Column(Integer, primary_key=True)
    aircraft_id = Column(ForeignKey('aircraft.id'), nullable=False)
    last_maintenance_date = Column(DateTime)
    description = Column(String)

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("MaintenanceRecordList"))

    # child relationships (access children)



class Route(Base):  # type: ignore
    """
    description: Flight route details for airlines.
    """
    __tablename__ = 'route'
    _s_collection_name = 'Route'  # type: ignore

    id = Column(Integer, primary_key=True)
    airline_id = Column(ForeignKey('airline.id'))
    from_airport_id = Column(ForeignKey('airport.id'))
    to_airport_id = Column(ForeignKey('airport.id'))
    duration = Column(Integer)

    # parent relationships (access parent)
    airline : Mapped["Airline"] = relationship(back_populates=("RouteList"))
    from_airport : Mapped["Airport"] = relationship(foreign_keys='[Route.from_airport_id]', back_populates=("RouteList"))
    to_airport : Mapped["Airport"] = relationship(foreign_keys='[Route.to_airport_id]', back_populates=("toRouteList"))

    # child relationships (access children)



class Booking(Base):  # type: ignore
    """
    description: Stores ticket booking information linking passengers to flights.
    """
    __tablename__ = 'booking'
    _s_collection_name = 'Booking'  # type: ignore

    id = Column(Integer, primary_key=True)
    flight_id = Column(ForeignKey('flight.id'), nullable=False)
    passenger_id = Column(ForeignKey('passenger.id'), nullable=False)
    date_of_booking = Column(DateTime)
    seat_number = Column(String)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("BookingList"))
    passenger : Mapped["Passenger"] = relationship(back_populates=("BookingList"))

    # child relationships (access children)
    BoardingPassList : Mapped[List["BoardingPass"]] = relationship(back_populates="booking")
    CheckInList : Mapped[List["CheckIn"]] = relationship(back_populates="booking")



class BoardingPass(Base):  # type: ignore
    """
    description: Details of boarding passes issued to passengers.
    """
    __tablename__ = 'boarding_pass'
    _s_collection_name = 'BoardingPass'  # type: ignore

    id = Column(Integer, primary_key=True)
    booking_id = Column(ForeignKey('booking.id'), nullable=False)
    issued_time = Column(DateTime)
    seat_number = Column(String)

    # parent relationships (access parent)
    booking : Mapped["Booking"] = relationship(back_populates=("BoardingPassList"))

    # child relationships (access children)



class CheckIn(Base):  # type: ignore
    """
    description: Check-in details for flights.
    """
    __tablename__ = 'check_in'
    _s_collection_name = 'CheckIn'  # type: ignore

    id = Column(Integer, primary_key=True)
    booking_id = Column(ForeignKey('booking.id'), nullable=False)
    check_in_time = Column(DateTime)
    gate_number = Column(String)

    # parent relationships (access parent)
    booking : Mapped["Booking"] = relationship(back_populates=("CheckInList"))

    # child relationships (access children)
