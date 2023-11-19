import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit


class OknoZGZ(QWidget):
    def __init__(self, poprzednie_okno):
        super().__init__()

        self.poprzednie_okno = poprzednie_okno
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('ZGZ - Podaj Azymut')

        azymut_label = QLabel('Podaj azymut T z punktu do punktu B:', self)
        azymut_input = QLineEdit(self)
        azymut_button = QPushButton('OK', self)
        powrot_button = QPushButton('Powrót', self)

        layout = QVBoxLayout()
        layout.addWidget(azymut_label)
        layout.addWidget(azymut_input)
        layout.addWidget(azymut_button)
        layout.addWidget(powrot_button)

        self.setLayout(layout)

        azymut_button.clicked.connect(self.ok_button_clicked)
        powrot_button.clicked.connect(self.powrot_button_clicked)

    def ok_button_clicked(self):
        try:
            azymut = int(self.findChild(QLineEdit).text())
            print(f"Wprowadzony azymut: {azymut}")
        except ValueError:
            print("Podana nieprawidłowa wartość. Spróbuj jeszcze raz.")

        self.close()

    def powrot_button_clicked(self):
        self.close()
        self.poprzednie_okno.show()


class MojaAplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Kalkulator dla Topo')

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

        self.okno_zgz = OknoZGZ(self)
        self.okno_zgz.show()

    def zgzo_clicked(self):
        self.objasnienie_label.setText('Istotą zadania geodezyjnego odwrotnego (ZGO)-\n jest wyznaczanie azymutu '
                                       'topograficznego (TAB) i odległości (-dAB-) między punktami A i B na podstawie\n'
                                       'współrzędnych prostokątnych punktu A oraz współrzędnych prostokątnych punktu '
                                       'B.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MojaAplikacja()
    window.show()
    sys.exit(app.exec_())
