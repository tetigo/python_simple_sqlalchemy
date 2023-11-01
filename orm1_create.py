from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = "root"
HOST = "localhost"
BANCO = "mydb2"
PORT = 3306

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
# session = sessionmaker(create_engine(CONN))()

class Pessoa(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    usuario = Column(String(20))
    senha = Column(String(10))
    
class Categoria(Base):
    __tablename__='categoria'
    id= Column(Integer,primary_key=True)
    nome=Column(String(50), nullable=False)

class Produto(Base):
    __tablename__='produto'
    id=Column(Integer, primary_key=True)
    nome=Column(String(50),nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    

    
Base.metadata.create_all(engine)

