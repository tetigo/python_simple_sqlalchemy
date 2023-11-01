from config import getSession

from orm1_create import Pessoa

session= getSession()

result = session.query(Pessoa).filter(Pessoa.id == 1).all()

print(result[0].nome)

result[0].nome='tiagopower'

# session.add(result[0]) # nem precisa dessa linha, quando faz query, o resultado já tá na session 

session.commit()