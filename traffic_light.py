from gpiozero import LED
from gpiozero import Button 
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import sys
import signal

# Variables
led_red = LED(13)       # red LED on 13
led_green = LED(26)     # green LED on 26
led_yellow = LED(19)    # yellow LED on 19
button = Button(2)      # button on 2
buzzer = TonalBuzzer(3) # buzzer on 3

# Function - Red State
def state_red():
    # On entrance - turn on red, wait for button press
    print("\n -- Red Light --")
    print("Press button to trigger the green light.")
    led_red.on()
    button.wait_for_press()

    # On exit - turn off red, go to green state
    led_red.off()
    state_green()

# Function - Yellow State
def state_yellow():
    # On entrance - turn on yellow, wait 1 second
    print("\n -- Yellow Light --")
    led_yellow.on()
    sleep(1)

    # On exit - turn off yellow, go to red state
    led_yellow.off()
    state_red()

# Function - Green State
def state_green():
    # On entrance - turn on green
    print("\n -- Green Light --")
    led_green.on()

    # Buzz in quarter-second increments for 2 seconds
    for _ in range(8):
        buzzer.play(Tone("A4"))
        sleep(0.15)
        buzzer.stop()
        sleep(0.10)

    # On exit - turn off green, go to yellow state
    led_green.off()
    state_yellow()

# Function - to handle exit 
def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)


# Initialization

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

print()
print("------------------------")
print("| Python Traffic Light |")
print("------------------------")
print("To exit, type ^C \n")

# Start in the red state
state_red()