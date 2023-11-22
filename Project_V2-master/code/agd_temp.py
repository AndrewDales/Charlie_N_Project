from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Country, CountryMatch

engine = create_engine('sqlite:///World_cup.sqlite3', echo=True)
sess = Session(engine)

match_winner = sess.query(CountryMatch).filter_by(match_id=1, country_id=5).one()
match_winner.score = 3
match_winner.result = "win"

sess.commit()
sess.close()