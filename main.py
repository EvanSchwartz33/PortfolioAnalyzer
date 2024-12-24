from db.make import create_tables
from db.stocks import *
from db.users import *
from modules.security import *
from modules.auth import *
create_tables()



print(log_in("Evan33", "MattIsCool"))