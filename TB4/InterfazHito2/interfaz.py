#Antes, descargar las librerias "Tkinter" y "pillow".
from tkinter import *
from PIL import ImageTk, Image
from SecondWindow import segundaVentana

framelist = []
frame_index = 0
resize_img = []
count = 0
#Llamado a la funcion de la ventana
ventana = Tk()

#Titulo de la ventana
ventana.title("RuTop")

#Background
ventana.config(background='#9CDCE8')

#Cambiar el icono del programa
ventana.iconbitmap("ping.ico")

#Size de la ventana
ventana.geometry("400x400")

#Implementación de la imágen
image=Image.open("mundomaps.gif")
frames=image.n_frames
imageObject=[PhotoImage(file="mundomaps.gif", format = f"gif -index {i}") for i in range(frames)]
showAnimation = None
def animation(count):
    global showAnimation
    newImage=imageObject[count]
    gif_Label.configure(image=newImage)
    count += 1
    if count == frames:
        count = 0
    showAnimation = ventana.after(20 , lambda: animation(count))
gif_Label=Label(ventana,image="")
gif_Label.place(relx=0.19,rely=0.1, width=250,height=250)

#TITULO
lbl1=Label(ventana , text="Bienvenido a RuTop",bg="#1C71B8", font='bold')
lbl1.place(relx=0.17,rely=0.01,width=270,height=30)

#Implementacion de botones
btn1=Button(ventana,text="Comenzar",command=segundaVentana,bg="#71A7A2")

btn2=Button(ventana,text="Salir de la App",command=ventana.quit,bg="#71A7A2")
btn1.place(relx=0.4,rely=0.76)
btn2.place(relx=0.376,rely=0.85)

animation(count)
ventana.mainloop()