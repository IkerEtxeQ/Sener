from lector_archivos.lector_archivos import leer_archivo
from capa_logica import crear_json_desde_resultados
from capa_visualizacion import graficar_listas
from utils.result_utils import desplazar_seis_unidades_tiempo
from utils.vector_entrada import json_to_vector_entrada_resultados

datos = leer_archivo("./datos_entrada/datos.json")

### RESULTADOS QUANTICOS ###
resultados_cuánticos = leer_archivo("./datos_entrada/resultados_cuanticos.json")

# ##################### RESULTADOS CLASICOS ##########################

resultados_Sener_json = leer_archivo("./datos_entrada/resultados.json")

resultados_Sener_originales_desplazados = desplazar_seis_unidades_tiempo(
    resultados_Sener_json
)

vector_oferta_C = resultados_Sener_originales_desplazados["C"][0]["x"]

############ GENERADO CLASICO ################
resultados_Sener_vector_entrada = json_to_vector_entrada_resultados(
    resultados_Sener_json
)

resultados_Sener_generados_desplazados = desplazar_seis_unidades_tiempo(
    resultados_Sener_vector_entrada
)

dict_GC = crear_json_desde_resultados(resultados_Sener_generados_desplazados, datos)
# io.guardar_archivo_json("../outputs", "resultados_C.json", dict_GC)

vector_oferta_GC = dict_GC["C"][0]["x"]

### CURVA DE DEMANDA #####
C_Demanda = datos["C"][0]["Consumo"].get("Pot")  # MW/h
vector_demanda_timestep = [x for elem in C_Demanda for x in [elem] * 6]

#### RESULTADOS CUÁNTICOS JSON ######
dict_GQ = crear_json_desde_resultados(list(resultados_cuánticos.values()), datos)
# io.guardar_archivo_json("../outputs", "resultados_Q.json", dict_GQ)

vector_oferta_GQ = dict_GQ["C"][0]["x"]

#### VISUALIZACIÓN ########
labels = ["Demanda", "GeneradoC", "GeneradoQ", "LeidoC"]
markers = ["o", "_", "_", "_"]


graficar_listas(
    vector_demanda_timestep,
    vector_oferta_GC,
    vector_oferta_GQ,
    vector_oferta_C,
    labels=labels,
    markers=markers,
)
