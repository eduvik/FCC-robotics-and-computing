#initial tests of radio strength detection
import radio
import random
from microbit import display, Image, button_a, sleep
display.show('a')
# The radio won't work unless it's switched on.
radio.on()



# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send('flash')  # a-ha
    # Read any incoming messages.
    incoming = radio.receive_full()
    if incoming is not None:  #ignore content of message
        #sleep(random.randint(50, 350))
        strength = int((incoming[1] + 255 - 180)/7)
        display.show(str(strength), delay=100, wait=False)
    
