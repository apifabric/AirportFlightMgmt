import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not -7217976690316935145 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport1 = Airport(id=1, name="John F. Kennedy International Airport", location="New York, USA", code="JFK")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7217976690316935145)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2117072748965758670 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport2 = Airport(id=2, name="Los Angeles International Airport", location="Los Angeles, USA", code="LAX")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2117072748965758670)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8356640977648213772 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport3 = Airport(id=3, name="Narita International Airport", location="Narita, Japan", code="NRT")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8356640977648213772)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -715406884173494538 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport4 = Airport(id=4, name="Heathrow Airport", location="London, UK", code="LHR")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-715406884173494538)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6301182114231411979 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight1 = Flight(id=1, number="AA101", departure_id=1, arrival_id=2, date=date(2023, 7, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6301182114231411979)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8496186048620286398 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight2 = Flight(id=2, number="BA202", departure_id=4, arrival_id=3, date=date(2023, 8, 16))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8496186048620286398)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5637703182099551854 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight3 = Flight(id=3, number="JL303", departure_id=3, arrival_id=1, date=date(2023, 9, 17))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5637703182099551854)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -9058313002640496406 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight4 = Flight(id=4, number="AA404", departure_id=2, arrival_id=4, date=date(2023, 10, 18))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-9058313002640496406)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1011159848900756716 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger1 = Passenger(id=1, first_name="John", last_name="Doe", passport_number="A1234567")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1011159848900756716)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6337223710708774556 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger2 = Passenger(id=2, first_name="Jane", last_name="Doe", passport_number="B1234567")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6337223710708774556)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5550737481140013316 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger3 = Passenger(id=3, first_name="Alice", last_name="Smith", passport_number="C1234567")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5550737481140013316)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5376132127356619000 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger4 = Passenger(id=4, first_name="Bob", last_name="Johnson", passport_number="D1234567")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5376132127356619000)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8084069033787428894 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking1 = Booking(id=1, flight_id=1, passenger_id=1, date_of_booking=datetime(2023, 7, 1, 15, 45), seat_number="12A")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8084069033787428894)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2253217061182539911 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking2 = Booking(id=2, flight_id=2, passenger_id=2, date_of_booking=datetime(2023, 8, 2, 16, 50), seat_number="14B")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2253217061182539911)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4765956860814935553 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking3 = Booking(id=3, flight_id=3, passenger_id=3, date_of_booking=datetime(2023, 9, 3, 17, 55), seat_number="16C")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4765956860814935553)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4810650508909555195 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking4 = Booking(id=4, flight_id=4, passenger_id=4, date_of_booking=datetime(2023, 10, 4, 18, 60), seat_number="18D")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4810650508909555195)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1240463335391969744 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft1 = Aircraft(id=1, model="Boeing 737", max_capacity=120, aviation_serial_number="SN737001")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1240463335391969744)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3110406235239982409 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft2 = Aircraft(id=2, model="Airbus A320", max_capacity=150, aviation_serial_number="SN320002")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3110406235239982409)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8713826618757737094 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft3 = Aircraft(id=3, model="Boeing 777", max_capacity=300, aviation_serial_number="SN777003")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8713826618757737094)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6589808930111612595 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft4 = Aircraft(id=4, model="Airbus A380", max_capacity=500, aviation_serial_number="SN380004")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6589808930111612595)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -9090539206737486077 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline1 = Airline(id=1, name="American Airlines", iata_code="AA")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-9090539206737486077)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8825828871253644048 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline2 = Airline(id=2, name="British Airways", iata_code="BA")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8825828871253644048)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1623633513989354649 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline3 = Airline(id=3, name="Japan Airlines", iata_code="JL")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1623633513989354649)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8300836831228208941 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline4 = Airline(id=4, name="Emirates", iata_code="EK")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8300836831228208941)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -110642013258518086 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member1 = CrewMember(id=1, first_name="James", last_name="Brown", position="Pilot", airline_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-110642013258518086)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8185807296956486526 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member2 = CrewMember(id=2, first_name="Emily", last_name="Clark", position="Flight Attendant", airline_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8185807296956486526)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8477794558632927392 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member3 = CrewMember(id=3, first_name="Michael", last_name="Scott", position="Co-Pilot", airline_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8477794558632927392)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7744297562627492151 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member4 = CrewMember(id=4, first_name="Sarah", last_name="Doe", position="Ground Staff", airline_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7744297562627492151)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5348004549349113375 in succeeded_hashes:  # avoid duplicate inserts
            instance = maintenance_record1 = MaintenanceRecord(id=1, aircraft_id=1, last_maintenance_date=datetime(2023, 5, 20, 14, 0), description="Engine Check")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5348004549349113375)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -205383855385394045 in succeeded_hashes:  # avoid duplicate inserts
            instance = maintenance_record2 = MaintenanceRecord(id=2, aircraft_id=2, last_maintenance_date=datetime(2023, 6, 21, 15, 0), description="Landing Gear Check")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-205383855385394045)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8886884345391687353 in succeeded_hashes:  # avoid duplicate inserts
            instance = maintenance_record3 = MaintenanceRecord(id=3, aircraft_id=3, last_maintenance_date=datetime(2023, 7, 22, 16, 0), description="Cabin Pressure Test")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8886884345391687353)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -136554672847102444 in succeeded_hashes:  # avoid duplicate inserts
            instance = maintenance_record4 = MaintenanceRecord(id=4, aircraft_id=4, last_maintenance_date=datetime(2023, 8, 23, 17, 0), description="Fuel System Check")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-136554672847102444)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3006329958377641393 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage1 = Luggage(id=1, passenger_id=1, weight=23.5, dimensions="55x40x20")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3006329958377641393)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4061801594460490446 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage2 = Luggage(id=2, passenger_id=2, weight=18.0, dimensions="50x35x25")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4061801594460490446)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5689379238942540562 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage3 = Luggage(id=3, passenger_id=3, weight=30.0, dimensions="60x45x30")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5689379238942540562)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6527229265850857403 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage4 = Luggage(id=4, passenger_id=4, weight=15.0, dimensions="40x30x15")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6527229265850857403)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3087682981253345934 in succeeded_hashes:  # avoid duplicate inserts
            instance = check_in1 = CheckIn(id=1, booking_id=1, check_in_time=datetime(2023, 7, 15, 10, 30), gate_number="G1")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3087682981253345934)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8278029392254949779 in succeeded_hashes:  # avoid duplicate inserts
            instance = check_in2 = CheckIn(id=2, booking_id=2, check_in_time=datetime(2023, 8, 16, 11, 45), gate_number="G2")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8278029392254949779)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1309691430929733258 in succeeded_hashes:  # avoid duplicate inserts
            instance = check_in3 = CheckIn(id=3, booking_id=3, check_in_time=datetime(2023, 9, 17, 12, 50), gate_number="G3")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1309691430929733258)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8700429097740674857 in succeeded_hashes:  # avoid duplicate inserts
            instance = check_in4 = CheckIn(id=4, booking_id=4, check_in_time=datetime(2023, 10, 18, 13, 55), gate_number="G4")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8700429097740674857)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4600527282998451196 in succeeded_hashes:  # avoid duplicate inserts
            instance = route1 = Route(id=1, airline_id=1, from_airport_id=1, to_airport_id=2, duration=360)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4600527282998451196)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1987873252206502386 in succeeded_hashes:  # avoid duplicate inserts
            instance = route2 = Route(id=2, airline_id=2, from_airport_id=4, to_airport_id=3, duration=420)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1987873252206502386)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -545025603599888701 in succeeded_hashes:  # avoid duplicate inserts
            instance = route3 = Route(id=3, airline_id=3, from_airport_id=3, to_airport_id=1, duration=480)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-545025603599888701)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6042642153374609228 in succeeded_hashes:  # avoid duplicate inserts
            instance = route4 = Route(id=4, airline_id=4, from_airport_id=2, to_airport_id=4, duration=540)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6042642153374609228)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8626074287164918795 in succeeded_hashes:  # avoid duplicate inserts
            instance = boarding_pass1 = BoardingPass(id=1, booking_id=1, issued_time=datetime(2023, 7, 15, 9, 0), seat_number="12A")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8626074287164918795)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4887059881417921327 in succeeded_hashes:  # avoid duplicate inserts
            instance = boarding_pass2 = BoardingPass(id=2, booking_id=2, issued_time=datetime(2023, 8, 16, 10, 15), seat_number="14B")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4887059881417921327)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -3285717652187590995 in succeeded_hashes:  # avoid duplicate inserts
            instance = boarding_pass3 = BoardingPass(id=3, booking_id=3, issued_time=datetime(2023, 9, 17, 11, 30), seat_number="16C")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3285717652187590995)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5118628701249270608 in succeeded_hashes:  # avoid duplicate inserts
            instance = boarding_pass4 = BoardingPass(id=4, booking_id=4, issued_time=datetime(2023, 10, 18, 12, 45), seat_number="18D")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5118628701249270608)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
