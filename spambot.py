from pynput.keyboard import Key, Controller

import time

Keyboard = Controller()

spam=str(input("Enter the spam\n"))

n=int(input("How many spams?\n"))

time.sleep(5)

try:

    for i in range(n):
        time.sleep(0.1)
        for letter in spam:    
                Keyboard.press(letter)
                Keyboard.release(letter)
                time.sleep(0.015)
        Keyboard.press(Key.enter)
        time.sleep(0.015)
        Keyboard.release(Key.enter)

except KeyboardInterrupt: # ctrl + c

    print("Program Terminated")

    exit()
