from tkinter import Tk, Button, Label, Entry
from tkinter.ttk import Separator
from functools import partial

import core

def cria_janela():

    janela = Tk()
    janela.title("Calculadora de bhaskara")



    separador = Separator(janela, orient='horizontal')
    separador.pack(fill='x')
    separador.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)


    titulo_bhaskara = Label(separador, text="Cálculadora de Bhaskara", font=("Roboto", 20))
    titulo_bhaskara.grid(column = 0, row = 0, columnspan = 7, padx= 20, pady = 20)


    label_entry_a = Label(separador, text="A:",  font=("Roboto", 15), justify="center")
    label_entry_a.grid(column = 0, row = 1)
    entry_a = Entry(separador, width=7,font=("Roboto", 15), justify="center")
    entry_a.insert(0, "1")
    entry_a.grid(column = 1, row = 1)


    label_entry_b = Label(separador, text="B:",  font=("Roboto", 15) ,justify="center")
    label_entry_b.grid(column = 2, row = 1)
    entry_b = Entry(separador, width=7,font=("Roboto", 15), justify="center")
    entry_b.insert(0, "1")
    entry_b.grid(column = 3, row = 1)


    label_entry_c = Label(separador, text="C:",  font=("Roboto", 15),justify="center")
    label_entry_c.grid(column = 4, row = 1)
    entry_c = Entry(separador, width=7,font=("Roboto", 15), justify="center")
    entry_c.insert(0,"0")
    entry_c.grid(column = 5, row = 1)



    separador2 = Separator(janela, orient='horizontal')
    separador2.pack(fill='x')
    separador2.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)


    label_resposta = Label(separador2,height=2, text="", justify  = "left",font=("Roboto", 15))
    label_resposta.grid(column = 0, row = 1, columnspan = 7)


    label_desenvolvimento_delta = Label(separador2,height=15, text="",justify  = "left",anchor="nw",font=("Arial", 12))
    label_desenvolvimento_delta.grid(column = 0, row = 2)


    label_desenvolvimento_x = Label(separador2,height=15, text="",justify  = "left",anchor="nw",font=("Arial", 12))
    label_desenvolvimento_x.grid(column = 4, row = 2)


    calcula_args = partial(core.calcula, entry_a.get,entry_b.get,entry_c.get, label_resposta,label_desenvolvimento_delta,label_desenvolvimento_x)
    butonn_calcula = Button(separador2, text="Calcular", command=calcula_args, font=("Roboto", 15), justify="center")
    butonn_calcula.grid(column=0, row=0, columnspan=7, padx= 20, pady = 20)

    janela.mainloop()


if __name__ == '__main__':
    cria_janela()