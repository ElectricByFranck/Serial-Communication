from machine import UART, Pin

# Initialize UART (tx=Pin 8, rx=Pin 9)
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

# Function to receive data
def receive_data():
    if uart.any():  # Check if data is available
        data = uart.read()  # Read the data
        print('Received:', data)

# Example usage in a loop
while True:
    receive_data()