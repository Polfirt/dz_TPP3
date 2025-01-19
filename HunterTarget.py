import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QTimer, QPoint

class HunterTarget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Target and Hunter')
        self.setGeometry(100, 100, 800, 500)
        #бахаем кнопки
        self.target = QPushButton('Target', self)
        self.hunter = QPushButton('Hunter', self)
        #размеры кнопок
        self.target.setFixedSize(50, 50)
        self.hunter.setFixedSize(50, 50)
        self.target.setStyleSheet("background-color: blue; color: white;")
        self.hunter.setStyleSheet("background-color: red; color: black;")
        # рандомные позиции начальные
        self.move_button_randomly()
        #таймер для обновления позиции хантера
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_hunter)
        self.timer.start(70)  # Обновляем каждые 70 мс

    def move_button_randomly(self):
        #размеры окна
        window_width = self.width()
        window_height = self.height()
        #рандомные икс и игрик
        target_x = random.randint(0, window_width - 100)
        target_y = random.randint(0, window_height - 100)
        # Перемещаем кнопку
        self.target.move(target_x, target_y)

    def move_hunter(self):
        #текущие позиции кнопок
        target_pos = self.target.pos()
        hunter_pos = self.hunter.pos()
        #проверка пересечения кнопок
        if self.hunter.geometry().intersects(self.target.geometry()):
            # тэпаем таргет
            self.move_button_randomly()
            return

        # Вычисляем вектор направления
        napr = target_pos - hunter_pos
        distance = (napr.x()**2 + napr.y()**2) ** 0.5
        #чтоб на ноль не делилось
        if distance > 0:
            napr = napr / distance
            step_size = 5  # Скорость хантера
            new_hunter = hunter_pos + QPoint(napr.x() * step_size, napr.y() * step_size)
            self.hunter.move(new_hunter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HunterTarget()
    ex.show()
    sys.exit(app.exec_())
