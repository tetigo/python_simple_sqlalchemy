from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getSession():
    user='root'
    pasw='root'
    host='localhost'
    port=3306
    db='mydb2'
    conn = f'mysql+pymysql://{user}:{pasw}@{host}:{port}/{db}'
    engine=create_engine(conn, echo=True)
    Session = sessionmaker(engine)
    session=Session()
    return session
