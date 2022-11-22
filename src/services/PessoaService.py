from src.models.PessoaDAO import PessoaDAO
from src.models.PessoaModel import PessoaModel
from abc import abstractmethod

class PessoaService:

    @abstractmethod
    def ordenacao(campo: str, ordem_anterior: str):
        if campo == 'id':
            if ordem_anterior == campo:
                return PessoaDAO.getAllDesc(order=campo)
            else:
                return PessoaDAO.getAllAsc(order=campo)
        elif campo == 'nome':
            if ordem_anterior == campo:
                return PessoaDAO.getAllDesc(order=campo)
            else:
                return PessoaDAO.getAllAsc(order=campo)
        elif campo == 'idade':
            if ordem_anterior == campo:
                return PessoaDAO.getAllDesc(order=campo)
            else:
                return PessoaDAO.getAllAsc(order=campo)
        elif campo == 'sexo':
            if ordem_anterior == campo:
                return PessoaDAO.getAllDesc(order=campo)
            else:
                return PessoaDAO.getAllAsc(order=campo)
        elif campo == 'salario':
            if ordem_anterior == campo:
                return PessoaDAO.getAllDesc(order=campo)
            else:
                return PessoaDAO.getAllAsc(order=campo)
        else:
            return PessoaDAO.getAllAsc(order=campo)
    

    @abstractmethod
    def consulta(field: str, search: str):
        if field == 'nome':
            return PessoaDAO.getLike(field=field, search=search)
        elif field == 'idade':
            return PessoaDAO.getLike(field=field, search=search)
        elif field == 'sexo':
            return PessoaDAO.getLike(field=field, search=search)
        elif field == 'salario':
            return PessoaDAO.getLike(field=field, search=search)
        else:
            return PessoaDAO.getAllAsc()

    @abstractmethod
    def atualizar(id: int, nome: str, idade: int, sexo: str, salario: float):
        pessoa = PessoaDAO.getOne(id=id)

        if nome == None:
            nome = pessoa["nome"]

        if idade == None:
            idade = pessoa["idade"]
        
        if sexo == None:
            sexo = pessoa["sexo"]

        if salario == None:
            salario = pessoa["salario"]
        
        pessoa_update = PessoaModel(
            id=pessoa["id"],
            nome=nome,
            idade=idade,
            sexo=sexo,
            salario=salario
        )
        PessoaDAO.update(pessoa=pessoa_update)