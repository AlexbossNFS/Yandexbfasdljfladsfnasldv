import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем интерфейс из файла UI.ui
        uic.loadUi("UI.ui", self)

        # Связываем кнопку с методом добавления окружности
        self.pushButton.clicked.connect(self.add_circle)

        # Список для хранения параметров окружностей
        self.circles = []

    def add_circle(self):
        # Генерация случайного диаметра и позиции
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 50)  # Учитываем высоту кнопки

        # Добавляем параметры окружности в список
        self.circles.append((x, y, diameter))

        # Обновляем окно, чтобы вызвать метод paintEvent
        self.update()

    def paintEvent(self, event):
        # Переопределяем метод paintEvent для отрисовки окружностей
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 0))  # Черный контур
        painter.setBrush(QColor(255, 255, 0))  # Желтая заливка

        # Рисуем все окружности из списка
        for circle in self.circles:
            x, y, diameter = circle
            painter.drawEllipse(QPoint(x, y), diameter // 2, diameter // 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())