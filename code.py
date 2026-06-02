import time
import board
import digitalio
import os

from engine import run_script, get_programming_status, kbd

# ----------------------------
# BOOT DELAY (USB settle time)
# ----------------------------
time.sleep(2)

# ----------------------------
# LED SETUP (SAFE FOR PICO W / 2W)
# ----------------------------
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

def blink():
    for _ in range(3):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)

# ----------------------------
# MAIN
# ----------------------------
def main():
    print("System booting...")

    blink()

    print("Checking programming status...")

    if get_programming_status():
        print("Programming mode enabled")
        return

    # ----------------------------
    # SAFE HID RESET
    # ----------------------------
    try:
        kbd.release_all()
    except:
        pass

    time.sleep(1.5)

    # ----------------------------
    # RUN PAYLOAD
    # ----------------------------
    try:
        files = os.listdir("/")
    except:
        files = []

    if "payload.dd" in files:
        print("Running payload.dd")
        run_script("payload.dd")
    else:
        print("No payload found")

    print("Done")

main()
