from config import getSession
from orm1_create import Pessoa


session= getSession()

result = session.query(Pessoa).filter(Pessoa.id == 5).all()

print(result[0].nome)

session.delete(result[0])


session.commit()