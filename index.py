import pymysql.cursors

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    database='mydb2'
)
def criaTabela(nomeTabela):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"create table if not exists {nomeTabela} (id integer auto_increment, nome varchar(50), primary key(id))")
        print('tabela criada com sucesso')
    except Exception as e:
        print(f"Erro: {e}")


def removeTabela(nomeTabela):
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"drop table if exists {nomeTabela}")
        print('tabela removida com sucesso')
    except Exception as e:
        print(f"Erro: {e}")


def selecionaDaTabela(nomeTabela):
    try:
        with conn.cursor() as cursor:
            # cursor.execute("set @rowid=0;")
            # cursor.execute(f"select @rowid:=@rowid+1 as id, nome from {nomeTabela};")
            cursor.execute(f"select * from {nomeTabela}")
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print(f"Erro: {e}")


def inserirNaTabela(nomeTabela, valor):
    try:
        with conn.cursor() as cursor:
            sql = f'insert into {nomeTabela}(nome) values("{valor}")'
            print(sql)
            cursor.execute(sql)
            conn.commit()
        print('valor inserido com sucesso')
    except Exception as e:
        print(f"Erro: {e}")


def alteraValorDaTabela(nomeTabela, coluna, valor, id):
    try:
        with conn.cursor() as cursor:
            sql = f'update {nomeTabela} set {coluna} = "{valor}" where id = {id}'
            print(sql)
            cursor.execute(sql)
            conn.commit()
        print('valor alterado com sucesso')
    except Exception as e:
        print(f"Erro: {e}")

def removerDaTabela(nomeTabela, id):
    try:
        with conn.cursor() as cursor:
            sql = f'delete from {nomeTabela} where id = {id}'
            print(sql)
            cursor.execute(sql)
            conn.commit()
        print('valor removido com sucesso')
    except Exception as e:
        print(f"Erro: {e}")


# criaTabela('teste')
# removeTabela('teste')
# inserirNaTabela("teste", 'tiago')
# inserirNaTabela("teste", 'marta')
# inserirNaTabela("teste", 'lixox')
# selecionaDaTabela('teste')
# alteraValorDaTabela('teste','nome', 'catarina', 3)
# removerDaTabela('teste', 4)
# selecionaDaTabela('teste')


conn.close()




