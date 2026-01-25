import tkinter as tk
import pandas as pd
from tkinter import filedialog, messagebox


#Função para cadastro de usuário
def cadastro():
    def salvar_dados():
        usuario = input_usuario.get()
        senha = input_senha.get()
        chave = input_chave.get()

# Criação da janela de Login
def tela_de_cadastro():
    def verificar_login():
        usuario = input_usuario.get()
        senha = input_senha.get()
        chave = input_chave.get()
        
        if usuario != '' and senha != '' and chave != '':
            
            novo_usuario = pd.DataFrame([[usuario, senha, chave]])
            
            novo_usuario.to_csv('base_cadastros.csv', mode= 'a', index=False, header=False, sep=';' , encoding='utf-8')
            
            messagebox.showinfo("Login", "Acesso concedido!")
            
            input_chave.delete(0, tk.END) #Limpa campo Chave
            input_senha.delete(0, tk.END) #Limpa campo Senha
            input_usuario.delete(0, tk.END) #Limpa campo Usuário
        else:
            messagebox.showerror("Erro", "Preencha os campos corretamente")
            
    janela_de_login = tk.Tk()
    janela_de_login.title("Cadastro de Usuário")
    janela_de_login.geometry("300x350")

    # Elementos da janela de login
    tk.Label(janela_de_login, text='Usuário').pack(pady=5)
    input_usuario = tk.Entry(janela_de_login)
    input_usuario.pack(pady=5)

    tk.Label(janela_de_login, text='Senha').pack(pady=5)
    input_senha = tk.Entry(janela_de_login, show='*')
    input_senha.pack(pady=5)

    tk.Label(janela_de_login, text='Palavra Chave').pack(pady=5)
    input_chave = tk.Entry(janela_de_login)
    input_chave.pack(pady=5)

    #Botão Entrar
    btn_entrar = tk.Button(janela_de_login, text="Entrar", command=verificar_login)
    btn_entrar.pack(pady=20)

    janela_de_login.mainloop()

tela_de_cadastro()
