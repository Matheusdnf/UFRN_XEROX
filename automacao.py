
from io import BytesIO
import os
import re
from PIL import Image
from pypdf import PdfWriter, PdfReader


def criar_pastas(turno, ano):
    pasta_principal="CONTROLE DE COMPROVANTES"
    base_turno = os.path.join(pasta_principal, turno)   
    base_ano = os.path.join(base_turno, ano)           

    if not os.path.exists(base_turno):
        os.makedirs(base_turno)
        print(f"Turno {turno} criado em {pasta_principal}.")
        input("Pressione Enter para continuar...")
        return

    if os.path.exists(base_ano):
        print(f"O ano {ano} já existe no turno {turno}!")
        input("Pressione Enter para continuar...")
        return

    os.mkdir(base_ano)

    meses = [
        "1-JANEIRO", "2-FEVEREIRO", "3-MARÇO", "4-ABRIL", "5-MAIO", "6-JUNHO",
        "7-JULHO", "8-AGOSTO", "9-SETEMBRO", "10-OUTUBRO", "11-NOVEMBRO", "12-DEZEMBRO"
    ]

    for mes in meses:
        os.mkdir(os.path.join(base_ano, mes))

    print(f"Estrutura criada para o ano {ano} no turno {turno}!")
    input("Pressione Enter para continuar...")



def pasta_relatorio(mes_do_relatorio):
    pasta_destino = f"Relatório {mes_do_relatorio}"
    if not os.path.exists(pasta_destino):
        os.mkdir(pasta_destino)
        print(f"Diretório '{pasta_destino}' criado!")
        input("Pressione Enter para continuar...")
    return pasta_destino

def juntar_pdfs(lista_de_readers, pasta_destino, caminho_para_salvar, mensagem_final):
    writer = PdfWriter()
    for reader in lista_de_readers:
        for page in reader.pages:
            writer.add_page(page)
    nome_pdf_turno = os.path.join(pasta_destino, caminho_para_salvar)
    with open(nome_pdf_turno, "wb") as f_out:
        writer.write(f_out)
    print(mensagem_final)
    input("Pressione Enter para continuar...")



def juntar_pdfs_e_imagens_turnos(ano,mes):
    turnos = ["MANHÃ", "TARDE", "NOITE"]

    pasta_principal="CONTROLE DE COMPROVANTES"

    mes_pasta = mes

    pasta_destino = pasta_relatorio(mes_pasta)

    todos_arquivos_geral = []


    #turno/ano/mes

    for turno in turnos:
        diretorio_turno = os.path.join(pasta_principal,turno, ano, mes_pasta)
        arquivos_turno = []
        if os.path.exists(diretorio_turno):
            for pasta_atual, subpastas, arquivos in os.walk(diretorio_turno):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(pasta_atual, arquivo)
                    arquivos_turno.append(caminho_completo)
        else:
            print(f"Pasta do turno não encontrada: {diretorio_turno}")
            input("Pressione Enter para continuar...")
            continue
        
        if arquivos_turno:
            pdfs_convertidos = []
            for arquivo in arquivos_turno:
                ext = os.path.splitext(arquivo)[1].lower()

            
                if ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
                    img = Image.open(arquivo).convert("RGB")
                    pdf_bytes = BytesIO()
                    img.save(pdf_bytes, format="PDF")
                    pdf_bytes.seek(0)
                    reader = PdfReader(pdf_bytes)
                    pdfs_convertidos.append(reader)

                elif ext == ".pdf":
                    reader = PdfReader(arquivo)
                    pdfs_convertidos.append(reader)

                else:
                    print(f"Arquivo ignorado: {arquivo}")
                    input("Pressione Enter para continuar...")

            caminho_mes= f"{ano}_{mes}_{turno}.pdf"
            mensagem_mes=f"PDF do turno '{turno}' criado com {len(pdfs_convertidos)} arquivos!"

            juntar_pdfs(pdfs_convertidos,pasta_destino,caminho_mes,mensagem_mes)
            todos_arquivos_geral.extend(pdfs_convertidos)


    if todos_arquivos_geral:
        caminho_relatorio= f"{ano}_{mes}_todos_turnos.pdf"
        mensagem_relatorio=f"PDF geral criado com {len(todos_arquivos_geral)} arquivos!"
        input("Pressione Enter para continuar...")
        juntar_pdfs(todos_arquivos_geral,pasta_destino,caminho_relatorio,mensagem_relatorio)
        input("Pressione Enter para continuar...")




