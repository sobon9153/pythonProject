import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class MojaAplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Moja Aplikacja PyQt')

        zgzs_button = QPushButton('ZGZ', self)
        zgzo_button = QPushButton('ZGO', self)
        objasnienie_label = QLabel('Wybierz odpowiedni dla Ciebie program.', self)

        layout = QVBoxLayout()
        layout.addWidget(zgzs_button)
        layout.addWidget(zgzo_button)
        layout.addWidget(objasnienie_label)

        self.setLayout(layout)

        zgzs_button.clicked.connect(self.zgzs_clicked)
        zgzo_button.clicked.connect(self.zgzo_clicked)

    def zgzs_clicked(self):
        self.objasnienie_label.setText('ZGZ to zadanie geodezyjne zwykłe.')

    def zgzo_clicked(self):
        self.objasnienie_label.setText('ZGO to zadanie geodezyjne otwarte.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MojaAplikacja()
    window.show()
    sys.exit(app.exec_())
