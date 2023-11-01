from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from orm1_create import Categoria, Produto

def getSession():
    user = 'root'
    pasw = 'root'
    host = 'localhost'
    port = 3306
    db = 'mydb2'

    conn = f'mysql+pymysql://{user}:{pasw}@{host}:{port}/{db}'

    engine = create_engine(conn, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

session = getSession()

c1 = Categoria(nome='frios')
c2 = Categoria(nome='frutas')

session.add_all([c1,c2])

session.rollback()

pro1= Produto(nome='Banana',categoria_id=2)
pro2= Produto(nome='Goiaba',categoria_id=2)

session.add_all([pro1, pro2])

session.rollback()

# session.commit()

for p, c in  session.query(Produto,Categoria).filter(Produto.categoria_id == Categoria.id).all():
    print(p.nome, c.nome)