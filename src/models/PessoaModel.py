# from app import db

class PessoaModel:

	def __init__(self,id: int, nome: str, idade: int, sexo: str, salario: float):
		self.__id 	   = id
		self.__nome    = nome
		self.__idade   = idade
		self.__sexo    = sexo
		self.__salario = salario
	
	@property
	def id(self) -> int:
		return self.__id

	@property
	def nome(self) -> str:
		return self.__nome

	@property
	def idade(self) -> int:
		return self.__idade

	@property
	def sexo(self) -> str:
		return self.__sexo

	@property
	def salario(self) -> str:
		return self.__salario

	def __repr__(self):
		return f'<Pessoa {self.__nome}>' 