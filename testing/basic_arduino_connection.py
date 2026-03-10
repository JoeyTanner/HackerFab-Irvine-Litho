import time
import serial
import serial.tools.list_ports

BAUD_RATE = 115200


class SerialConnection:

    def __init__(self):
        self._port = SerialConnection.get_serial()


    @staticmethod
    def get_serial():
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description:
                print('Arduino connected')
                return port.device
        print('Failed to connect to arduino')
        return None


    def write_num_rotations(self, num):
        ser = serial.Serial(self._port, BAUD_RATE)
        time.sleep(2)
        ser.write(f"X {num}\n".encode())
        ser.close()



if __name__ == "__main__":
    connection = SerialConnection()
    connection.write_num_rotations(1)