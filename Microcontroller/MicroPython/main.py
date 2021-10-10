# MicroPython
from machine import Pin

led = Pin(25, Pin.OUT)

# Turn the LED on
def on():
    led.value(1)

# Turn the LED off
def off():
    led.value(0)