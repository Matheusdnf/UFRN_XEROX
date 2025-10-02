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

def entrada_ano():
    while True:
        ano = input("Digite o ano (ex: 2023): ")
        if not verifica_ano(ano):
            print("Ano inválido! Digite um ano no formato 20XX.")
        else:
            break
    return ano

def entrada_mes():
    menu_meses()
    while True:
        entrada_mes = input("Digite o mês: ")
        if not verifica_mes(entrada_mes):
            print("Mês inválido! Digete o número que corresponde ao mês!.")
        else:
            mes=verifica_mes(entrada_mes)
            break
    return mes


def entrada_turno():
    while True:
        entrada_turno = int(input("Digite o turno (1 - MANHÃ, 2 - TARDE, 3 - NOITE): "))
        if not verifica_turno(entrada_turno):
            print("Turno inválido!")
        else:
            turno=verifica_turno(entrada_turno)
            break
    return turno
