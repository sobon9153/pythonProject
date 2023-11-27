import math

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QMessageBox, \
    QInputDialog


class OknoZGZ(QWidget):
    def __init__(self, poprzednie_okno):
        super().__init__()

        self.poprzednie_okno = poprzednie_okno
        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('ZGZ - Podaj Azymut')

        self.azymut_label = QLabel('Podaj azymut T z punktu do punktu B:', self)
        self.azymut_input = QLineEdit(self)
        self.azymut_button = QPushButton('OK', self)
        self.powrot_button = QPushButton('Powrót', self)

        layout = QVBoxLayout()
        layout.addWidget(self.azymut_label)
        layout.addWidget(self.azymut_input)
        layout.addWidget(self.azymut_button)
        layout.addWidget(self.powrot_button)

        self.setLayout(layout)

        self.azymut_button.clicked.connect(self.ok_button_clicked)
        self.powrot_button.clicked.connect(self.powrot_button_clicked)

    def ok_button_clicked(self):
        try:
            azymut = int(self.azymut_input.text())
            if 0 <= azymut <= 6000:
                print(f"Wprowadzony azymut: {azymut}")
                odleglosc, ok_pressed = QInputDialog.getInt(self, 'Podaj odległość',
                                                            'Podaj odległość między punktem A i punktem B:')
                if ok_pressed:
                    print(f"Podana odległość: {odleglosc}")
                    self.show_wspolrzedne_prostokatne_dialog(azymut, odleglosc)
            else:
                self.show_error_message("Podano azymut spoza zakresu 0-360 stopni.")
        except ValueError:
            self.show_error_message("Podana nieprawidłowa wartość. Spróbuj jeszcze raz.")

        ok_button_clicked = pyqtSignal()

    def show_wspolrzedne_prostokatne_dialog(self, azymut, odleglosc):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Przejdziemy teraz do współrzędnych prostokątnych.\n"
                    "Pamiętaj, aby współrzędne podać w zapisie 5-cyfrowym, np. 39620 lub 39600.\n"
                    "Zależy od Ciebie, z jaką dokładnością chcesz pracować.")

        # Dodajemy pola do wprowadzenia współrzędnych
        rzedna_a, ok1 = QInputDialog.getInt(self, 'Podaj wartość', 'Podaj rzędna A:')
        odcieta_a, ok2 = QInputDialog.getInt(self, 'Podaj wartość', 'Podaj odciętą A:')

        if ok1 and ok2:
            print(f"Wprowadzone współrzędne prostokątne: rzęda_A={rzedna_a}, odcieta_A={odcieta_a}")
            self.perform_calculations(azymut, odleglosc, rzedna_a, odcieta_a)

    def perform_calculations(self, azymut, odleglosc, rzedna_a, odcieta_a):
        azymut_w_stopniach = azymut * 0.06
        przyrost_rzedna = math.sin(math.radians(azymut_w_stopniach))
        przyrost_odcieta = math.cos(math.radians(azymut_w_stopniach))
        przyrost_a = przyrost_rzedna * odleglosc
        przyrost_b = przyrost_odcieta * odleglosc
        rzedna_b = rzedna_a + przyrost_a
        odcieta_b = odcieta_a + przyrost_b

        self.show_wyniki_dialog(azymut_w_stopniach, przyrost_a, przyrost_b, rzedna_b, odcieta_b)

    def show_wyniki_dialog(self, azymut_w_stopniach, przyrost_a, przyrost_b, rzedna_b, odcieta_b):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Azymut w stopniach: {azymut_w_stopniach:.2f}\n"
                    f"Przyrost rzędna: {przyrost_a:.2f}\n"
                    f"Przyrost odcięta: {przyrost_b:.2f}\n"
                    f"Rzędna B: {rzedna_b:.0f}\n"
                    f"Odcięta B: {odcieta_b:.0f}")
        msg.setWindowTitle("Wyniki obliczeń")
        msg.addButton(QMessageBox.Ok)
        msg.exec_()

        self.close()

    def powrot_button_clicked(self):
        self.close()
        self.poprzednie_okno.show()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Błąd")
        msg.exec_()


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

        zgzs_button.clicked.connect(self.zgzs_clicked)  # Dodaj to połączenie
        zgzo_button.clicked.connect(self.zgzo_clicked)

    def zgzs_clicked(self):
        self.okno_zgz = OknoZGZ(self)  # Tworzymy nowe okno OknoZGZ
        self.okno_zgz.show()  # Pokazujemy nowe okno

    def zgzo_clicked(self):
        self.okno_zgo = OknoZGZ(self)  # Tworzymy nowe okno OknoZGO (przykładowo)
        self.okno_zgo.show()  # Pokazujemy nowe okno


if __name__ == '__main__':
    app = QApplication([])
    window = MojaAplikacja()
    window.show()
    app.exec_()
