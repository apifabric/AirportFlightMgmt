
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Constraint(validate=Passenger, as_condition=lambda row: row.passport_number is not None, error_msg="Passenger passport numbers must be unique")
