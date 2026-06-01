import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# -----------------------
# INIT HID
# -----------------------
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# -----------------------
# KEY MAP
# -----------------------
KEYS = {
    "GUI": Keycode.GUI,
    "WINDOWS": Keycode.GUI,
    "CTRL": Keycode.CONTROL,
    "ALT": Keycode.ALT,
    "SHIFT": Keycode.SHIFT,

    "ENTER": Keycode.ENTER,
    "TAB": Keycode.TAB,
    "ESC": Keycode.ESCAPE,
    "SPACE": Keycode.SPACE,

    "R": Keycode.R,
}

# -----------------------
# STATUS
# -----------------------
def get_programming_status():
    return False

# -----------------------
# STRING OUTPUT (REAL HID)
# -----------------------
def send_string(text):
    layout.write(text)   # <-- THIS is the actual fix

# -----------------------
# KEY PRESS
# -----------------------
def press_key(key):
    if key in KEYS:
        kbd.press(KEYS[key])
        kbd.release_all()

# -----------------------
# RUN LINE
# -----------------------
def run_line(line):
    line = line.strip()

    if not line or line.startswith("REM"):
        return

    if line.startswith("DELAY"):
        time.sleep(int(line.split()[1]) / 1000)
        return

    if line.startswith("STRING"):
        send_string(line[7:])
        return

    parts = line.split()

    # single key
    if len(parts) == 1:
        key = parts[0].upper()
        if key in KEYS:
            press_key(key)
        return

    # combo (GUI r)
    if len(parts) == 2:
        a, b = parts[0].upper(), parts[1].upper()
        if a in KEYS and b in KEYS:
            kbd.press(KEYS[a], KEYS[b])
            kbd.release_all()
        return

    print("[UNKNOWN]", line)

# -----------------------
# RUN SCRIPT
# -----------------------
def run_script(path):
    try:
        with open(path, "r") as f:
            for line in f:
                print("RUN:", line.strip())
                run_line(line)
                time.sleep(0.01)
    except OSError:
        print("Script not found:", path)