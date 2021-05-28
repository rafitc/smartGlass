import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)\
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
lang[] = {"ml", "tn", 'kr', 'hn'}

while(1):
    if GPIO.input(10) == GPIO.HIGH:
        print("Button one was pushed!")
        count += count 
    if GPIO.input(11) == GPIO.HIGH:
        print("Button two was pushed!")
        count -= count