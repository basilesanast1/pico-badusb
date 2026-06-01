import time
import board
import pwmio
import digitalio
import os

from engine import run_script, get_programming_status

time.sleep(2)

# LED setup
if board.board_id.startswith("raspberry_pi_pico"):
    led = pwmio.PWMOut(board.LED, frequency=5000)
else:
    led = digitalio.DigitalInOut(board.LED)
    led.switch_to_output()

def blink():
    for _ in range(3):
        try:
            if hasattr(led, "duty_cycle"):
                led.duty_cycle = 20000
                time.sleep(0.2)
                led.duty_cycle = 0
            else:
                led.value = True
                time.sleep(0.2)
                led.value = False
        except:
            pass

def main():
    print("System booting...")

    blink()

    print("Checking programming status...")
    if get_programming_status():
        print("Programming mode enabled")
        return

    if "payload.dd" in os.listdir("/"):
        print("Running payload.dd")
        run_script("payload.dd")
    else:
        print("No payload found")

    print("Done")

main()