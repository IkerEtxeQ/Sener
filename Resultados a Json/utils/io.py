import json
import os


def guardar_archivo_json(ruta: str, nombre: str, data: dict) -> None:
    """
    Guarda un diccionario como un archivo JSON en la ruta especificada.

    Args:
        ruta (str): La ruta del directorio donde se guardará el archivo JSON.
        nombre (str): El nombre del archivo JSON (con la extensión .json).
        data (dict): El diccionario que se guardará como JSON.

    Returns:
        None: Esta función no devuelve nada.  Crea un archivo en el disco.
    """
    output_path = os.path.join(ruta, nombre)
    os.makedirs(ruta, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            data, f, indent=4, ensure_ascii=False
        )  # Writing dictionary to JSON file
