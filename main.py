from tkinter import *
from tkinter import ttk
from random import randint as rnd


root = Tk()
root.title('Тренажер устного счета')
point = count = 0
# генерация примера
x1 = StringVar()
x2 = StringVar()
answer = StringVar()
result = StringVar()
status = StringVar()
x1.set(0)
x2.set(0)
answer.set(0)

# создание интерфейса
frm_1 = ttk.Frame(root, padding="30")
frm_1.grid(column=0, row=0, sticky=(W, E))
ttk.Label(frm_1, textvariable=x1, font='Arial 45').grid(row=3, column=1, columnspan=2)
ttk.Label(frm_1, text='+', font='Arial 45').grid(row=3, column=3, sticky=(W, E))
ttk.Label(frm_1, textvariable=x2, font='Arial 45').grid(row=3, column=4, columnspan=2)
ttk.Label(frm_1, text='=', font='Arial 45').grid(row=3, column=6)
equil = ttk.Entry(frm_1, width=3, font='Arial 45', textvariable=answer)
equil.grid(row=3, column=8, sticky=E, padx=20, pady=40)


root.mainloop()