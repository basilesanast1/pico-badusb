import digitalio
from digitalio import DigitalInOut, Pull
import board
from adafruit_debouncer import Debouncer

# -----------------------
# BUTTON
# -----------------------
button1_pin = DigitalInOut(board.GP22)
button1_pin.switch_to_input(pull=Pull.UP)
button1 = Debouncer(button1_pin)
button1.update()

# -----------------------
# PAYLOAD SELECT PINS
# -----------------------
payload1Pin = DigitalInOut(board.GP4)
payload1Pin.switch_to_input(pull=Pull.UP)

payload2Pin = DigitalInOut(board.GP5)
payload2Pin.switch_to_input(pull=Pull.UP)

payload3Pin = DigitalInOut(board.GP10)
payload3Pin.switch_to_input(pull=Pull.UP)

payload4Pin = DigitalInOut(board.GP11)
payload4Pin.switch_to_input(pull=Pull.UP)

# -----------------------
# PROGRAM MODE PIN
# -----------------------
progStatusPin = DigitalInOut(board.GP0)
progStatusPin.switch_to_input(pull=Pull.UP)
