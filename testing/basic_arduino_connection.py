import time
import serial
import serial.tools.list_ports

def get_serial():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description:
            return port.device
    return None

def connect_arduino(port, num):
    ser = serial.Serial(port, 115200)
    time.sleep(2)
    # num = input("Enter an integer ")
    ser.write(f"{num}\n".encode())
    ser.close()

def main():
    port = get_serial()
    connect_arduino(port)

if __name__ == "main":
    main()