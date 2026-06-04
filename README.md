
# Pico BadUSB

A BadUSB flash drive based on the Raspberry Pi Pico

## Authors

- [@basilesanast1](https://www.github.com/basilesanast1)


## Changelog

- Added support for the Raspberry Pi Pico 2W (02/06/2026)
- Cleaned up `code.py`, `engine.py`, `boot.py` and `pins.py` (02/06/2026)
- Added a way to reset your Pico in case you want to get rid of the code (02/06/2026)


## About this project

This is a simple BadUSB engine for the Raspberry Pi Pico and the Raspberry Pi Pico 2W using CircuitPython. It reads raw DuckyScript files and executes them without the need to convert them to `.bin`, thus making the setup process much easier. It supports the official Raspberry Pi Pico and any other compatible boards. Raspberry Pi W/2 is not currently supported. DuckyScript v1.0 works best.


## Installation

Installing this engine on your Raspberry Pi Pico is very easy. All the files needed are in this repository. You will need:

1. CircuitPython 10.2.1 (.uf2 file is on the repository)
2. Raspberry Pi Pico board (any official or knockoff board will do)
3. USB data cable (Micro-USB or Type-C, depends on your board)
4. [Thonny](https://thonny.org/)
5. A 3D-Printed case for your Raspberry Pi Pico (optional)

Download the code as a `.zip` file on your computer and de-compress it. Next, connect your Raspberry Pi Pico to your computer. Drag and drop
`adafruit-circuitpython-raspberry_pi_pico-en_US-10.2.1.uf2` to the Pico's storage. It will automatically reboot and show up as CIRCUITPY. If you are using a
Raspberry Pi Pico 2W, drag and drop `adafruit-circuitpython-raspberry_pi_pico2_w-en_US-10.2.1.uf2` to the Pico's storage.

Next, copy all the files from the `lib` folder of the de-compressed folder and place them in the `lib` folder of your Pico. If the folder does not exist, create it.

Lastly, copy `boot.py`, `code.py`, `pins.py`, and `engine.py` from the de-compressed folder and place them in the root folder of your Pico.

Congratulations. You just made yourself a BadUSB. Now copy your `payload.dd` file on the root folder of your Pico and after it is done, disconnect it from your computer immediatelly, or else the script ypu copied will run.

[Hak5 Payload Library](https://github.com/hak5/usbrubberducky-payloads/tree/master/payloads/library/)


## How to reset your Pico

Connect your Pico to your computer while holding the `BOOTSEL` button. Drag and drop `RP-008273-DS-3-flash_nuke.uf2` to the Pico's storage. It will automatically reboot and return your Pico into a clean like-new state.


## Disclaimer
I am not responsible for any damage that this causes to your system. Use it for educational purposes only, with permission from the target system's owner. Doing otherwise is illegal and could get you in jail.


## Issues

If there is a problem or a bug with this project, open an issue and I will look into it.

## Future Updates

I am expecting to have a web server for the Raspberry Pi Pico 2W working soon. Also multiple payload mode is planned.
