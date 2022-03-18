import random
import tkinter
from logging import root
from tkinter import*
from tkinter import ttk

import tk as tk


co0 = '#ffffff'
co1 = '#000000'
co2 = '#008000'
co3 = '#00ff00'

janela = Tk()
janela.title('DADO')
janela.wm_geometry('430x276')
janela.configure(bg=co1)


frame_cima = Frame(janela, width=215, height=180, bg=co1, pady= 0, padx=0, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NSEW)


frame_cima1 = Frame(janela, width=215, height=180, bg=co1, pady= 0, padx=0, relief='raised')
frame_cima1.grid(row=0, column=1, sticky=NSEW)

frame_baixo = Frame(janela, width=215, height=50, bg=co1, pady=0, padx=0, relief='groove')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

frame_baixo1 = Frame(janela, width=215, height=50, bg=co1, pady=0, padx=0, relief='groove')
frame_baixo1.grid(row=1, column=1, sticky=NSEW)

app_nome = Label(frame_cima, text=' DADOS ', width=23, height=0, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=+0, y=0)


app_nome = Label(frame_cima1, text=' RPG ', width=23, height=0, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co1, fg=co0)
app_nome.place(x=-50, y=0)

def girard4():
    b_d4 = int(random.randint(1, 4))
    l_resultado['text'] = '{}'.format(b_d4)
b_d4 = Button(frame_baixo, command=girard4, text='D4', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d4.grid(row=0, column=0, sticky=NSEW, pady=1.5, padx=0, columnspan=35)


def girard6():
    b_d6 = int(random.randint(1, 6))
    l_resultado['text'] = '{}'.format(b_d6)
b_d6 = Button(frame_baixo, command=girard6, text='D6', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d6.grid(row=1, column=0, sticky=NSEW, pady=1.5, padx=0, columnspan=35)

def girard8():
    b_d8 = int(random.randint(1, 8))
    l_resultado['text'] = '{}'.format(b_d8)
b_d8 = Button(frame_baixo, command=girard8, text='D8', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d8.grid(row=0, column=1, sticky=NSEW, pady=1.5, padx=0, columnspan=35)
b_d8.place(x=108, y=2)

def girard10():
    b_d10 = int(random.randint(1, 10))
    l_resultado['text'] = '{}'.format(b_d10)
b_d10 = Button(frame_baixo, command=girard10, text='D10', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d10.grid(row=0, column=1, sticky=NSEW, pady=1.5, padx=0, columnspan=35)
b_d10.place(x=108, y=50)

def girard12():
    b_d12 = int(random.randint(1, 12))
    l_resultado['text'] = '{}'.format(b_d12)
b_d12 = Button(frame_baixo1, command=girard12, text='D12', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d12.grid(row=0, column=1, sticky=NSEW, pady=1.5, padx=0, columnspan=35)

def girard20():
    b_d20 = int(random.randint(1, 20))
    l_resultado['text'] = '{}'.format(b_d20)
b_d20 = Button(frame_baixo1, command=girard20, text='D20', width=10, height=2, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d20.grid(row=1, column=0, sticky=NSEW, pady=1.5, padx=0, columnspan=35)

def girard100():
    b_d100 = int(random.randint(1, 100))
    l_resultado['text'] = '{}'.format(b_d100)
b_d100 = Button(frame_baixo1, command=girard100, text='D100', width=10, height=5, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
b_d100.grid(row=0, column=1, sticky=NSEW, pady=1.5, padx=0, columnspan=35)
b_d100.place(x=120, y=1.5)

l_resultado = Label(frame_cima1, text='', width=10, height=2, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 29 bold'), bg=co1, fg=co0)
l_resultado.place(x=-40, y=40)


janela.mainloop()