import serial

# Create a serial port object with the appropriate settings
ser = serial.Serial(
    port='COM16',      # Change to the name of your COM port (e.g., 'COM1', 'COM2')
    baudrate=9600,    # Set the baud rate to match the device you're connecting to
    timeout=1         # Timeout in seconds (adjust as needed)
)

try:
    while True:
        # Read data from the COM port
        data = ser.readline()
        if data:
            print(data.decode('utf-8').strip())  # Print the received data
except KeyboardInterrupt:
    # Close the serial port when the program is interrupted (e.g., Ctrl+C)
    ser.close() 
