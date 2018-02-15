from __future__ import division
import threading
import time
import Principal
import Banco_de_Dados

class Automacao(threading.Thread):
	def __init__(self, threadID, nome):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.nome = nome
		self.executando = False

	def run(self):
		self.executando = True
		print "Iniciando processo %s" % (self.nome)
		while self.executando:
			print "Processo %s em funcionamento" % (self.nome)
			time.sleep(60)

	def parar(self):
		print 'Parando Thread', self.nome
		self.executando = False

	def Cooler(self):
		while True:
			if celsius > 33:
				liga_cooler()
			else:
				desliga_cooler()
			time.sleep(60)

	def LED(self):
		while True:
			if luminosidade < 200 :
				liga_LED()
			else:
				desliga_LED()
			time.sleep(60)

	def Bomba(self):
		while True:
			if umidade > 5:
				liga_bomba()
			else:
				desliga_bomba()
			time.sleep(60)

	def Coleta(self):
		while 1:
			Banco_de_Dados.adiciona_dados_sensores(celsius, umidade, luminosidade)
			time.sleep(60)

# Criando as Threads
Cooler_1 = Automacao(1, "Cooler")
LED_1 = Automacao(2, "LED")
Bomba_1 = Automacao(3, "Bomba")
Leitura_1 = Automacao(4, "Coleta")

Cooler_1.start()
LED_1.start()
Bomba_1.start()
Leitura_1.start()
Cooler_1.Cooler()
LED_1.LED()
Bomba_1.Bomba()
Leitura_1.Coleta()
