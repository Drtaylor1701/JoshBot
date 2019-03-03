import os
from threading import Timer
import time
import random

def chooseWord():
    wordNumber = random.randint(0, 3)
    word = words[wordNumber]
    os.system("echo " + word)
    os.system("say " + word)

words = ["estachtological", "anthropopathism", "apocrypha", "Apollinarianism"]

for i in range(0, 10):
    #choose an interval
    print("Choose a number of seconds")
    interval = random.randint(1, 10)
    print(str(interval) + " seconds")
    #from Threading module, action that should be run only after whatever time is in inerval is past, uses "chooseword" function to pick a word to say
    t = Timer(interval, chooseWord)
    #starts the Timer
    t.start()
    #sleeps for whatever time is in interval variable
    time.sleep(interval)
