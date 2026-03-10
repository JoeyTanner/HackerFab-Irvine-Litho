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

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter integer input: ") # Add placeholder text

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.text_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.output_label)

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