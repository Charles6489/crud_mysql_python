import tkinter as tk
from tkinter import ttk
from tkinter import  messagebox as mb
from tkinter import scrolledtext as st
import conexion


class InterfazArticulos:
    def __init__(self):
        self.articulos1 =conexion.Articulos()
        self.ventana = tk.Tk()
        self.ventana.geometry("600x300+300+300")
        self.ventana.title("Interfaz de Mysql")
        self.cuaderno1 = ttk.Notebook(self.ventana)
        self.cargarArticulos()
        self.consultarporcodigo()
        self.listado_completo()
        self.BorrarArticulo()
        self.ModificarArticulo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana.mainloop()

    def cargarArticulos(self):
        self.frame1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frame1,text="Cargar Articulos")
        self.frame2 = ttk.LabelFrame(self.frame1,text="Articulos",width=50,height=10)
        self.frame2.grid(column=0,row=0,padx=5,pady=10)
        self.descricion = tk.StringVar()
        self.precio = tk.StringVar()
        self.label1 = ttk.Label(self.frame2,text="Descripcion :")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.label2 = ttk.Label(self.frame2, text="Precio :")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry1 = ttk.Entry(self.frame2,textvariable=self.descricion)
        self.entry1.grid(column=2,row=0, padx=5, pady=5)
        self.entry2 = ttk.Entry(self.frame2,textvariable=self.precio)
        self.entry2.grid(column=2, row=1, padx=5, pady=5)
        self.button = ttk.Button(self.frame2,text="Cargar",command=self.Cargar)
        self.button.grid(column=2,row=3, padx=5, pady=5)

    def Cargar(self):
        datos = (self.descricion.get(),self.precio.get())
        self.articulos1.alta(datos)
        mb.showinfo("Mensaje","Los datos fueron Cargados Correctamente")
        self.descricion.set("")
        self.precio.set("")



    def consultarporcodigo(self):
        self.frame3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frame3,text="Consulta Por Codigo")
        self.frame4 = ttk.LabelFrame(self.frame3,text="Articulos")
        self.frame4.grid(column = 0,row=0,padx=5,pady=10)
        self.codigo1=tk.StringVar()
        self.descripcion1 = tk.StringVar()
        self.precio1 = tk.StringVar()
        self.label3 = ttk.Label(self.frame4,text="Codigo :")
        self.label3.grid(column=0,row=0,padx=5,pady=5)
        self.label4 = ttk.Label(self.frame4, text="Descripcion :")
        self.label4.grid(column=0, row=1,padx=5,pady=5)
        self.label5 = ttk.Label(self.frame4, text="Precio :")
        self.label5.grid(column=0, row=2,padx=5,pady=5)
        self.button2 = ttk.Button(self.frame4,text="Consultar",command=self.Consultar)
        self.button2.grid(column=1,row=4,padx=5,pady=5)
        self.entry3 = ttk.Entry(self.frame4,textvariable=self.codigo1)
        self.entry3.grid(column=1,row=0,padx=5,pady=5)
        self.entry4 = ttk.Entry(self.frame4,textvariable=self.descripcion1)
        self.entry4.grid(column=1, row=1, padx=5, pady=5)
        self.entry5 = ttk.Entry(self.frame4,textvariable=self.precio1)
        self.entry5.grid(column=1, row=2, padx=5, pady=5)

    def listado_completo(self):
        self.frame5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frame5,text="Listado Completo")
        self.frame6 = ttk.LabelFrame(self.frame5,text="Articulos")
        self.frame6.grid(column=0,row=0,padx=5,pady=10)

        self.button3 = ttk.Button(self.frame6,text="Listado Completo",command=self.listar)
        self.button3.grid(column=2,row=0)
        self.scrolledtext =st.ScrolledText(self.frame6,width=50,height=10)
        self.scrolledtext.grid(column=0,row=1,padx=10,pady=10)

    def Consultar(self):
        datos = (self.codigo1.get(),)
        respuesta = self.articulos1.consultar(datos)
        if len(respuesta)>0:
            self.descripcion1.set(respuesta[0][0])
            self.precio1.set(respuesta[0][1])
        else:
            self.descripcion1.set('')
            self.precio1.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def Consultar1(self):
        datos = (self.codigo11.get(),)
        respuesta = self.articulos1.consultar(datos)
        if len(respuesta)>0:
            self.descripcion11.set(respuesta[0][0])
            self.precio11.set(respuesta[0][1])
        else:
            self.descripcion11.set('')
            self.precio11.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listar(self):
        respuesta=self.articulos1.recuperar()
        self.scrolledtext.delete("1.0",tk.END)
        for fila in respuesta:
            self.scrolledtext.insert(tk.END, "código:" + str(fila[0]) + "\ndescripción:" + fila[1] + "\nprecio:" + str(
                fila[2]) + "\n\n")

    def BorrarArticulo(self):
        self.frame7 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frame7,text="Borrar Articulos")
        self.frame8= tk.LabelFrame(self.frame7,text="Articulo")
        self.frame8.grid(row=0,column=0)
        self.eliminar=tk.StringVar()

        self.label6 = tk.Label(self.frame8,text="Codigo :")
        self.label6.grid(column=0,row=0,padx =5 ,pady=5)

        self.entry6 = tk.Entry(self.frame8,textvariable=self.eliminar)
        self.entry6.grid(row=0,column=1,padx=5,pady=10)

        self.button4 = tk.Button(self.frame8,text="Eliminar",command=self.Eliminar)
        self.button4.grid(row=2,column=1)

    def ModificarArticulo(self):
        self.frame19=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frame19,text="Modificar Articulo")
        self.frame10 = tk.LabelFrame(self.frame19,text="Articulo")
        self.frame10.grid(row=0,column=0)
        self.codigo11 = tk.StringVar()
        self.descripcion11 = tk.StringVar()
        self.precio11 = tk.StringVar()
        self.label31 = ttk.Label(self.frame10, text="Codigo :")
        self.label31.grid(column=0, row=0, padx=5, pady=5)
        self.label41 = ttk.Label(self.frame10, text="Descripcion :")
        self.label41.grid(column=0, row=1, padx=5, pady=5)
        self.label51 = ttk.Label(self.frame10, text="Precio :")
        self.label51.grid(column=0, row=2, padx=5, pady=5)
        self.button21 = ttk.Button(self.frame10, text="Consultar", command=self.Consultar1)
        self.button21.grid(column=1, row=4, padx=5, pady=5)
        self.entry31 = ttk.Entry(self.frame10, textvariable=self.codigo11)
        self.entry31.grid(column=1, row=0, padx=5, pady=5)
        self.entry41 = ttk.Entry(self.frame10, textvariable=self.descripcion11)
        self.entry41.grid(column=1, row=1, padx=5, pady=5)
        self.entry51 = ttk.Entry(self.frame10, textvariable=self.precio11)
        self.entry51.grid(column=1, row=2, padx=5, pady=5)
        self.button22 = ttk.Button(self.frame10, text="Modificar", command=self.Modificar)
        self.button22.grid(column=1, row=5, padx=5, pady=5)

    def Modificar(self):
        datos = (self.descripcion11.get(), self.precio11.get(),self.codigo11.get())
        self.articulos1.actualizar(datos)
        mb.showinfo("Mensaje", "Los datos fueron Cargados Correctamente")
        self.descricion.set("")
        self.precio.set("")



    def Eliminar(self):
        datos = (self.descripcion11.get(), self.precio11.get(),self.codigo11)
        print(datos)
        respuesta = self.articulos1.actualizar(datos)
        mb.showinfo("Mensaje",f'Se ha eliminado un {respuesta} articulo')










aplicacion = InterfazArticulos()