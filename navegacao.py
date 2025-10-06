import os
from automacao import criar_pastas,juntar_pdfs_e_imagens_turnos
from telas import meu_menu, tela_apresentacao
from valida import entrada_ano, entrada_mes


def nav_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        tela_apresentacao()
        meu_menu()
        choice = input("Digite o número da opção desejada: ")
        if choice == '1':
            ano=entrada_ano()
            print(ano)
            criar_pastas(ano)
        elif choice == '2':
            ano=entrada_ano()
            mes=entrada_mes()
            juntar_pdfs_e_imagens_turnos(ano,mes)
        elif choice == '3':
            print("Saindo do programa...")
            break
        else:
            input("Opção inválida. Tente novamente.")
    input()


   
