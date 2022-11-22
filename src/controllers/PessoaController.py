from src import app
from flask import render_template
from flask import request
from src.models.PessoaModel import PessoaModel
from src.models.PessoaDAO import PessoaDAO
from src.services.PessoaService import PessoaService

@app.route('/')
@app.route('/listagem')
def listagem():
	return render_template('listagem.html', pessoas=PessoaDAO.getAllAsc(), ordem='id')

@app.route('/selecao/<int:id>')
def selecao(id=0):
	return render_template('listagem.html', pessoas=PessoaDAO.getOne(id=id), ordem='id')

@app.route('/ordenacao/<campo>/<ordem_anterior>')
def ordenacao(campo='id', ordem_anterior=''):
	pessoas = PessoaService.ordenacao(campo=campo, ordem_anterior=ordem_anterior)
	return render_template('listagem.html', pessoas=pessoas, ordem=campo)	

@app.route('/consulta', methods=['POST'])
def consulta():
	consulta = request.form.get('consulta')
	campo = request.form.get('campo')
	pessoas = PessoaService.consulta(field=campo, search=consulta)
	return render_template('listagem.html', pessoas=pessoas, ordem='id')

@app.route('/insercao')
def insercao():
	return render_template('insercao.html')

@app.route('/salvar_insercao', methods=['POST'])
def salvar_insercao():
	nome = request.form.get('nome')
	idade = int(request.form.get('idade'))
	sexo = request.form.get('sexo')
	salario = float(request.form.get('salario'))

	pessoa = PessoaModel(id=None, nome=nome, idade=idade,sexo=sexo, salario=salario)
	PessoaDAO.create(pessoa=pessoa)
	return render_template('listagem.html', pessoas=PessoaDAO.getAllAsc(), ordem='id')

@app.route('/edicao/<int:id>')
def edicao(id=0):
	return render_template('edicao.html', pessoa=PessoaDAO.getOne(id=id))

@app.route('/salvar_edicao', methods=['POST'])
def salvar_edicao():
	id = int(request.form.get('id'))
	nome = request.form.get('nome')
	idade = int(request.form.get('idade'))
	sexo = request.form.get('sexo')
	salario = float(request.form.get('salario'))

	PessoaService.atualizar(id=id, nome=nome, idade=idade, sexo=sexo, salario=salario)
	return render_template('listagem.html', pessoas=PessoaDAO.getAllAsc(), ordem='id')

@app.route('/delecao/<int:id>')
def delecao(id=0):
	return render_template('delecao.html', pessoa=PessoaDAO.getOne(id=id))

@app.route('/salvar_delecao', methods=['POST'])
def salvar_delecao():
	id = int(request.form.get('id'))
	pessoa = PessoaDAO.getOne(id=id)
	PessoaDAO.delete(id=pessoa["id"])

	return render_template('listagem.html', pessoas=PessoaDAO.getAllAsc(), ordem='id')

@app.route('/graficos')
def graficos():
	pessoasM = PessoaDAO.getLike(field="sexo", search="m")
	pessoasF = PessoaDAO.getLike(field="sexo", search="f")

	salarioM = 0
	for m in pessoasM:
		salarioM += m["salario"]
	if len(pessoasM) > 0:
		salarioM = salarioM / len(pessoasM)

	salarioF = 0
	for f in pessoasF:
		salarioF += f["salario"]
	if len(pessoasF) > 0:
		salarioF = salarioF / len(pessoasF)

	idadeM = 0
	for m in pessoasM:
		idadeM += m["idade"]
	if len(pessoasM) > 0:
		idadeM = idadeM / len(pessoasM)

	idadeF = 0
	for f in pessoasF:
		idadeF += f["idade"]
	if len(pessoasF) > 0:
		idadeF = idadeF / len(pessoasF)

	return render_template('graficos.html', 
							salarioM=salarioM, salarioF=salarioF, idadeM=idadeM, idadeF=idadeF)