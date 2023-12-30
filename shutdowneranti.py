import time
import keyboard

def dont_shutdown_message():
    print("dont shutdown")

while True:
    dont_shutdown_message()
    time.sleep(10)
    if keyboard.is_pressed('q'):  # 'q' tuþuna basýlýrsa programý sonlandýr
        break
