from PySide6.QtWidgets import (
    QMainWindow, QWidget, QGridLayout,
    QPushButton, QLineEdit, QLabel, QMessageBox
)
from PySide6.QtCore import QSize, Qt

from arduino_connection import ArduinoConnection


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lithostepper GUI')
        self._connection: ArduinoConnection | None = None

        self._create_widgets()
        self._connect_signals()
        self._arrange_layout()

    # ── Widget creation ────────────────────────────────────────────────────

    def _create_widgets(self):
        self.connect_button = QPushButton('Connect Arduino')
        self.connect_button.setFixedSize(QSize(140, 50))

        self.emergency_button = QPushButton('EMERGENCY STOP')
        self.emergency_button.setStyleSheet(
            'background-color: red; color: white; font-weight: bold;'
        )

        # Raw command (debug / manual)
        self.raw_input = QLineEdit()
        self.raw_input.setPlaceholderText('Raw command:')
        self.raw_submit = QPushButton('Send')
        self.raw_output = QLabel('—')

        # Single-axis movement
        self.movement_header = QLabel('Single Axis Movement (um)')
        self.movement_header.setAlignment(Qt.AlignCenter)
        self.movement_input = QLineEdit()
        self.movement_input.setPlaceholderText('Distance (um):')
        self.axis_input = QLineEdit()
        self.axis_input.setPlaceholderText('Axis (X, Y, Z):')
        self.move_button = QPushButton('Move')

        # 3D grid movement
        self.move3d_header = QLabel('3D Grid Movement (um)')
        self.move3d_header.setAlignment(Qt.AlignCenter)
        self.x_input = QLineEdit()
        self.x_input.setPlaceholderText('X (um)')
        self.y_input = QLineEdit()
        self.y_input.setPlaceholderText('Y (um)')
        self.z_input = QLineEdit()
        self.z_input.setPlaceholderText('Z (um)')
        self.move3d_button = QPushButton('Move XYZ')

        # Wafer matrix
        self.wafer_matrix_header = QLabel('Wafer Matrix (um)')
        self.wafer_matrix_header.setAlignment(Qt.AlignCenter)
        self.wafer_len_input = QLineEdit()
        self.wafer_len_input.setPlaceholderText('Wafer length (um):')
        self.wafer_width_input = QLineEdit()
        self.wafer_width_input.setPlaceholderText('Wafer width (um):')
        self.matrix_rows_input = QLineEdit()
        self.matrix_rows_input.setPlaceholderText('Matrix rows:')
        self.matrix_cols_input = QLineEdit()
        self.matrix_cols_input.setPlaceholderText('Matrix cols:')
        self.wafer_matrix_button = QPushButton('Submit')

        # Position
        self.cur_pos_label = QLabel('Position: —')
        self.get_cur_pos_button = QPushButton('Get Position')
        self.zero_grid_button = QPushButton('Zero Grid')

    # ── Signal connections ─────────────────────────────────────────────────

    def _connect_signals(self):
        self.connect_button.clicked.connect(self._on_connect)
        self.emergency_button.clicked.connect(self._on_emergency_stop)
        self.raw_submit.clicked.connect(self._on_raw_submit)
        self.move_button.clicked.connect(self._on_move)
        self.move3d_button.clicked.connect(self._on_move3d)
        self.wafer_matrix_button.clicked.connect(self._on_wafer_matrix)
        self.get_cur_pos_button.clicked.connect(self._on_get_cur_pos)
        self.zero_grid_button.clicked.connect(self._on_zero_grid)

    # ── Layout ─────────────────────────────────────────────────────────────

    def _arrange_layout(self):
        layout = QGridLayout()

        # Col 0: connect, raw command, emergency stop
        layout.addWidget(self.connect_button, 0, 0)
        layout.addWidget(self.raw_input, 1, 0)
        layout.addWidget(self.raw_submit, 2, 0)
        layout.addWidget(self.raw_output, 3, 0)
        layout.addWidget(self.emergency_button, 4, 0)

        # Col 1: single-axis movement
        layout.addWidget(self.movement_header, 0, 1)
        layout.addWidget(self.movement_input, 1, 1)
        layout.addWidget(self.axis_input, 2, 1)
        layout.addWidget(self.move_button, 3, 1)

        # Col 2: 3D grid movement
        layout.addWidget(self.move3d_header, 0, 2)
        layout.addWidget(self.x_input, 1, 2)
        layout.addWidget(self.y_input, 2, 2)
        layout.addWidget(self.z_input, 3, 2)
        layout.addWidget(self.move3d_button, 4, 2)

        # Col 3: wafer matrix
        layout.addWidget(self.wafer_matrix_header, 0, 3)
        layout.addWidget(self.wafer_len_input, 1, 3)
        layout.addWidget(self.wafer_width_input, 2, 3)
        layout.addWidget(self.matrix_rows_input, 3, 3)
        layout.addWidget(self.matrix_cols_input, 4, 3)
        layout.addWidget(self.wafer_matrix_button, 5, 3)

        # Col 4: position
        layout.addWidget(self.get_cur_pos_button, 0, 4)
        layout.addWidget(self.cur_pos_label, 1, 4)
        layout.addWidget(self.zero_grid_button, 2, 4)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # ── Slots ──────────────────────────────────────────────────────────────

    def _require_connection(self) -> bool:
        if self._connection is None:
            QMessageBox.warning(self, 'Not Connected', 'Connect to Arduino first.')
            return False
        return True

    def _on_connect(self):
        try:
            self._connection = ArduinoConnection()
            self.connect_button.setText('Connected')
            self.connect_button.setEnabled(False)
        except RuntimeError as e:
            QMessageBox.critical(self, 'Connection Failed', str(e))

    def _on_emergency_stop(self):
        if not self._require_connection():
            return
        self._connection.emergency_stop()

    def _on_raw_submit(self):
        if not self._require_connection():
            return
        response = self._connection.send_raw(self.raw_input.text().strip())
        self.raw_output.setText(response or '—')

    def _on_move(self):
        if not self._require_connection():
            return
        self._connection.single_axis_movement(
            self.axis_input.text().strip(),
            self.movement_input.text().strip()
        )

    def _on_move3d(self):
        if not self._require_connection():
            return
        x = self.x_input.text().strip()
        y = self.y_input.text().strip()
        z = self.z_input.text().strip()
        if not all([x, y, z]):
            QMessageBox.warning(self, 'Input Error', 'X, Y, and Z values are all required.')
            return
        self._connection.grid_movement(x, y, z)

    def _on_wafer_matrix(self):
        if not self._require_connection():
            return
        fields = [
            self.wafer_len_input.text(),
            self.wafer_width_input.text(),
            self.matrix_rows_input.text(),
            self.matrix_cols_input.text(),
        ]
        if not all(fields):
            QMessageBox.warning(self, 'Input Error', 'All wafer matrix fields are required.')
            return
        self._connection.wafer_matrix(*fields)

    def _on_get_cur_pos(self):
        # TODO: implement once Arduino supports a position query command
        self.cur_pos_label.setText('Position: not implemented')

    def _on_zero_grid(self):
        if not self._require_connection():
            return
        self._connection.zero_grid()
