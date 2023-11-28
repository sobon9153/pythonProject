import math

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QMessageBox, \
    QInputDialog, QHBoxLayout


def show_error_message(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("Błąd")
    msg.exec_()


class OknoZGZ(QWidget):
    def __init__(self, poprzednie_okno):
        super().__init__()

        self.poprzednie_okno = poprzednie_okno
        self.init_ui()

    def init_ui(self):
        self.setGeometry(500, 300, 260, 200)
        self.setWindowTitle('ZGZ - Azymut')

        self.azymut_label = QLabel('Podaj azymut T z punktu A do punktu B:', self)
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
                show_error_message("Podano azymut spoza zakresu 0- 6000 ")
        except ValueError:
            show_error_message("Podana nieprawidłowa wartość. Spróbuj jeszcze raz.")

        pyqtSignal()

    def show_wspolrzedne_prostokatne_dialog(self, azymut, odleglosc):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Przejdziemy teraz do współrzędnych prostokątnych.\n"
                    "Pamiętaj, aby współrzędne podać w zapisie 5-cyfrowym, np. 39620 lub 39600.\n"
                    "Zależy od Ciebie, z jaką dokładnością chcesz pracować.")

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


class OknoZGO(QWidget):
    def __init__(self, poprzednie_okno):
        super().__init__()

        self.poprzednie_okno = poprzednie_okno
        self.rzedna_a_zgo = None
        self.odcieta_a_zgo = None
        self.rzedna_b_zgo = None
        self.odcieta_b_zgo = None
        self.init_ui()

    def init_ui(self):
        self.setGeometry(500, 300, 250, 250)
        self.setWindowTitle("Współrzędne prostokątne")
        self.wspolrzedne_guzik_a = QLabel("Podaj współrzędne punktu A")
        self.rzedna_a_zgo = QLineEdit(self)
        self.odcieta_a_zgo = QLineEdit(self)

        self.wspolrzedne_guzik_b = QLabel("Podaj współrzędne punktu B")
        self.rzedna_b_zgo = QLineEdit(self)
        self.odcieta_b_zgo = QLineEdit(self)
        self.ok_button = QPushButton('OK', self)
        self.powrot_button = QPushButton('Powrót', self)
        main_layout = QVBoxLayout()

        layout_a = QHBoxLayout()
        layout_a.addWidget(self.wspolrzedne_guzik_a)
        layout_a.addWidget(self.rzedna_a_zgo)
        layout_a.addWidget(self.odcieta_a_zgo)
        main_layout.addLayout(layout_a)

        layout_b = QHBoxLayout()
        layout_b.addWidget(self.wspolrzedne_guzik_b)
        layout_b.addWidget(self.rzedna_b_zgo)
        layout_b.addWidget(self.odcieta_b_zgo)
        main_layout.addLayout(layout_b)

        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.powrot_button)

        self.setLayout(main_layout)
        self.ok_button.clicked.connect(self.przetworz_dane_a)
        self.ok_button.clicked.connect(self.przetworz_dane_b)
        self.ok_button.clicked.connect(self.perform_calculations)

        self.powrot_button.clicked.connect(self.powrot_button_clicked)

    def przetworz_dane_a(self):
        rzedna_a_zgo = self.rzedna_a_zgo.text()
        odcieta_a_zgo = self.odcieta_a_zgo.text()

        if 5 != len(rzedna_a_zgo) or not rzedna_a_zgo.isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Podałeś złe wartości dla rzędnej punktu A. Muszą być to dokładnie 5 cyfr.")
            msg.setWindowTitle("Błąd")
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            return

        if len(odcieta_a_zgo) != 5 or not odcieta_a_zgo.isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Podałeś złe wartości dla odciętej punktu A. Muszą być to dokładnie 5 cyfr.")
            msg.setWindowTitle("Błąd")
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            return

        self.rzedna_a_zgo = int(rzedna_a_zgo)
        self.odcieta_a_zgo = int(odcieta_a_zgo)

    def przetworz_dane_b(self):
        rzedna_b_zgo = self.rzedna_b_zgo.text()
        odcieta_b_zgo = self.odcieta_b_zgo.text()

        if len(rzedna_b_zgo) != 5 or not rzedna_b_zgo.isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Podałeś złe wartości dla rzędnej punktu B. Muszą być to dokładnie 5 cyfr.")
            msg.setWindowTitle("Błąd")
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            return

        if len(odcieta_b_zgo) != 5 or not odcieta_b_zgo.isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Podałeś złe wartości dla ociętej punktu B. Muszą być to dokładnie 5 cyfr.")
            msg.setWindowTitle("Błąd")
            msg.addButton(QMessageBox.Ok)
            msg.exec_()
            return

        self.rzedna_b_zgo = int(rzedna_b_zgo)
        self.odcieta_b_zgo = int(odcieta_b_zgo)

    def perform_calculations(self):
        if self.rzedna_a_zgo is not None and self.odcieta_a_zgo is not None and \
           self.rzedna_b_zgo is not None and self.odcieta_b_zgo is not None:

            przyrost_rzedna1 = self.rzedna_b_zgo - self.rzedna_a_zgo
            przyrost_odcieta1 = self.odcieta_b_zgo - self.odcieta_a_zgo
            dowolna = przyrost_rzedna1 / przyrost_odcieta1
            dowolna = abs(dowolna)
            tan_roznicy_przyrostu = math.atan(dowolna)
            azymut_zgo = tan_roznicy_przyrostu / 0.06
            if przyrost_rzedna1 > 0 and przyrost_odcieta1 > 0:
                ab = azymut_zgo
            elif przyrost_rzedna1 > 0 > przyrost_odcieta1:
                ab = 30.00 - azymut_zgo
            elif przyrost_rzedna1 < 0 and przyrost_odcieta1 < 0:
                ab = 30.00 + azymut_zgo
            elif przyrost_rzedna1 < 0 < przyrost_odcieta1:
                ab = 60.00 - azymut_zgo

            odleglosc_ab = math.sqrt(przyrost_rzedna1 ** 2 + przyrost_odcieta1 ** 2)
            self.show_wyniki_dialog_zgo(przyrost_rzedna1, przyrost_odcieta1, dowolna, tan_roznicy_przyrostu, azymut_zgo, ab, odleglosc_ab)

    def show_wyniki_dialog_zgo(self,przyrost_rzedna1, przyrost_odcieta1, dowolna, tan_roznicy_przyrostu, azymut_zgo, ab, odleglosc_ab):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(
            f"Przyrost rzednej:{przyrost_rzedna1:.2f}\n"f"Przyrost odcięta:{przyrost_odcieta1:.2f}\n"f"Iloczyn przyrostów:{dowolna:.2f}\n"f"tangens podniesiony do -1:{tan_roznicy_przyrostu:.2f}\n"f"Azymut przed czwartakiem:{azymut_zgo:.2f}\n"f"szukany azymut:{ab:.0f}\n"f"Odległość z punktu A do punktu B:{odleglosc_ab:.0f}")
        msg.setWindowTitle("Wyniki obliczeń")
        msg.addButton(QMessageBox.Ok)
        msg.exec_()
        self.close()

    def powrot_button_clicked(self):
        self.close()
        self.poprzednie_okno.show()


class MojaAplikacja(QWidget):
    def __init__(self):
        super().__init__()
        self.okno_zgo = None
        self.okno_zgz = None
        self.init_ui()

    def zgzs_clicked(self):
        if not self.okno_zgz or (self.okno_zgz and not self.okno_zgz.isVisible()):
            self.okno_zgz = OknoZGZ(self)
            self.okno_zgz.show()

    def zgzo_clicked(self):
        if not self.okno_zgo or (self.okno_zgo and not self.okno_zgo.isVisible()):
            self.okno_zgo = OknoZGO(self)
            self.okno_zgo.show()

    def init_ui(self):
        self.setGeometry(500, 250, 400, 200)
        self.setWindowTitle('Pluton Topo')

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
        self.okno_zgz = OknoZGZ(self)
        self.okno_zgz.show()

    def zgzo_clicked(self):
        self.okno_zgo = OknoZGO(self)
        self.okno_zgo.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MojaAplikacja()
    window.show()
    app.exec_()
