import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *
from decimal import Decimal
from datetime import date, datetime

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    # Booking Time Constraint 
    # Bookings must be made a certain number of hours before a flight departs.
    Rule.constraint(validate=Booking, as_condition=lambda row: row.date_of_booking <= row.flight.scheduled_departure - timedelta(hours=2), error_msg="Bookings must be made at least 2 hours before departure")
    