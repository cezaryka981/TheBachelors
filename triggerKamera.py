import RPi.GPIO as GPIO
import time
import os

button = 16
led    = 18
				
def setup():
       GPIO.setmode(GPIO.BOARD) #I RPi.GPIO så kan du enten bruke pin numrene (BOARD), eller Broadcom GPIO numrene (BCM). Men man kan kun bruke en av de i et prosjekt.
       GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       GPIO.setup(led, GPIO.OUT)

def loop():
        while True:
              button_state = GPIO.input(button)
              if  button_state == False:
                  GPIO.output(led, True)
	          os.system('./webcam.sh')#os.system lar deg skrive inn terminalkommandoer i pythonprogrammet.
                  print('Picture taken...')
                  os.system('sudo python trueFalseGPIO.py') 
                  while GPIO.input(button) == False:
                    time.sleep(0.2)
              else:
                  GPIO.output(led, False)

def endprogram():
         GPIO.output(led, False)
         GPIO.cleanup() #Denne funksjonen resetter alle porter. Men den påvirker kun de portene som har blitt brukt i programmet. 


if __name__ == '__main__':
          setup()
          try:
                 loop()
          except KeyboardInterrupt:
                 print 'keyboard interrupt detected'
                 endprogram()


