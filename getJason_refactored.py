"""
Copyright UADER-FCyT-IS2©2024 - Todos los derechos reservados
Programa: getJason_refactored.py
Descripción: Accede a un valor de una clave en un archivo JSON utilizando programación orientada a objetos.
Versión: 1.1
"""

import json
import sys
import os


class JSONLoaderSingleton:
    """Clase Singleton para cargar y obtener datos de archivos JSON"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(JSONLoaderSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = {}

    def load_file(self, filepath):
        """Carga un archivo JSON desde el sistema de archivos"""
        if not os.path.exists(filepath):
            raise ValueError(f"Archivo no encontrado: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                self.data = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error al decodificar JSON: {e}") from e

    def get_value(self, key):
        """Obtiene el valor asociado a una clave del JSON"""
        if key not in self.data:
            raise ValueError(f"La clave '{key}' no se encuentra en el archivo JSON.")
        return self.data[key]


def print_help():
    """Imprime el mensaje de ayuda de uso del programa"""
    print("Uso: python getJason_refactored.py <archivo_json> [clave]")
    print("Opciones:")
    print("  -v           Muestra la versión del programa (1.1)")
    print("  -h, --help   Muestra este mensaje de ayuda")


def main():
    args = sys.argv[1:]

    if not args:
        print("Error: No se pasaron argumentos.")
        print_help()
        sys.exit(1)

    if args[0] in ('-h', '--help'):
        print_help()
        sys.exit(0)

    if args[0] == '-v':
        print("getJason_refactored.py - Versión 1.1")
        sys.exit(0)

    if len(args) < 1 or len(args) > 2:
        print("Error: Número incorrecto de argumentos.")
        print_help()
        sys.exit(1)

    json_file = args[0]
    json_key = args[1] if len(args) == 2 else 'token1'

    try:
        loader = JSONLoaderSingleton()
        loader.load_file(json_file)
        value = loader.get_value(json_key)
        print(str(value))
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
