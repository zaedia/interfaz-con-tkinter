import tkinter as tk

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
app = tk.Tk()
app.geometry('500x400')
#app.config(background='black')

lienzo_nuevo = tk.StringVar(app)
lienzo_nuevo.set(crear_lienzo(m,b))
m_nueva = tk.StringVar(app)
m_nueva.set(m)
b_nueva = tk.StringVar(app)
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

func_label = tk.Label(app, textvariable=lienzo_nuevo, bg="white", fg="black", height=30 , anchor= tk.CENTER# width=app.winfo_screenwidth()
).grid(row=0,column=0, rowspan=2)
 
tk.Button( app, text='Disminuir m', bg="darkred", fg='black', command=disminuir_m
).grid(row=0, column=1)

tk.Label( app, textvariable=m_nueva, bg="white", fg="black",
).grid(row=0, column=2)

tk.Button(app, text='Aumentar m', bg="darkred", fg='black', command=aumentar_m
).grid(row=0, column=3)

tk.Button( app, text='Disminuir b', bg="darkred", fg='black', command=disminuir_b
).grid(row=1, column=1)

tk.Label( app, textvariable=b_nueva, bg="white", fg="black",
).grid(row=1, column=2)

tk.Button(app, text='Aumentar b', bg="darkred", fg='black', command=aumentar_b
).grid(row=1, column=3)

print(app.winfo_height())

app.mainloop()
