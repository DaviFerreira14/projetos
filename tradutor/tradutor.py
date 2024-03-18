import customtkinter as cTkn
from deep_translator import GoogleTranslator


#funções
def traduzir():
    texto_para_traduzir = texto.get()
    linguagem = lang_to_var.get()
    resultado = GoogleTranslator(source='auto',target=linguagem).translate(texto_para_traduzir)    
    texto_traduzido.configure(state='normal')
    texto_traduzido.delete(0, 'end')
    texto_traduzido.insert(0, resultado)
#----------------------------

cTkn.set_appearance_mode('white')
cTkn.set_default_color_theme('green')

janela = cTkn.CTk()
janela.minsize(500,400)
janela.maxsize(600,400)
janela.title('TRADUTOR APP')

cTkn.CTkLabel(janela, text='Tradutor Universal V1.0',text_color='black',font=('Times new roman',25,'bold')).pack(anchor=cTkn.CENTER, pady=10)


#frame
app_frame = cTkn.CTkFrame(janela, width=500, height=500, fg_color='transparent')
app_frame.pack(fill=cTkn.X, padx=20, pady=10)
#----------------------------

#coletando texto do usuario
texto = cTkn.CTkEntry(app_frame, placeholder_text='digite o texto para a tradução: ', width=350, height=35)
texto.pack(padx=20, pady=20)
#----------------------------

#idioma
lang_to_var = cTkn.StringVar(value='english')

lang_list = GoogleTranslator().get_supported_languages()

lang_to = cTkn.CTkOptionMenu(app_frame, values=lang_list, variable=lang_to_var, dropdown_fg_color='white')
lang_to.set('english')
lang_to.pack(pady=5)
#---------------------

#texto traduzido
texto_traduzido = cTkn.CTkEntry(app_frame, placeholder_text='texto traduzido: ', width=350, height=50)
texto_traduzido.pack(padx=30, pady=40)
#----------------------------

#botão
traduzirbtn = cTkn.CTkButton(app_frame, text='traduzir', command=traduzir, font=('Times new roman',15,'bold'), text_color='white', fg_color='black', hover_color='#0d61ba', width=200)
traduzirbtn.pack(padx=40,pady=20)
#----------------------------

janela.mainloop()