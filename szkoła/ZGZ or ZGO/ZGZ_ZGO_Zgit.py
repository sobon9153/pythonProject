import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class MojaAplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('kalkulator dla Topo')

        zgzs_button = QPushButton('ZGZ', self)
        zgzo_button = QPushButton('ZGO', self)
        self.objasnienie_label = QLabel('Wybierz który program chcesz realizować.', self)

        layout = QVBoxLayout()
        layout.addWidget(zgzs_button)
        layout.addWidget(zgzo_button)
        layout.addWidget(self.objasnienie_label)

        self.setLayout(layout)

        zgzs_button.clicked.connect(self.zgzs_clicked)
        zgzo_button.clicked.connect(self.zgzo_clicked)

    def zgzs_clicked(self):
        self.objasnienie_label.setText('Istotą zadania geodezyjnego zwykłego\n'
                                       '(ZGZ) – jest wyznaczenie współrzędnych prostokątnych punktu końcowego (punkt '
                                       'B),\n'
                                       ' na podstawie współrzędnych prostokątnych punktu wyjściowego (punktu A) oraz\n'
                                       ' azymutu (T-AB) i odległości (-dAB-) między nimi.')

    def zgzo_clicked(self):
        self.objasnienie_label.setText('Istotą zadania geodezyjnego odwrotnego (ZGO)\n jest wyznaczanie azymutu '
                                       'topograficznego (TAB) i odległości (-dAB-) między punktami A i B na podstawie\n'
                                       'współrzędnych prostokątnych punktu A oraz współrzędnych prostokątnych punktu '
                                       'B.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MojaAplikacja()
    window.show()
    sys.exit(app.exec_())
