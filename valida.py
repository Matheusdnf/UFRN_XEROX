import re


def verifica_ano(ano):
    padrao_ano = r"^(20\d{2})$"
    match = re.match(padrao_ano, ano)
    if not match:
        return False
    return ano


def verifica_turno(turno):
    turnos_dict = {
        1: "MANHÃ",
        2: "TARDE",
        3: "NOITE"
    }
    if turno not in turnos_dict:
        return False
    else:    
        return turnos_dict[turno]