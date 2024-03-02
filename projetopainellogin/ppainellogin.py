import customtkinter as cTkn
from tkinter import *
import database
from tkinter import messagebox

janela = cTkn.CTk()

class application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()
                
    def tema(self): 
        cTkn.set_appearance_mode('dark')
        cTkn.set_default_color_theme('blue')
 
    def tela(self):
        janela.geometry("700x500")
        janela.title("Painel de Login")
        janela.iconbitmap("projetopainellogin/icon/simbolo.ico")
        janela.resizable(False, False)#para não alterar tamanho da janela
    
    def tela_login(self):
    #imagem de fundo 
        img = PhotoImage(file="projetopainellogin/planodefundo/planodefundo.png")
        Label_img = cTkn.CTkLabel(janela, image=img)
        Label_img.place(x=15, y=105)
    #-------------------------
    
        titulo = cTkn.CTkLabel(janela, text='FAÇA LOGIN E ACESSE A LOJA!', text_color='white',font=('arial',18,'bold')).place(x=11, y=35)
        
        #frame
        loginframe = cTkn.CTkFrame(janela, width=400, height=496)
        loginframe.pack(side=RIGHT)
        #-------------------------

        #frame widgets
        Label = cTkn.CTkLabel(loginframe, text='TELA DE LOGIN', text_color='white', font=('arial',25,'bold')).place(x=100, y=40)

        name = cTkn.CTkEntry(loginframe, placeholder_text='Nome do usuario', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', bg_color='transparent', border_width=0, corner_radius=10, font=('arial',18))
        name.place(x=20,y=130)
        name_label = cTkn.CTkLabel(loginframe, text='*O campo usuario é de carater obrigatorio.', text_color='green', font=('arial',10)).place(x=20, y=160)

        senha = cTkn.CTkEntry(loginframe, placeholder_text='Insira sua senha', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', show='*',bg_color='transparent',border_width=0, corner_radius=10, font=('arial',18))
        senha.place(x=20,y=190)
        senha_label = cTkn.CTkLabel(loginframe, text='*O campo senha é de carater obrigatorio.', text_color='green', font=('arial',10)).place(x=20, y=222)
        #-------------------------

        chekbox = cTkn.CTkCheckBox(loginframe, text='Mantenha-me conectado.').place(x=20, y=260)

        def login():
            msg = messagebox.showinfo(title='Estado de Login', message='Login feito com sucesso.')
        
        loginbtn = cTkn.CTkButton(loginframe, text='LOGIN', command=login, width=350, font=('arial',15),text_color='white', fg_color='blue',hover_color='gray',bg_color='transparent', border_width=0, corner_radius=10).place(x=20, y=310)
        
        def telacadastro():
            #Remover o frame de login
            loginframe.pack_forget()
            
            #criando tela de cadastro
            cadastroframe = cTkn.CTkFrame(janela, width=400, height=496)
            cadastroframe.pack(side=RIGHT)
            
            Label = cTkn.CTkLabel(cadastroframe, text='FAÇA O SEU CADASTRO!', text_color='white', font=('arial',25,'bold')).place(x=46, y=29)
            
            span = cTkn.CTkLabel(cadastroframe, text='Por favor preencha todos os campos corretamente.',text_color='white', font=('arial',10,) ).place(x=20, y=64)
            
            name = cTkn.CTkEntry(cadastroframe, placeholder_text='Nome do usuario', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', bg_color='transparent', border_width=0, corner_radius=10, font=('arial',18))
            name.place(x=20,y=100)
            
            email = cTkn.CTkEntry(cadastroframe, placeholder_text='Email do usuario', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', bg_color='transparent', border_width=0, corner_radius=10, font=('arial',18))
            email.place(x=20,y=160)
            
            senha = cTkn.CTkEntry(cadastroframe, placeholder_text='Insira a senha', width=350, placeholder_text_color='gray', show='*',fg_color='white', text_color='black', bg_color='transparent', border_width=0, corner_radius=10, font=('arial',18))
            senha.place(x=20,y=220)
            
            csenha = cTkn.CTkEntry(cadastroframe, placeholder_text='Confirme a senha', width=350, placeholder_text_color='gray', show='*', fg_color='white', text_color='black', bg_color='transparent', border_width=0, corner_radius=10, font=('Roboto',18))
            csenha.place(x=20,y=280)
            
            chekbox = cTkn.CTkCheckBox(cadastroframe, text='Eu declaro que li e aceito os termos e condições.').place(x=20, y=330)
            
            def salvarusuario():
                msg = messagebox.showinfo(title='Estado de Cadastro', message='Parabéns! Usuario cadastrado com sucesso.')
            
            
            salvarbtn = cTkn.CTkButton(cadastroframe, text='CRIAR CONTA', command=salvarusuario, width=140, font=('arial',15),text_color='white', fg_color='green',hover_color='gray',bg_color='transparent', border_width=0, corner_radius=10).place(x=215, y=380)
            
            def back():
                # removendo frame de cadastro
                cadastroframe.pack_forget()
                
                #devolvendo o frame de login
                loginframe.pack(side=RIGHT)
            
            backbtn = cTkn.CTkButton(cadastroframe, text='VOLTAR', command=back, width=140, font=('arial',15),text_color='white', fg_color='blue',hover_color='gray',bg_color='transparent', border_width=0, corner_radius=10).place(x=35, y=380)
            
            pass
        
        registrospan = cTkn.CTkLabel(loginframe, text='Se não possui cadastro: ', text_color='white', font=('Roboto',18)).place(x=20, y=358)
        registrobtn = cTkn.CTkButton(loginframe, text='CADASTRE-SE', command=telacadastro, width=150, font=('Roboto',15),text_color='white', fg_color='green',hover_color='gray',bg_color='transparent', border_width=0, corner_radius=10).place(x=219, y=358)
        
application()