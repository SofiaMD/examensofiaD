# -*- coding: utf8 -*-
import sys
import platform
from  IngresoCliente import IngresoCliente

class menu:

        """Muestra todos los datos que necesita el menu"""

        def __init__(self):
                    self.IngresoCliente = IngresoCliente()
                         self.options = {"1": self.IngresoCleinte,
                                        "2": self.SalidaDelCliente,
                                        "3": self.Buscar,
                                        "4": self.reporte,
                                        "5": self.Salir}

        def Mostar_Menu():
            """ Despliega todas las opciones del menu"""
            print("""
                **** Menu Principal ****
                1. Hora Ingreso
                2. Salida del Cliente
                3. Buscar
                4. Reporte
                5. Salir
            """)
        
            def run(self):
        """ Metodo entrada al menu """
                while True:
                    self.MenuEstacionamiento()
                    choise = input("Ingrese la opción: ")
                    action = self.options.get(choise)

                    if action:
                        action()
                     else:
                        print("¡{0} no es una opción válida!".format(choise))

def IngresoCliente(self, IngresoCliente=None):
        """Despliega Menu para el ingreso del cliente"""
        

      