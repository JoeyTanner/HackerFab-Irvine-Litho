from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, \
    QGridLayout, QVBoxLayout, QLabel
from PySide6.QtCore import QSize, Qt
import sys
import basic_arduino_connection

# Subclassing allows customization of the application's main window
class MainWindow(QMainWindow):
    """ Notes:
    For ANY widget:
         - self.setFixedSize(QSize(x, y)) sets fixed pixel size for window
            - self.setMinimumSize( )
            - self.setMaximumSize( )
    Buttons:
        - button.setCheckable(True/False)
        - button.clicked.connect(self.method_name)
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lithostepper GUI')
        self._connection = None

        self.input_text = None
        self.output_label = QLabel("Input will appear here")
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter dummy integer input: ")  # Add placeholder text

        self.output_label_cur_pos = QLabel("Current position will appear here")

        self.connect_button = QPushButton('Connect arduino')
        self.connect_button.clicked.connect(self.try_motor_connection)
        self.connect_button.setFixedSize(QSize(120, 50))

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.on_submit_clicked)

        # Basic x,y,z movement
        self.movement_header = QLabel("Movement Controls (mm)")
        self.movement_header.setAlignment(Qt.AlignCenter)
        self.movement_input = QLineEdit()
        self.movement_input.setPlaceholderText("Enter Distance (mm):")
        self.axis_input1 = QLineEdit()
        self.axis_input1.setPlaceholderText("Axis (X, Y, Z):")
        self.move_button = QPushButton("Submit")
        self.move_button.clicked.connect(self.on_move_clicked)

        # x,y,z rotations
        rotation_header = QLabel("Rotation Controls")
        rotation_header.setAlignment(Qt.AlignCenter)
        self.rotation_input = QLineEdit()
        self.rotation_input.setPlaceholderText("Number of rotations:")
        self.axis_input2 = QLineEdit()
        self.axis_input2.setPlaceholderText("Axis (X, Y, Z):")
        self.rotation_button = QPushButton("Submit")
        #self.rotation_button.clicked.connect(self.on_rotation_clicked)

        # Spacing distance
        spacing_header = QLabel("Spacing Distance (um)")
        spacing_header.setAlignment(Qt.AlignCenter)
        self.spacing_input = QLineEdit()
        self.spacing_input.setPlaceholderText("Spacing distance (mm):")
        self.spacing_button = QPushButton("Submit")
        # self.spacing_button.clicked.connect(on_spacing_input)

        # Stopping time
        stop_time_header = QLabel("Stopping time (ms)")
        self.stop_time_input = QLineEdit()
        self.stop_time_input.setPlaceholderText("Stopping time (ms):")
        self.stop_time_button = QPushButton("Submit")
        # self.stop_time_button.clicked.connect(on_stop_time)

        # Emergency stop
        self.emergency_button = QPushButton("EMERGENCY STOP")
        self.emergency_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.emergency_button.clicked.connect(self.on_emergency_stop)

        # Set exposure time
        exposure_time_header = QLabel("Exposure Time (ms)")
        exposure_time_header.setAlignment(Qt.AlignCenter)
        self.exposure_input = QLineEdit()
        self.exposure_input.setPlaceholderText("Exposure time (ms):")
        self.exposure_button = QPushButton("Submit")
        #self.exposure_button.clicked.connect(self.on_exposure_clicked)

        # Enter wafer dimensions
        wafer_matrix_header = QLabel("Wafer Matrix (um)")
        wafer_matrix_header.setAlignment(Qt.AlignCenter)

        self.wafer_len = QLineEdit()
        self.wafer_len.setPlaceholderText("Wafer length: ")  # Add placeholder text

        self.wafer_width = QLineEdit()
        self.wafer_width.setPlaceholderText("Wafer width: ")  # Add placeholder text

        self.matrix_rows = QLineEdit()
        self.matrix_rows.setPlaceholderText("Matrix rows: ")

        self.matrix_cols = QLineEdit()
        self.matrix_cols.setPlaceholderText("Matrix cols: ")

        self.submit_wafer_matrix = QPushButton("Submit")
        self.submit_wafer_matrix.clicked.connect(self.on_submit_wafer_matrix)

        # Get current position (NOT IMPLEMENTED)
        self.get_cur_pos = QPushButton("Get current position")
        self.get_cur_pos.clicked.connect(self.on_get_cur_pos)

        # Zero grid
        self.zero_grid = QPushButton("Zero grid")
        self.zero_grid.clicked.connect(self.on_zero_grid)

        layout = QGridLayout()
        layout.addWidget(self.connect_button, 0, 0)
        layout.addWidget(self.text_input, 1, 0)
        layout.addWidget(self.submit_button, 2, 0)
        layout.addWidget(self.output_label, 3, 0)

        layout.addWidget(self.movement_header, 0, 1)
        layout.addWidget(self.movement_input, 1, 1)
        layout.addWidget(self.axis_input1, 2, 1)
        layout.addWidget(self.move_button, 3, 1)

        layout.addWidget(rotation_header, 0, 2)
        layout.addWidget(self.rotation_input, 1, 2)
        layout.addWidget(self.axis_input2, 2, 2)
        layout.addWidget(self.rotation_button, 3, 2)

        layout.addWidget(exposure_time_header, 0, 3)
        layout.addWidget(self.exposure_input, 1, 3)
        layout.addWidget(self.exposure_button, 2, 3)

        layout.addWidget(stop_time_header, 3, 3)
        layout.addWidget(self.stop_time_input, 4, 3)
        layout.addWidget(self.stop_time_button, 5, 3)

        layout.addWidget(spacing_header, 0, 4)
        layout.addWidget(self.spacing_input, 1, 4)
        layout.addWidget(self.spacing_button, 2, 4)

        layout.addWidget(wafer_matrix_header, 0, 5)
        layout.addWidget(self.wafer_len, 1, 5)
        layout.addWidget(self.wafer_width, 2, 5)
        layout.addWidget(self.matrix_rows, 3, 5)
        layout.addWidget(self.matrix_cols, 4, 5)
        layout.addWidget(self.submit_wafer_matrix, 5, 5)

        layout.addWidget(self.get_cur_pos, 0, 6)
        layout.addWidget(self.output_label_cur_pos, 1, 6)

        layout.addWidget(self.zero_grid, 2, 6)

        layout.addWidget(self.emergency_button, 4, 0)

        container = QWidget()
        container.setLayout(layout)

        # Sets the central widget of the Window
        self.setCentralWidget(container)

    def try_motor_connection(self):
        #try:
        self._connection = basic_arduino_connection.SerialConnection()

    def on_submit_clicked(self):
        # Get the text from the QLineEdit using the .text() method
        input_num = self.text_input.text().strip()
        self.output_label.setText(f"You entered: {input_num}")
        self._connection.write_num_rotations(input_num)

    def on_submit_wafer_matrix(self):
        if self.wafer_len.text() == '' or self.wafer_width.text() == '' \
            or self.matrix_rows.text() == '' or self.matrix_cols.text() == '':
            print('Wafer length and width as well as matrix rows and columns must be entered to submit')
            return
        self._connection.wafer_matrix(self.wafer_len.text(), self.wafer_width.text(),
                                      self.matrix_rows.text(), self.matrix_cols.text())

    def on_get_cur_pos(self):
        # print('Requesting current position')
        self.output_label_cur_pos.setText("Current pos requested")
        # add serial code

    def on_move_clicked(self):
        self._connection.single_axis_movement(self.axis_input1.text(), self.movement_input.text())

    def on_emergency_stop(self):
        self._connection.write('S')
        print("Emergency stop triggered")

    def get_integer(self):
        return self.input_text

    def on_zero_grid(self):
        self._connection.zero_grid()


if __name__ == '__main__':
    # sys.argv allows app to have command line arguments;
    #   QApplication([]) works too
    app = QApplication(sys.argv)

    window = MainWindow()
    # Windows are hidden by default
    window.show()



    # Starts the event loop
    app.exec()