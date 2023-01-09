from mfrc522 import SimpleMFRC522
from time import sleep
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id = reader.read()[0]
        print(f"ID: {id}")
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
