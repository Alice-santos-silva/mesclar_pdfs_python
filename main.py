import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def mesclar_pdfs():
    merger = PyPDF2.PdfMerger()

    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            merger.append(arquivo)

    #merger.write("PDF Final.pdf")
    #merger.close()
    #root.quit()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nome_arquivo_final = f"arquivos/PDF_FINAL_{timestamp}.pdf"

    merger.write(nome_arquivo_final)
    merger.close()
    print("PDFs mesclados com sucesso!")

    lista_box.delete(0, tk.END)

def selecionar_arquivos():
    global lista_arquivos
    lista_arquivos = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for arquivo in lista_arquivos:
        lista_box.insert(tk.END, arquivo)

#def remover_arquivo():
    # Remove o arquivo selecionado da lista
   # indice_selecionado = lista_box.curselection()
   # if indice_selecionado:
      #  lista_box.delete(indice_selecionado[0])

if not os.path.exists("arquivos"):
    os.makedirs("arquivos")

root = tk.Tk()
root.title("Mesclar PDFs")

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

lista_box = tk.Listbox(frame_lista, width=50, height=10)
lista_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_box.yview)

btn_selecionar = tk.Button(root, text="Selecionar PDFs", command=selecionar_arquivos)
btn_selecionar.pack(pady=5)

btn_mesclar = tk.Button(root, text="Mesclar PDFs", command=mesclar_pdfs)
btn_mesclar.pack(pady=5)

btn_concluido = tk.Button(root, text="Concluído", command=root.quit)
btn_concluido.pack(pady=5)

root.mainloop()