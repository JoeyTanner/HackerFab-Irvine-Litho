import time
import serial
import serial.tools.list_ports


class SerialConnection:

    def __init__(self):
        self._port = SerialConnection.get_serial()
        self.BAUD_RATE = 115200


    @staticmethod
    def get_serial():
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description:
                print('Arduino connected')
                return port.device
        print('Failed to connect to arduino')
        return None


    def write(self, message: str):
        ser = serial.Serial(self._port, self.BAUD_RATE)
        time.sleep(1)
        ser.write(message.encode())
        ser.close()


    def write_num_rotations(self, num):
        ser = serial.Serial(self._port, self.BAUD_RATE)
        time.sleep(2)
        ser.write(f"X {num}\n".encode())
        ser.close()



if __name__ == "__main__":
    connection = SerialConnection()
    connection.write_num_rotations(1)