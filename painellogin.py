import customtkinter as cTkn
from tkinter import *

cTkn.set_appearance_mode('dark')
cTkn.set_default_color_theme('blue')

janela = cTkn.CTk()
janela.geometry("700x500")
janela.title("Painel de Login")
janela.iconbitmap("icons/login_icon_176905.ico")
janela.resizable(False, False)#para não alterar tamanho da janela

titulo = cTkn.CTkLabel(janela, text='FAÇA LOGIN E ACESSE A LOJA', text_color='pink',font=('Roboto',18,'bold')).place(x=15, y=15)

#imagem de fundo
img = PhotoImage(file="planodefundo/planodefundo.png")
Label_img = cTkn.CTkLabel(janela, image=img)
Label_img.place(x=15, y=105)
#-------------------------

#frame
frame = cTkn.CTkFrame(janela, width=400, height=496)
frame.pack(side=RIGHT)
#-------------------------

#frame widgets
Label = cTkn.CTkLabel(frame, text='TELA DE LOGIN', text_color='white', font=('Roboto',25,'bold')).place(x=20, y=18)

name = cTkn.CTkEntry(frame, placeholder_text='Nome do usuario:', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', bg_color='transparent', border_width=3, corner_radius=3, font=('Roboto',14,'bold'))
name.place(x=20,y=130)
label1 = cTkn.CTkLabel(frame, text='*O campo usuario é de carater obrigatorio.', text_color='green', font=('Roboto',8,'bold')).place(x=20, y=155)

senha = cTkn.CTkEntry(frame, placeholder_text='Insira sua senha:', width=350, placeholder_text_color='gray', fg_color='white', text_color='black', show='*',bg_color='transparent', border_width=3, corner_radius=3, font=('Roboto',14,'bold'))
senha.place(x=20,y=190)
label2 = cTkn.CTkLabel(frame, text='*O campo senha é de carater obrigatorio.', text_color='green', font=('Roboto',8,'bold')).place(x=20, y=215)
#-------------------------

chekbox = cTkn.CTkCheckBox(frame, text='Mantenha-me conectado.').place(x=20, y=260)

btn = cTkn.CTkButton(frame, text='LOGIN', width=350, command='Login', font=('Roboto',15,'bold'),text_color='black', fg_color='white',hover_color='gray',bg_color='transparent', border_width=3, corner_radius=3).place(x=20, y=310)

janela.mainloop()