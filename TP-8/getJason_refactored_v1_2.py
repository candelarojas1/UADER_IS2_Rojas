# getJason_refactored_v1_2.py - Versión 1.2
# Copyright UADER-FCyT-IS202024 - Todos los derechos reservados
# Descripción: Sistema automático de pagos con múltiples cuentas usando patrones de diseño

import json
import os
from datetime import datetime
from abc import ABC, abstractmethod


class JSONLoaderSingleton:
    """Clase Singleton para cargar y obtener datos de un archivo JSON"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JSONLoaderSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = {}

    def load_file(self, filepath):
        if not os.path.exists(filepath):
            # Crea el archivo con contenido predeterminado si no existe
            default_data = {
                "token1": "clavebanco1",
                "token2": "clavebanco2"
            }
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(default_data, file, indent=4)
            print(f"Archivo {filepath} creado automáticamente con valores por defecto.")

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON: {e}") from e

    def get_token_key(self, token):
        if token not in self.data:
            raise ValueError(f"Token '{token}' no encontrado en el JSON.")
        return self.data[token]


class Cuenta:
    """Representa una cuenta bancaria"""
    def __init__(self, token, saldo_inicial):
        self.token = token
        self.saldo = saldo_inicial

    def puede_pagar(self, monto):
        return self.saldo >= monto

    def realizar_pago(self, monto):
        if self.puede_pagar(monto):
            self.saldo -= monto
            return True
        return False


class Pago:
    """Representa un pago realizado"""
    def __init__(self, numero, token, monto):
        self.numero = numero
        self.token = token
        self.monto = monto
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"Pedido #{self.numero} - Banco: {self.token} - "
            f"Monto: ${self.monto} - Fecha: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
        )


class HistorialPagos:
    """Registra y permite iterar sobre pagos realizados"""
    def __init__(self):
        self.pagos = []

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def __iter__(self):
        return iter(self.pagos)


class ManejadorCuenta(ABC):
    """Manejador abstracto del patrón Chain of Responsibility"""
    def __init__(self, cuenta):
        self.cuenta = cuenta
        self.siguiente = None

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def manejar(self, numero_pedido, monto, historial):
        if self.cuenta.puede_pagar(monto):
            self.cuenta.realizar_pago(monto)
            pago = Pago(numero_pedido, self.cuenta.token, monto)
            historial.agregar_pago(pago)
            print(f"✅ Pago realizado: {pago}")
        elif self.siguiente:
            self.siguiente.manejar(numero_pedido, monto, historial)
        else:
            print(f"❌ Pedido #{numero_pedido} - No hay saldo suficiente en ninguna cuenta.")


def main():
    loader = JSONLoaderSingleton()
    loader.load_file("sitedata.json")

    cuenta1 = Cuenta("token1", 1000)
    cuenta2 = Cuenta("token2", 2000)

    handler1 = ManejadorCuenta(cuenta1)
    handler2 = ManejadorCuenta(cuenta2)
    handler1.set_siguiente(handler2)

    historial = HistorialPagos()

    pedidos = [(1, 500), (2, 500), (3, 500), (4, 500), (5, 500), (6, 500)]

    for numero, monto in pedidos:
        handler1.manejar(numero, monto, historial)

    print("\n📋 Historial de pagos:")
    for pago in historial:
        print(pago)


if __name__ == "__main__":
    main()
