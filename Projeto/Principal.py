import time
from upm import pyupm_temperature as upm
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
pino_sensor_temperatura = 0
pino_cooler = 5
pino_sensor_luminosidade = 15
pino_LED = 4
pino_sensor_umidade = 16
pino_bomba = 6

pinos.pinMode(pino_sensor_luminosidade, pinos.ANALOG_INPUT)
pinos.pinMode(pino_LED, pinos.OUTPUT)
pinos.pinMode(pino_sensor_umidade, pinos.ANALOG_INPUT)
pinos.pinMode(pino_bomba, pinos.OUTPUT)
pinos.pinMode(pino_cooler, pinos.OUTPUT)

def leitura_temperatura():
	temperatura = upm.Temperature(pino_sensor_temperatura)
	celsius = temperatura.value()
	return celsius

def liga_cooler():
	pinos.digitalWrite(pino_cooler, pinos.HIGH)

def desliga_cooler():
	pinos.digitalWrite(pino_cooler, pinos.LOW)

def leitura_LDR():
	luminosidade = pinos.analogRead(pino_sensor_luminosidade)
        return luminosidade
        
def liga_LED():
	pinos.digitalWrite(pino_LED, pinos.HIGH)

def desliga_LED():
	pinos.digitalWrite(pino_LED, pinos.LOW)

def leitura_umidade():
	umidade = pinos.analogRead(pino_sensor_umidade)
        return umidade

def liga_bomba():
	pinos.digitalWrite(pino_bomba, pinos.HIGH)

def desliga_bomba():
	pinos.digitalWrite(pino_bomba, pinos.LOW)
