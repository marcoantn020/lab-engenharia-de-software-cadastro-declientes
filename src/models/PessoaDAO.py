
from src.database.db_mysql import connection
from src.models.PessoaModel import PessoaModel
from abc import abstractmethod

class PessoaDAO:

    @abstractmethod
    def getAllDesc(order: str = "id"):
        query = f"SELECT * FROM bancodb.pessoa ORDER BY {order} DESC"
        return connection.read_query(query=query)


    @abstractmethod
    def getAllAsc(order: str = "id"):
        query = f"SELECT * FROM bancodb.pessoa ORDER BY {order} ASC"
        return connection.read_query(query=query)


    @abstractmethod
    def getLike(field: str, search: str):
        query = f"SELECT * FROM bancodb.pessoa WHERE {field} LIKE '%{search}%'"
        print(query)
        return connection.read_query(query=query)


    @abstractmethod
    def getOne(id: int):
        query = f"SELECT * FROM bancodb.pessoa WHERE id = '{id}'"
        result = connection.read_query(query=query)
        if result:
            return result[0]
        return {}


    @abstractmethod
    def create(pessoa: PessoaModel):
        query = f"""INSERT INTO bancodb.pessoa
                    (nome, idade, sexo, salario)
                    VALUES('{pessoa.nome}', '{pessoa.idade}', '{pessoa.sexo}', '{pessoa.salario}');"""
        return connection.write_query(query=query)


    @abstractmethod
    def update(pessoa: PessoaModel):
        query = f"""UPDATE bancodb.pessoa
            SET nome='{pessoa.nome}', idade='{pessoa.idade}', sexo='{pessoa.sexo}', salario='{pessoa.salario}'
            WHERE id='{pessoa.id}';"""
        return connection.write_query(query=query)
    

    @abstractmethod
    def delete(id: int):
        query = f"DELETE FROM bancodb.pessoa WHERE id = '{id}'"
        return connection.write_query(query=query)