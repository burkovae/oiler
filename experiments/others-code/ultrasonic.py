#!/usr/bin/env python
# -*- coding: utf-8 -*-

# code eingelesen aus 
# http://www.forum-raspberrypi.de/Thread-haussteuerung-heizoel-tankstand-oder-verbrauchs-fernablesung-mit-raspi-geloest-beitrag-21?page=3

#Bibliotheken einbinden
import time
import datetime
import RPi.GPIO as GPIO

#GPIO Modus (BOARD / BCM)
#GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIOTrigger = 18
GPIOEcho    = 24
GPIO.setwarnings(False)

# function to measure the distance
def MeasureDistance():
 # setze Trigger auf HIGH
 #time.sleep(0.2)
 GPIO.output(GPIOTrigger, True)

 # setze Trigger nach 0.01ms aus LOW
 GPIO.output(GPIOTrigger, False)

 #StartTime = time.time()
 #StopTime = time.time()

 # speichere Startzeit
 while GPIO.input(GPIOEcho) == 0:
   StartTime = time.time()

 # speichere Ankunftszeit
 while GPIO.input(GPIOEcho) == 1:
   StopTime = time.time()

 # Zeit Differenz zwischen Start und Ankunft
 TimeElapsed = StopTime - StartTime
 Distance = (TimeElapsed * 34300) / 2
 
 return Distance

# main function
def main():
 try:
#    while True:
     Distance0 = MeasureDistance()
     Distance01 = MeasureDistance()
     Distance02 = MeasureDistance()
     Distance03 = MeasureDistance()
     Distance04 = MeasureDistance()
     Distance05 = MeasureDistance()
     Distance06 = MeasureDistance()
     Distance07 = MeasureDistance()
     Distance08 = MeasureDistance()
     Distance09 = MeasureDistance()
     Distance10 = MeasureDistance()
     Distance11 = MeasureDistance()
     Distance12 = MeasureDistance()
     Distance13 = MeasureDistance()
     Distance14 = MeasureDistance()
     Distance15 = MeasureDistance()
     Distance16 = MeasureDistance()
     Distance17 = MeasureDistance()
     Distance18 = MeasureDistance()
     Distance19 = MeasureDistance()
     Distance20 = MeasureDistance()
     Distance_sum = Distance01 + Distance02 + Distance03 + Distance04 + Distance05 + Distance06 + Distance07 + Distance08 + Distance09 + Distance10 + Distance11 + Distance12 + Distance13 + Distance14 + Distance15 + Distance16 + Distance17 + Distance18 + Distance19 + Distance20
     Distance = round(Distance_sum / 20,1)
#    Meine Tanks haben Maximal 4.500 Liter bei 150 cm Fuellhoehe
#    Zusätzlich 4 cm Offset vom Einbauort des Sensors
     Fuelstand = 154 - Distance
     Liter = 4500 / 150 * Fuelstand
     Zeit = time.time()
     ZeitStempel = datetime.datetime.fromtimestamp(Zeit).strftime('%Y-%m-%d_%H:%M:%S')
     print (ZeitStempel),("Entfernung: %.1f cm" % Distance),(" Fuelhoehe: %.1f cm" % Fuelstand),(" Liter: %.0f l" % Liter)
     time.sleep(2)

 # Zuruecksetzen der GPIO-Einstellungen mit Ctrl+C
 except KeyboardInterrupt:
   print("Messung durch Benutzer gestoppt")
   GPIO.cleanup()

if __name__ == '__main__':
 #GPIO Modus (BOARD / BCM)
 GPIO.setmode(GPIO.BCM)

 #Richtung der GPIO-Pins festlegen (IN / OUT)
 GPIO.setup(GPIOTrigger, GPIO.OUT)
 GPIO.setup(GPIOEcho, GPIO.IN)

 # set trigger to false
 time.sleep(0.00001)  
 GPIO.output(GPIOTrigger, False)

 # call main function
 main()
