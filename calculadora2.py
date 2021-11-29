import tkinter as tk
import sys
from tkinter import Place, ttk, messagebox
from tkinter import font
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import BOTTOM
from tkinter.font import Font
from typing import Text

ventana =tk.Tk()
ventana.title("Calculadora")
ventana.resizable(True,True)

#variables#
i=0
error=""
#funsiones del menu#
def salir():
    resultado = messagebox.askyesno(title="salir",message="quieres salir?")
    if resultado == True:sys.exit()

def ayuda():
    messagebox.showwarning(title="Ayuda", message="No se que mas quieres de mi soy una BETA")

def autor():
    messagebox.showinfo(title="Informacion", message="Leonard Amaya")
    
#funsiones de operaciones#
def operaciones():
    global error
    try:
        ecuacion = resultado.get()
        valor = eval(ecuacion)
    except ZeroDivisionError:
        error="Error"
        messagebox.showerror(title="Error", message=f"No se puede dividir por cero")    
    resultado.delete(0, tk.END)
    resultado.insert(0,float(valor))
    tabla_resultados.insert(tk.END,ecuacion)
    tabla_resultados.insert(tk.END,valor)
    i=0
    

#funsiones de accion#
def limpiar():
    tabla_resultados.delete(0, tk.END)
    
def AC():
    resultado.delete(0, tk.END)
    i=0
    
#funsion de botones numericos#
def boton(valor):
    global i
    resultado.insert(i,valor)
    i+=1

#menu de herramientas#
menu=tk.Menu()

#elementos del menu --- primero definir los sub elementos y despues los botones principales#

#elementos del menu --- sub elementos de botonos principales#
menu_archivos=tk.Menu(menu,tearoff=0)
menu_archivos.add_command(label="salir",command=salir)

menu_ayuda=tk.Menu(menu,tearoff=0)
menu_ayuda.add_command(label="ayuda",command=ayuda)
menu_ayuda.add_command(label="autor",command=autor)

#elementos del menu --- botonos principales#
menu.add_cascade(label="archivos",menu=menu_archivos)
menu.add_cascade(label="ayuda",menu=menu_ayuda)

#barra de resultado#
resultado=ttk.Entry(font=("arial 20"),)
resultado.place(x=30,y=30,width=430,height=40)#ubicacion y tamaño#

tabla_resultados=tk.Listbox()
tabla_resultados.place(width=300, height=350,x=485,y=30)

#boton de accion#
boton_limpiar=ttk.Button(text="limpiar",command=limpiar)
boton_limpiar.place(width=300, height=45,x=485,y=382)

#botones de operaciones#
boton_suma = ttk.Button(text="+",command=lambda:boton("+"))
boton_suma.place(x=385, y=90,height=30)
boton_resta = ttk.Button(text="-",command=lambda:boton("-"))
boton_resta.place(x=385, y=130,height=30)
boton_multiplicacion = ttk.Button(text="x",command=lambda:boton("*"))
boton_multiplicacion.place(x=385, y=170,height=30)
boton_division = ttk.Button(text="/",command=lambda:boton("/"))
boton_division.place(x=385, y=210,height=30)

#botones numericos#
numero_uno = ttk.Button(text="1",command=lambda:boton(1))
numero_uno.place(x=30, y=90, width=80,height=30,)
numero_dos = ttk.Button(text="2",command=lambda:boton(2))
numero_dos.place(x=150, y=90, width=80,height=30)
numero_tres = ttk.Button(text="3",command=lambda:boton(3))
numero_tres.place(x=270, y=90, width=80,height=30)
numero_cuatro = ttk.Button(text="4",command=lambda:boton(4))
numero_cuatro.place(x=30, y=130, width=80,height=30)
numero_cinco = ttk.Button(text="5",command=lambda:boton(5))
numero_cinco.place(x=150, y=130, width=80,height=30)
numero_seis = ttk.Button(text="6",command=lambda:boton(6))
numero_seis.place(x=270, y=130, width=80,height=30)
numero_siete = ttk.Button(text="7",command=lambda:boton(7))
numero_siete.place(x=30, y=170, width=80,height=30)
numero_ocho = ttk.Button(text="8",command=lambda:boton(8))
numero_ocho.place(x=150, y=170, width=80,height=30)
numero_nueve = ttk.Button(text="9",command=lambda:boton(9))
numero_nueve.place(x=270, y=170, width=80,height=30)
numero_cero =ttk.Button(text="0",command=lambda:boton(0))
numero_cero.place(x=30, y=210, width=320, height=30)

#botones complementarios#
boton_parentesis1=ttk.Button(text="(",command=lambda:boton("("))
boton_parentesis1.place(x=30, y=250, width=80,height=30,)
boton_parentesis2=ttk.Button(text=")",command=lambda:boton(")"))
boton_parentesis2.place(x=150, y=250, width=80,height=30)
boton_ac=ttk.Button(text="AC",command=lambda: AC())
boton_ac.place(x=270, y=250, width=80,height=30)
boton_punto=ttk.Button(text=".",command=lambda:boton("."))
boton_punto.place(x=385, y=250,height=30)
boton_igual=ttk.Button(text="=",command=lambda:operaciones())
boton_igual.place(x=30, y=290,width=430, height=30)

ventana.config(width=810, height=450,bg='light grey',menu=menu)# definir el ancho y alto de la ventana -- se debe habilitar menu para crear una barra#
ventana.mainloop()