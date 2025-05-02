import utils.crear_json as crear_json


def crear_json_desde_resultados(resultados, datos):
    datos = datos
    resultados = resultados

    input_curves = resultados[0]
    precalentando = resultados[1]
    G_result = resultados[2]
    Q_result = resultados[3]
    A_result = resultados[4]
    R_result = resultados[5]

    G = crear_json.G_json(G_result, datos)

    C = crear_json.C_json(input_curves, precalentando, datos)

    A = crear_json.A_json(A_result, Q_result, datos)

    R = crear_json.R_json(R_result, datos)

    L = crear_json.L_json(input_curves, precalentando, datos)

    resultados = [G, C, A, R, L]

    Costs = crear_json.Costs_json(resultados)

    Time = crear_json.Time_json()

    resultados.append(Time)
    resultados.append(Costs)

    dict_json = crear_json.crear_dict_json(resultados)

    return dict_json
