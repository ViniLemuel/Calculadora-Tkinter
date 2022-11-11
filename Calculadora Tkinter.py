from tkinter import *
root = Tk()
root.Title = "Calculadora do Lemuel"

def click_soma():
    primero_numero = visor.get()
    global p_numero
    global operacao
    operacao = "soma"
    p_numero = float(primero_numero)
    visor.delete(0,END)

def click_sub():
    primero_numero = visor.get()
    global p_numero
    global operacao
    operacao = "subtracao"
    p_numero = float(primero_numero)
    visor.delete(0,END)

def click_multi():
    primero_numero = visor.get()
    global p_numero
    global operacao
    operacao = "multiplicacao"
    p_numero = float(primero_numero)
    visor.delete(0,END)

def click_div():
    primero_numero = visor.get()
    global p_numero
    global operacao
    operacao = "div"
    p_numero = float(primero_numero)
    visor.delete(0,END)

def click_igual():
    segundo_numero = visor.get()
    visor.delete(0,END)

    if operacao == "soma":
        visor.insert(0, p_numero + float(segundo_numero))

    if operacao == "subtracao":
        visor.insert(0, p_numero - float(segundo_numero))

    if operacao == "multiplicacao":
        visor.insert(0, p_numero * float(segundo_numero))

    if operacao == "div":
        visor.insert(0, p_numero / float(segundo_numero))

def delete():
    visor.delete(0,END)

def click_ponto():
    visor.insert(END, ".")

def click_button(numero):
    atual= visor.get()
    visor.delete(0,END)
    visor.insert(END, str(atual)+str(numero))

lb1=Label(root, text="CALCULADORA", font= ("arial", 20, "bold"), pady=10)
lb1.pack()

visor = Entry(root,bg="lightblue")
visor.pack()

#fileira1

bt1 = Button(root, text="1", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt1.place(x=10, y=100)

bt1 = Button(root, text="2", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt1.place(x=10, y=155)

bt1 = Button(root, text="3", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt1.place(x=10, y=210)

bt1 = Button(root, text="0", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt1.place(x=10, y=265)

#fileira2

bt1 = Button(root, text="4", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt1.place(x=60, y=100)

bt1 = Button(root, text="5", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt1.place(x=60, y=155)

bt1 = Button(root, text="6", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt1.place(x=60, y=210)

bt1 = Button(root, text=".", bg="white", pady=14, padx=41, bd=4, command=click_ponto)
bt1.place(x=60, y=265)

#fileira3

bt1 = Button(root, text="7", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt1.place(x=110, y=100)

bt1 = Button(root, text="8", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt1.place(x=110, y=155)

bt1 = Button(root, text="9", bg="white", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt1.place(x=110, y=210)

#fileira4

bt1 = Button(root, text="+", bg="white", pady=14, padx=14, bd=4, command=click_soma)
bt1.place(x=160, y=100)

bt1 = Button(root, text="-", bg="white", pady=14, padx=14, bd=4, command=click_sub)
bt1.place(x=160, y=155)

bt1 = Button(root, text="x", bg="white", pady=14, padx=14, bd=4, command=click_multi)
bt1.place(x=160, y=210)

bt1 = Button(root, text="/", bg="white", pady=14, padx=14, bd=4, command=click_div)
bt1.place(x=160, y=265)

#botaoCE

bt1 = Button(root, text="CE", bg="white", pady=97, padx=14, bd=4, command=delete)
bt1.place(x=210, y=100)

#botaoIgual

bt1 = Button(root, text="=", bg="white", pady=14, padx=119, bd=4, command=click_igual)
bt1.place(x=10, y=330)

root.resizable(True, True)
root.geometry('280x400')
root.mainloop()