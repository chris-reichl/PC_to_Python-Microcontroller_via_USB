#CircuitPython
import supervisor
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()

        if value == 'on()': # Turn the LED on
            led.value = True 
            
        if value == 'off()': # Turn the LED off
            led.value = False