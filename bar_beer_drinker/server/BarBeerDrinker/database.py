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

def find_bars(name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT name, city from bars where city = :name;"
        )
        rs = con.execute(query, name=name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def filter_beers(max_price):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * from inventory where item_cost<:max_price;"
        )

        rs = con.execute(query, max_price = max_price)
        results = [dict(row) for row in rs]
        for r in results:
            r['item_cost'] = float(r['item_cost'])
        return results