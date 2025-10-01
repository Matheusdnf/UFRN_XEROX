import re
from telas import menu_meses


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
    
def verifica_mes(mes):
    meses_dict = {
        "1": "1-JANEIRO", "2": "2-FEVEREIRO", "3": "3-MARÇO", "4": "4-ABRIL",
        "5": "5-MAIO", "6": "6-JUNHO", "7": "7-JULHO", "8": "8-AGOSTO",
        "9": "9-SETEMBRO", "10": "10-OUTUBRO", "11": "11-NOVEMBRO", "12": "12-DEZEMBRO"
    }
    padrao_mes = r"^(1[0-2]|[1-9])"
    match = re.match(padrao_mes, mes)
    if not match:
        return False
    else:
        mes_num = match.group()
        return meses_dict[mes_num]

