import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 50)

        self.circles.append((x, y, diameter))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 0))
        painter.setBrush(QColor(255, 255, 0))

        for circle in self.circles:
            x, y, diameter = circle
            painter.drawEllipse(QPoint(x, y), diameter // 2, diameter // 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())