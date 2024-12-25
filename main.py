from db.make import create_tables
from db.stocks import *
from db.users import *
from modules.security import *
from modules.auth import *
from modules.finance import *
create_tables()

dat = grab_data("AAPL")



