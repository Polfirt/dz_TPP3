import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect, QPoint

class EscapingButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.setFixedSize(100, 50)

    def enterEvent(self, event):
        # Получаем координаты курсора мыши
        cursor_pos = event.pos()
        print(f"Cursor entered at: {cursor_pos}")
        self.rePos()

    def rePos(self):
        x = random.randint(0, 800-100)  #координаты по иксу
        y = random.randint(0, 600-50)   #координаты по игрику
        self.move(x,y) #новые координаты кнопки

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Escaping Button")
        self.setFixedSize(800, 600)

        self.button = EscapingButton("Click Me!")

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
