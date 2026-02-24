from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import QSize, Qt
import sys
import serial


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

        button = QPushButton('Run motor')
        button.clicked.connect(self.turn_motor_360_degrees)
        button.setFixedSize(QSize(100, 50))

        # Sets the central widget of the Window
        self.setCentralWidget(button)

    def turn_motor_360_degrees(self):
        print('Simulating turning the motor 360 degrees')


# sys.argv allows app to have command line arguments;
#   QApplication([]) works too
app = QApplication(sys.argv)

window = MainWindow()
# Windows are hidden by default
window.show()

# Starts the event loop
app.exec()