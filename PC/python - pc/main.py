# Python on PC
import serial
import time

ser = serial.Serial(
    port = 'COM3', # from device manager
    baudrate = 9600,
    timeout = 1
)

def sendCommand(comm):
    command = '%s\r\f' % comm
    ser.write(command.encode('UTF8'))

def receive():
    line = ser.read_until('\r'.encode('UTF8'))
    print('Message from Microcontroller: %s' % line.decode('UTF8').strip())


if ser.isOpen():
    sendCommand('on()') # turn LED on
    receive()
    time.sleep(2)
    sendCommand('off()') # turn LED off
    receive()
    time.sleep(0.1)
    ser.close()  # close Port
else:
    print('Port is not open!')
