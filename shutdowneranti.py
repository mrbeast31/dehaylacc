import time
import keyboard

def dont_shutdown_message():
    print("dont shutdown")

while True:
    dont_shutdown_message()
    time.sleep(10)
    if keyboard.is_pressed('q'):  # 'q' tu�una bas�l�rsa program� sonland�r
        break
