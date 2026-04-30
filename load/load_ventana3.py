from PyQt5 import QtWidgets, uic
from psp.ejercicio3.psps3 import Correlacion

class VentanaCalculadoraSum3(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("gui/ventana_psp3.ui", self)

       
        self.x = [130, 650, 99, 150, 128]
        self.y = [186, 699, 132, 272, 291]

        if hasattr(self, 'btn_calcular3'):
            self.btn_calcular3.clicked.connect(self.calcular)

    def calcular(self):
        try:
            
            calc = Correlacion(self.x, self.y)
            r, r2, t = calc.calcular()

            self.label_r.setText(f"{r:.4f}")
            self.label_r2.setText(f"{r2:.4f}")
            self.label_t.setText(f"{t:.4f}")

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error en Cálculo", str(e))