import RPi.GPIO as GPIO
import time
import os


button = 15
greenLed = 13
redLed = 11




def setup():
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       GPIO.setup(redLed, GPIO.OUT)
       GPIO.setup(greenLed, GPIO.OUT)

def loop():
        while True:
              button_state = GPIO.input(button)
              if  button_state == False:
                  GPIO.output(redLed, False)
                  GPIO.output(greenLed, True)
                  print('Computing...')
                  while GPIO.input(button) == False:
                    time.sleep(0.2)
              else:
                  GPIO.output(redLed, True)
                  GPIO.output(greenLed, False)

def endprogram():
         GPIO.output(redLed, False)
         GPIO.output(greenLed, False)
         GPIO.cleanup()


if __name__ == '__main__':
          setup()
          try:
                 loop()
          except KeyboardInterrupt:
                 print 'keyboard interrupt detected'
                 endprogram()

