import time
import board
import digitalio
import storage

time.sleep(0.1)  # stabilise GPIO at boot

# ----------------------------
# GP15 SWITCH
# ----------------------------
no_storage_pin = digitalio.DigitalInOut(board.GP15)
no_storage_pin.switch_to_input(pull=digitalio.Pull.UP)

no_storage = not no_storage_pin.value

# ----------------------------
# USB STORAGE CONTROL
# ----------------------------
if no_storage:
    storage.disable_usb_drive()
else:
    storage.enable_usb_drive()
