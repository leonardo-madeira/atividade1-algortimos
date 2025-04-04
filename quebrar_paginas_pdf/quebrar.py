from PyPDF2 import PdfReader, PdfWriter
import os

documento = 'quebrar_paginas_pdf\Parte_1.pdf'


ler = PdfReader(documento)


for i, pagina in enumerate(ler.pages, start=1):
    writer = PdfWriter()
    writer.add_page(pagina)

    diretorio = f'Parte_1\Atividade_{i}'
    
    os.makedirs(diretorio, exist_ok=True)

    caminho_saida = os.path.join(diretorio, f"Atividade_{i}.pdf")

    with open(caminho_saida, "wb") as paginaPdf:
        writer.write(paginaPdf)



            
        
