from sqlalchemy import or_
from config import getSession
from orm1_create import Pessoa


session= getSession()

result = session.query(Pessoa).all()

for cada in result:
    print(cada)


result = session.query(Pessoa).filter(Pessoa.nome == 'tiago')
result = session.query(Pessoa).filter_by(nome= 'tiago', usuario='tiago').all()
result = session.query(Pessoa).filter(or_(Pessoa.id==1,Pessoa.id==2)).all()


print(result)
# print(result[0].id)