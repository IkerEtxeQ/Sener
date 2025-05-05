import json
from ..interfaces import ILectorArchivo


def _convertir_subclaves_a_int(diccionario):
    return {k + 1: v for k, v in enumerate(diccionario.values())}


class LectorJSONResultQ(ILectorArchivo):
    def leer(self, ruta_archivo):
        """
        Lee el archivo JSON en la ruta especificada y retorna el objeto.
        La estructura de datos depende de la estructura del archivo JSON (puede ser un diccionario,
        una lista, etc.).

        Args:
            ruta_archivo (str): La ruta al archivo JSON que se va a leer.

        Returns:
            object | None: El objeto JSON parseado (diccionario, lista, etc.).
                           Retorna None si ocurre un error.
        """
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)  # Carga todo el archivo JSON

            for campo in ["input_curves", "precalentando"]:
                if campo in datos:
                    datos[campo] = _convertir_subclaves_a_int(datos[campo])

            return datos
        except FileNotFoundError:
            print(f"Error: Archivo JSON no encontrado: {ruta_archivo}")
            return None
        except Exception as e:
            print(f"Error al leer el archivo JSON: {e}")
            return None
