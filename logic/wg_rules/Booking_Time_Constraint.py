
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.constraint(validate=Booking, as_condition=lambda row: row.date_of_booking <= row.flight.scheduled_departure - timedelta(hours=2), error_msg="Bookings must be made at least 2 hours before departure")
