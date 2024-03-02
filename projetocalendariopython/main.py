from tkinter import *
from tkinter import ttk
import calendar

def show_calendar():
    newin = Tk()
    newin.title(f'CALENDARIO {int(calendar_year.get())}')
    newin.resizable(False, False)
    
    year = int(calendar_year.get())
    
    calendar_content = calendar.calendar(year)
    calendar_lb = Label(newin, text=calendar_content, font=('Consolas 10 bold'))
    calendar_lb.grid(row=5, column=0, padx=20)
    
    newin.mainloop()
    
if __name__ == '__main__':
    win = Tk()
    win.title('CALENDARIO')
    win.geometry('500x300')
    win.resizable(False, False)
    
    Label(win, text='CALENDÁRIO', font=('arial 20 bold')).pack(pady=20)
    
    Label(win, text='Introduza o ano:').pack()
    calendar_year = ttk.Entry(win, font=('arial 14 bold'))
    calendar_year.pack()
    
    btn_show_calendar = ttk.Button(win, text='Exibir calendario.', command=show_calendar).pack(pady=20)
    
    btn_show_calendar = ttk.Button(win, text='-> SAIR', command=exit).place(x=265, y=215)
    
    win.mainloop()