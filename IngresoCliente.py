# -*- coding: utf8 -*-
from SalidaCliente import SalidaCliente

class IngresoCliente:
""" Muestra todos los datos del vehiculo a estacionar """

def __init__(self):
        self.IngresoCliente = IngresoCliente()
        self.options = {"1": self.numeroPlacaVehiculo,
                        "2": self.marca,
                        "3": self.modelo,
                        "4": self.tipoVehiculo,
                        "5": self.horaIngreso,
                        "6": self.Estado}

        def Mostar_menuIngresoCliente():
            """ Despliega todas las opciones del menu Ingreso Cliente"""
            print("""
                **** Menu Ingreso Cliente ****
                1. Numero de Placa del Vehiculo
                2. Marca
                3. Modelo
                4. Tipo de Vehiculo (Automovil ó Motocicleta)
                5. Hora de Ingreso
                6. Estado
            """)

