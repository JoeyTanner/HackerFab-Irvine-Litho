import time
import serial
import serial.tools.list_ports


class ArduinoConnection:

    BAUD_RATE = 115200

    def __init__(self):
        port = self._find_port()
        if port is None:
            raise RuntimeError("No Arduino found on any serial port")
        self.ser = serial.Serial(port, self.BAUD_RATE, timeout=5.0)
        time.sleep(2)  # Arduino resets on serial connect; wait before sending commands

    @staticmethod
    def _find_port() -> str | None:
        for port in serial.tools.list_ports.comports():
            if "Arduino" in port.description:
                return port.device
        return None

    def _send(self, message: str) -> str:
        self.ser.write(f'{message}\n'.encode())
        return self.ser.readline().decode('utf-8').strip()

    def send_raw(self, command: str) -> str:
        return self._send(command)

    def single_axis_movement(self, axis: str, distance) -> str:
        return self._send(f'A {distance} {axis}')

    def grid_movement(self, x, y, z) -> str:
        return self._send(f'G {x} {y} {z}')

    def emergency_stop(self) -> str:
        return self._send('S')

    def wafer_matrix(self, wafer_len, wafer_width, matrix_rows, matrix_cols) -> str:
        return self._send(f'M {wafer_len} {wafer_width} {matrix_rows} {matrix_cols}')

    def zero_grid(self) -> str:
        return self._send('Z')

    def close(self):
        if self.ser.is_open:
            self.ser.close()
