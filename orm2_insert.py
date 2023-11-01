from config import getSession
from orm1_create import Pessoa


session = getSession()

p1 = Pessoa(nome='tiago',usuario='tiago',senha=123)
p2 = Pessoa(nome='marta',usuario='marta',senha=124)
p3 = Pessoa(nome='catarina',usuario='catarina',senha=125)
p4 = Pessoa(nome='beatriz',usuario='beatriz',senha=126)

# session.add(p1)
session.add_all([p2,p3,p4])

session.rollback()

session.commit()