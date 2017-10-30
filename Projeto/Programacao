import time
from upm import pyupm_temperature as upm
from wiringx86 import GPIOGalileo as GPIO

pinos = GPIO(debug=False)
pino_sensor_temperatura = 0
pino_cooler = 5
pino_sensor_luminosidade = 1
pino_LED = 4
pino_sensor_umidade = 2
pino_bomba = 6

pinos.pinMode(pino_sensor_luminosidade, pinos.ANALOG_INPUT)
pinos.pinMode(pino_LED, pinos.OUTPUT)
pinos.pinMode(pino_sensor_umidade, pinos.ANALOG_INPUT)
pinos.pinMode(pino_bomba, pinos.OUTPUT)
pinos.pinMode(pino_cooler, pinos.OUTPUT)
temperatura = upm.Temperature(0)
luminosidade = pinos.analogRead(pino_sensor_luminosidade)

def leitura_temperatura():
    while True:
        celsius = temperatura.value()
        print celsius
        time.sleep(1)
        if temperatura > 33:
            liga_cooler()
        else:
            desliga_cooler()

def liga_cooler():
  pinos.digitalWrite(pino_cooler, pinos.HIGH)

def desliga_cooler():
  pinos.digitalWrite(pino_cooler, pinos.LOW)

def leitura_LDR():
    while True:
        print luminosidade
        time.sleep(1)
        return luminosidade
        if luminosidade < 5:
            liga_LED()
        else:
            desliga_LED()

def liga_LED():
    pinos.digitalWrite(pino_LED, pinos.HIGH)

def desliga_LED():
    pinos.digitalWrite(pino_LED, pinos.LOW)

def leitura_umidade():
    while 2:
        umidade = pinos.analogRead(pino_sensor_umidade)
        print umidade
        time.sleep(1)
        if umidade < 5:
            liga_bomba()
        else:
            desliga_bomba()

def liga_bomba():
    pinos.digitalWrite(pino_bomba, pinos.HIGH)

def desliga_bomba():
    pinos.digitalWrite(pino_bomba, pinos.LOW)

leitura_LDR()
leitura_temperatura()
