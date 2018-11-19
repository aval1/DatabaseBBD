from sqlalchemy import create_engine
from sqlalchemy import sql

from BarBeerDrinker import config

engine = create_engine(config.database_uri)

def get_total():
    with engine.connect() as con:
        rs = con.execute("SELECT * from bars")
        return [dict(row) for row in rs]
def get_bars():
    with engine.connect() as con:
        rs = con.execute("SELECT name from bars")
        return [dict(row) for row in rs]