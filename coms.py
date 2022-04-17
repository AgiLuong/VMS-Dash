import serial
import time

serialPort = serial.Serial(
    port="COM12", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
'''
serialPort13 = serial.Serial(
    port="COM13", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
'''
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            data = serialString.decode("Ascii") 
            print("COM12:",data)
            parsed = data.replace(",V,",",A,")
            serialPort.write(b""+parsed)
        except:
            pass
