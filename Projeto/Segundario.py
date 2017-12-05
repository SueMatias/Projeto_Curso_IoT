from __future__ import division
import threading
import time
import Principal

class threadAutomacao(threading.Thread):
	def __init__(self, nome):
		threading.Thread.__init__(self)
		self.nome = nome
		self.executando = False

	def run(self):
		self.executando = True
		print 'Iniciando Thread ', self.nome
		while self.executando:
			print 'Thread Iniciada', self.nome, 				self.executando
			time.sleep(1)

	def parar(self):
		print 'Parando Thread', self.nome
		self.executando = False

	def Automacao_Cooler():
		while True:
			if celsius > 33:
				liga_cooler()
			else:
				desliga_cooler()
			time.sleep(1)
	
	def Automacao_LED():
		while True:
			if luminosidade < 200 :
				liga_LED()
			else:
				desliga_LED()
			time.sleep(1)

	def Automacao_Bomba():
		while True:
			if umidade > 5:
				liga_bomba()
			else:
				desliga_bomba()
			time.sleep(1)

Cooler = threadAutomacao('Cooler')
LED = threadAutomacao('LED')
Bomba = threadAutomacao('Bomba')

Cooler.start()
LED.start()
Bomba.start()
Cooler.Automacao_Cooler()
LED.Automacao_LED()
Bomba.Automacao_Bomba()
