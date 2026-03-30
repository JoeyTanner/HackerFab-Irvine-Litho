from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, \
    QVBoxLayout, QLabel
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

        button = QPushButton('Connect arduino')
        button.clicked.connect(self.try_motor_connection)
        button.setFixedSize(QSize(120, 50))

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.on_submit_clicked)

        # Spacing distance
        self.spacing_input = QLineEdit()
        self.spacing_input.setPlaceholderText("Spacing distance (mm):")

        # Stopping time
        self.stop_time_input = QLineEdit()
        self.stop_time_input.setPlaceholderText("Stopping time between images (ms):")

        # Emergency stop
        self.emergency_button = QPushButton("EMERGENCY STOP")
        self.emergency_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        #self.emergency_button.clicked.connect(self.on_emergency_stop)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter integer input: ") # Add placeholder text

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.text_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.output_label)

        layout.addWidget(self.spacing_input)
        layout.addWidget(self.stop_time_input)
        layout.addWidget(self.emergency_button)

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
'''
this is where you would implement the method to send a stop command to the arduino when the emergency button is clicked.
u  need to define a method in your basic_arduino_connection class that sends the appropriate command to the arduino to stop it
and then call that method here.

    def on_emergency_stop(self):
    if self._connection:
        self._connection.send_stop()  # define this in basic_arduino_connection
    print("Emergency stop triggered")
'''
def get_integer(self):
        return self.input_text


if __name__ == '__main__':
    # sys.argv allows app to have command line arguments;
    #   QApplication([]) works too
    app = QApplication(sys.argv)

    window = MainWindow()
    # Windows are hidden by default
    window.show()



    # Starts the event loop
    app.exec()