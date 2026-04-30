import os
from PyQt5 import QtWidgets, uic

# Importaciones de todas las ventanas
from load.load_ventana1 import VentanaCalculadoraSum
from load.load_ventan2 import VentanaCalculadoraSum2
from load.load_ventana3 import  VentanaCalculadoraSum3
from load.load_ventana4 import  VentanaCalculadoraSum4


class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        ui_path = os.path.join(os.path.dirname(__file__), "..", "gui", "ventana_menu.ui")
        uic.loadUi(ui_path, self)
        self.showMaximized()
        
        
        if hasattr(self, 'actioncalculadora'):
            self.actioncalculadora.triggered.connect(self.abrir_psp1)
        
        if hasattr(self, 'actioncalculadora_psp_2'):
            self.actioncalculadora_psp_2.triggered.connect(self.abrir_psp2)
        
        if hasattr(self, 'actioncalculadora_psp_3'):  
            self.actioncalculadora_psp_3.triggered.connect(self.abrir_psp3)
        
        if hasattr(self, 'actioncalculadora_psp_4'):  
            self.actioncalculadora_psp_4.triggered.connect(self.abrir_psp4)
        
        if hasattr(self, 'actionsalir'):
            self.actionsalir.triggered.connect(self.cerrar_app)

    def abrir_psp1(self):
        self.ventana_psp1 = VentanaCalculadoraSum()
        self.ventana_psp1.show()

    def abrir_psp2(self):
        try:
            self.ventana_psp2 = VentanaCalculadoraSum2()
            self.ventana_psp2.show()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error al abrir PSP 2", str(e))

    def abrir_psp3(self):  
        try:
            self.ventana_psp3 = VentanaCalculadoraSum3()
            self.ventana_psp3.show()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error al abrir PSP 3", str(e))

    def abrir_psp4(self):  
        try:
            self.ventana_psp4 = VentanaCalculadoraSum4()
            self.ventana_psp4.show()
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error al abrir PSP 4", str(e))

    def cerrar_app(self):
        self.close()
            