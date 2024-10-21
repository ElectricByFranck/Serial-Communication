import machine
import time

# Setup UART for transmission
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# Main loop for transmitting data
while True:
    message = "Hello from Pico 1"
    uart.write(message + "\n")  # Send data
    print(f"Sent: {message}")
    time.sleep(2)  # Delay before sending the next message
