import time
import serial
import serial.tools.list_ports


class SerialConnection:

    def __init__(self):
        self._port = SerialConnection.get_serial()
        self.BAUD_RATE = 115200
        self.ser = serial.Serial(self._port, self.BAUD_RATE)


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
        time.sleep(2)
        self.ser.write(f'{message}\n'.encode())
        print(f'{message}\n')
        time.sleep(2)
        print(str(self.ser.readline().decode('utf-8')))
        print('finished')
        #ser.close()


    def write_num_rotations(self, num):
        time.sleep(2)
        self.ser.write(f"A {num} X\n".encode())
        print('wrote')
        print(self.ser.read_all())
        #ser.close()

    def single_axis_movement(self, axis, distance):
        print(f'distance: {distance}, axis: {axis}')
        self.write(f'A {distance} {axis}')

    def grid_movement(self, x, y, z):
        self.write(f'G {x} {y} {z}')

    def send_emergency_stop(self):
        self.write('S')

    def wafer_matrix(self, wafer_len, wafer_width, matrix_rows, matrix_cols):
        self.write(f'M {wafer_len} {wafer_width} {matrix_rows} {matrix_cols}')

    def zero_grid(self):
        self.write('Z')



if __name__ == "__main__":
    connection = SerialConnection()
    connection.single_axis_movement('X', '5000')