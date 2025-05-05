from .lectores import LectorJSON
from .lectores import LectorJSONResultQ


def leer_archivo(archivo_path):
    if archivo_path.endswith("resultados_cuanticos.json"):
        lector = LectorJSONResultQ()
    elif archivo_path.endswith(".json"):
        lector = LectorJSON()
    else:
        raise ValueError("Formato de archivo no soportado. Debe ser .json")

    return lector.leer(archivo_path)  # Llama al método leer() de la interfaz
