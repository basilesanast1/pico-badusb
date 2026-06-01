
# Pico BadUSB

A BadUSB flash drive based on the Raspberry Pi Pico

## Authors

- [@basilesanast1](https://www.github.com/basilesanast1)


## About this project

This is a simple BadUSB engine for the Raspberry Pi Pico using CircuitPython. It reads raw DuckyScript files and executes them without the need to convert them to `.bin` files, thus making the setup process much easier. It supports the official Raspberry Pi Pico and any other compatible boards. Raspberry Pi W/2/2W is not currently supported. DuckyScript v1.0 works best.


## Installation

Installing this engine on your Raspberry Pi Pico is very easy. All the files needed are in this repository. You will need:

1. CircuitPython 10.2.1 (.uf2 file is on the repository)
2. Raspberry Pi Pico board (any official or knockoff board will do)
3. USB data cable (Micro-USB or Type-C, depends on your board)
4. [Thonny](https://thonny.org/)
5. A 3D-Printed case for your Raspberry Pi Pico (optional)

Download the code as a `.zip` file on your computer and de-compress it. Next, connect your Raspberry Pi Pico to your computer. Drag and drop
`adafruit-circuitpython-raspberry_pi_pico-en_US-10.2.1.uf2` on the Pico's storage. It will automatically reboot and show up as CIRCUITPY.

Next, copy all the files from the `lib` folder of the de-compressed folder and place them in the `lib` folder of your Pico. If the folder does not exist, create it.

Lastly, copy `boot.py`, `code.py`, `pins.py`, and `engine.py` from the de-compressed folder and place them in the root folder of your Pico.

Congratulations. You just made yourself a BadUSB. Now copy your "payload.dd" file on the root folder of your Pico and after it is done, disconnect it from your computer immediatelly, or else the script ypu copied will run.

[Hak5 Payload Library](https://github.com/hak5/usbrubberducky-payloads/)
## Disclaimer
I am not responsible for any damage that this causes to your system. Use it for educational purposes only, with permission from the target system's owner. Doing otherwise is illegal and could get you in jail.


## Issues

If there is a problem or a bug with this project, open an issue and I will look into it.

