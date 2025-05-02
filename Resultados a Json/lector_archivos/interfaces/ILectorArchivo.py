# ILectorArchivo.py
from abc import ABC, abstractmethod


class ILectorArchivo(ABC):
    @abstractmethod
    def leer(self, ruta_archivo):
        """
        Lee el archivo en la ruta especificada y retorna el Modelo de Datos Intermedio (IDM).

        Args:
            ruta_archivo (str): La ruta al archivo que se va a leer.

        Returns:
            object: El Modelo de Datos Intermedio (IDM).  Puede ser una lista de diccionarios,
                    una lista de objetos, un diccionario, o cualquier otra estructura de datos
                    que represente los datos del archivo.  Retorna None si ocurre un error.
        """
        pass
