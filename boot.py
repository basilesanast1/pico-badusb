import board
import digitalio
import storage
import os

# ----------------------------
# OPTIONAL: hardware switch (GP15)
# ----------------------------
# LOW (GND) = disable USB storage (advanced mode)
# HIGH / floating = USB enabled

no_storage_pin = digitalio.DigitalInOut(board.GP15)
no_storage_pin.switch_to_input(pull=digitalio.Pull.UP)

no_storage = not no_storage_pin.value  # True if grounded

# ----------------------------
# SAFE DEFAULT BEHAVIOR
# ----------------------------
# Always keep USB enabled unless GP15 explicitly requests disable

if no_storage:
    print("GP15 active -> Disabling USB drive")
    storage.disable_usb_drive()
else:
    print("USB drive enabled")

# ----------------------------
# OPTIONAL SAFETY OVERRIDE
# ----------------------------
# If you ever get locked out, comment EVERYTHING above
# and leave only:
# print("USB enabled")