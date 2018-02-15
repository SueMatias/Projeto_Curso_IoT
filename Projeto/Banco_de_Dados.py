# -*- coding: latin-1 -*-
import sqlite3
import datetime
import time
import scipy
'''import Segundario'''

def cria_tabela_de_sensores():
	try:
		conect = sqlite3.connect('Status.db')
		cursor = conect.cursor()

		cursor.execute("""
			CREATE TABLE IF NOT EXISTS Dados (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				Tempo TIMESTAMP DEFAULT (DATETIME('now')),
				Temperatura REAL,
				Umidade REAL,
				Luminosidade REAL
			)
		""")
		conect.commit()
		conect.close()
		print('Banco criado com sucesso.')
	except Exception as e:
		print 'except - cria_tabela', e

def retorno_dados_sensores():
	conn = sqlite3.connect('Status.db')
	cursor = conect.cursor()
	if not quantidade:
		cursor.execute("""SELECT * FROM Dados ORDER BY datetime(Tempo) ASC""")
	else:
        	cursor.execute("""SELECT * FROM Dados ORDER BY datetime(Tempo) DESC LIMIT ?""",(quantidade,))
	return cursor.fetchall()

def adiciona_dados_sensores(Temperatura, Umidade, Luminosidade):
	Temp = Principal.leitura_temperatura()
	LDR = Principal.leitura_LDR()
	Umi = Principal.leitura_umidade()
	try:
		conect = sqlite3.connect('Status.db')
		cursor = conect.cursor()
		Tempo  = datetime.datetime.now()
		cursor.execute("""INSERT INTO Dados (Tempo, Temp, Umi, LDR)
							VALUES(?,?,?,?,?,?,?)""",(Tempo, Temperatura, Umidade, Luminosidade))
		conect.commit()
		conect.close()
		if cursor.rowcount > 0:
			print 'Dados inseridos com sucesso'
		else:
			print 'Falha ao inserir os dados. Tente novamente'
	except Exception as e:
		print e
		return False
