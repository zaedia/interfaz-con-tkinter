import tkinter as Tk

m = 1
b = 0
dominio = 20
rango = 20

def funcion_lineal(m, x, b):
    y = m*x+b
    return y


def crear_lienzo(m,b):
    lienzo = ""
    for y in range(rango):
        for x in range(dominio):
            if ((rango//2-y) == funcion_lineal(m, (x - dominio//2), b)):
                lienzo += 'a'
            elif (x == (dominio//2) or y == (rango//2)):
                lienzo += 'a'
            
            else:
                lienzo += ' '
        lienzo += '\n'

    return lienzo


# Creacion de la interfaz grafica
ventana = Tk()
ventana.geometry('500x500')
alto = ventana.winfo_height()
print(alto)
ventana.config(background='black')


lienzo_nuevo = Tk.StringVar(ventana)
lienzo_nuevo.set(crear_lienzo(m,b))
m_nueva = Tk.StringVar(ventana)
m_nueva.set(m)
b_nueva = Tk.StringVar(ventana)
b_nueva.set(b)


def aumentar_m():
    global m
    m += 1
    actualizar()


def disminuir_m():
    global m
    m -= 1
    actualizar()
    

def aumentar_b():
    global b
    b += 1
    actualizar()


def disminuir_b():
    global b
    b -= 1
    actualizar()
    

def actualizar():
    lienzo_nuevo.set(crear_lienzo(m,b))
    b_nueva.set(b)
    m_nueva.set(m)

func_label = tk.Label(ventana, textvariable=lienzo_nuevo, bg="white", fg="black", height=30 , anchor= tk.CENTER# width=ventana.winfo_screenwidth()
).grid(row=0,column=0, rowspan=2)
 
tk.Button(ventana, text='Disminuir m', bg="darkred", fg='black', command=disminuir_m
).grid(row=0, column=1)

tk.Label(ventana, textvariable=m_nueva, bg="white", fg="black",
).grid(row=0, column=2)

tk.Button(ventana, text='Aumentar m', bg="darkred", fg='black', command=aumentar_m
).grid(row=0, column=3)

tk.Button(ventana, text='Disminuir b', bg="darkred", fg='black', command=disminuir_b
).grid(row=1, column=1)

tk.Label(ventana, textvariable=b_nueva, bg="white", fg="black",
).grid(row=1, column=2)

tk.Button(ventana, text='Aumentar b', bg="darkred", fg='black', command=aumentar_b
).grid(row=1, column=3)

ventana.mainloop()
