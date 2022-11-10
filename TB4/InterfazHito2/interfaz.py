#Antes, descargar las librerias "Tkinter" y "pillow".
from tkinter import *
from PIL import ImageTk, Image

#Llamado a la funcion de la ventana
ventana = Tk();

#Titulo de la ventana
ventana.title("Grafo de Restaurantes");

#Cambiar el icono del programa
ventana.iconbitmap("")

#Size de la ventana
ventana.geometry("400x400");

#Primer texto
lbl1=Label(ventana , text="Bienvenido al grafo de Restaurantes",bg="green");
lbl1.place(relx=0.14,rely=0.05,width=300,height=30);

#Implementacion de Imagen
image=Image.open("Imagenes/maps.png") #Asignacion de la foto a la variable image
image=image.resize((200,200), Image.ANTIALIAS);
nodoimg = ImageTk.PhotoImage(image);

lbl_img = Label(ventana,image=nodoimg);
lbl_img.place(relx=0.22,rely=0.15)

#Funcion del botón para abrir la segunda ventana

def segundaVentana ():
    #Intento de nueva ventana

    ventana.destroy();
    ventana2=Tk();
    ventana2.title("Ventana de funcionamiento");
    ventana2.geometry("800x600");
    lbl2w_0= Label(ventana2, text="Ingresar punto incial").pack();
    write2w_0=Entry(ventana2,width=20,borderwidth=2).pack();
    lbl2w_1 = Label(ventana2, text="Ingresar punto final").pack();
    write2w_1 = Entry(ventana2, width=20, borderwidth=2).pack();
    btn2w_0=Button(ventana2,text="Buscar").pack();
    lbl2w_2 = Label(ventana2, text="El mejor camino a tomar es el siguiente: ", bg="#E5E5E5").pack();
    lbl2w_3 = Label(ventana2, text="A->B, B->C, C->D",bg="#E5E5E5").pack();
    lbl2w_4 = Label(ventana2, text="Peso total recorrido:", bg="#E5E5E5").pack();
    lbl2w_5 = Label(ventana2, text="           25            ", bg="#E5E5E5").pack();
    lbl2w_5 = Label(ventana2, text="                         ").pack();
    lbl2w_5 = Label(ventana2, text="                         ").pack();
    lbl2w_6 = Label(ventana2, text="◘Imagen Referencial.jpg").pack()


#Implementacion de botones
btn1=Button(ventana,text="Comenzar",command=segundaVentana);
btn2=Button(ventana,text="Salir de la App",command=ventana.quit);


btn1.place(relx=0.4,rely=0.68);
btn2.place(relx=0.37,rely=0.76);

ventana.mainloop();