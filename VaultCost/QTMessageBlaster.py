
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self, announcement):
        super(MainWindow, self).__init__()
        self.announcement=announcement

        self.layout = QVBoxLayout()
        myLabel="A lean cost spreadsheet could not be found.\n \nAn e-mail was sent requesting a cost estimate."
        self.label = QLabel(myLabel)
        self.label.setFont(QFont('Calibri', 12))

        self.layout.addWidget(self.label)
        self.setWindowTitle("Information")
        self.setLayout(self.layout)

        # setting  the fixed width of window
        self.setFixedWidth(400)
        self.setFixedHeight(100)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
