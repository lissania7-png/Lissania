from PyQt5 import QtWidgets, uic
from psp.ejercicio4.psp4 import Intervalos

class VentanaCalculadoraSum4(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("gui/ventana_psp4.ui", self)

        self.x = [130, 650, 99, 150, 128]
        self.y = [186, 699, 132, 272, 291]

        self.btn_calcular4.clicked.connect(self.calcular)

    def calcular(self):
        try:
            xk = float(self.input_xk.text())

            calc = Intervalos(self.x, self.y, xk)
            yk, upi, lpi = calc.calcular()

            self.label_yk.setText(f"{yk:.4f}")
            self.label_upi.setText(f"{upi:.4f}")
            self.label_lpi.setText(f"{lpi:.4f}")

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor ingresa un número válido.")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))