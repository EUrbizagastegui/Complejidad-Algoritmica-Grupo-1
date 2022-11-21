from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import sys
from heapq import heapify, heappush
import csv

g = {
        '1':{'2':2,'3':4},
        '2':{'1':2,'3':3,'4':8,'7':6},
        '3':{'1':4,'2':3,'4':2,'5':5,'8':4},
        '4':{'2':8,'3':2,'5':11,'6':22,'9':4},
        '5':{'3':5,'4':11,'6':1,'7':1,'8':3,'9':7},
        '6':{'4':22,'5':1,'7':10,'8':7},
        '7':{'2':6,'5':1,'6':10},
        '8':{'3':4,'5':3,'6':7,'10':4},
        '9':{'4':4,'5':7,'10':6},
        '10':{'8':4,'9':6}
}


    
def new_nodo(grafo,inicio,final,root):
    random.seed(0)
    np.random.seed(0)
    G=nx.DiGraph()

    inf = sys.maxsize
    informacionNodo = {
        '1':{'costo':inf,'pred':[]},
        '2':{'costo':inf,'pred':[]},
        '3':{'costo':inf,'pred':[]},
        '4':{'costo':inf,'pred':[]},
        '5':{'costo':inf,'pred':[]},
        '6':{'costo':inf,'pred':[]},
        '7':{'costo':inf,'pred':[]},
        '8':{'costo':inf,'pred':[]},
        '9':{'costo':inf,'pred':[]},
        '10':{'costo':inf,'pred':[]}
    }

    informacionNodo[inicio]['costo'] = 0
    visitado = []
    aux = inicio
    for i in range(len(grafo)-1):
        if aux not in visitado:
            visitado.append(aux)
            min_heap = []
            for j in grafo[aux]:
                if j not in visitado:
                    costo = informacionNodo[aux]['costo'] + grafo[aux][j]
                    if costo < informacionNodo[j]['costo']:
                        informacionNodo[j]['costo'] = costo
                        informacionNodo[j]['pred'] = informacionNodo[aux]['pred'] + [aux]
                    heappush(min_heap,(informacionNodo[j]['costo'],j))
        heapify(min_heap)
        aux = min_heap[0][1]

    for element in range(len(informacionNodo[final]['pred'])):
      if element != len(informacionNodo[final]['pred']) - 1:
        G.add_edge(str(informacionNodo[final]['pred'][element]),str(informacionNodo[final]['pred'][element+1]))
      else:
        G.add_edge(str(informacionNodo[final]['pred'][element]),str(final))
    peso=str(informacionNodo[final]['costo'])
    lblpeso = Label(root, text=peso, bg="#E5E5E5")
    lblpeso.place(relx=0.76,rely=0.25)
    
    linea=""

    for element in range(len(informacionNodo[final]['pred'])):
      if element != len(informacionNodo[final]['pred']) - 1:
        linea+=str(informacionNodo[final]['pred'][element])+" -> "+str(informacionNodo[final]['pred'][element+1])+" ; "
      else:
        linea+=str(informacionNodo[final]['pred'][element])+" -> "+str(final)

    lbl2w_3 = Label(root, text=linea,bg="#E5E5E5")
    lbl2w_3.place(relx=0.1,rely=0.44)
    
    nx.draw(G,with_labels=True,node_color="red",node_size=1000,font_color="white",font_size=20,font_family="Times New Roman",font_weight="bold")
    plt.margins(0.2)
    plt.show()
        
        
def mostrar_nodo(grafo,inicio,final,root):
    random.seed(0)
    np.random.seed(0)
    G=nx.DiGraph()

    inf = sys.maxsize
    informacionNodo = {
        '1':{'costo':inf,'pred':[]},
        '2':{'costo':inf,'pred':[]},
        '3':{'costo':inf,'pred':[]},
        '4':{'costo':inf,'pred':[]},
        '5':{'costo':inf,'pred':[]},
        '6':{'costo':inf,'pred':[]},
        '7':{'costo':inf,'pred':[]},
        '8':{'costo':inf,'pred':[]},
        '9':{'costo':inf,'pred':[]},
        '10':{'costo':inf,'pred':[]}
    }

    informacionNodo[inicio]['costo'] = 0
    visitado = []
    aux = inicio
    for i in range(len(grafo)-1):
        if aux not in visitado:
            visitado.append(aux)
            min_heap = []
            for j in grafo[aux]:
                if j not in visitado:
                    costo = informacionNodo[aux]['costo'] + grafo[aux][j]
                    if costo < informacionNodo[j]['costo']:
                        informacionNodo[j]['costo'] = costo
                        informacionNodo[j]['pred'] = informacionNodo[aux]['pred'] + [aux]
                    heappush(min_heap,(informacionNodo[j]['costo'],j))
        heapify(min_heap)
        aux = min_heap[0][1]    
    for element in range(len(informacionNodo[final]['pred'])):
      if element != len(informacionNodo[final]['pred']) - 1:
        G.add_edge(str(informacionNodo[final]['pred'][element]),str(informacionNodo[final]['pred'][element+1]))
      else:
        G.add_edge(str(informacionNodo[final]['pred'][element]),str(final))
    peso=str(informacionNodo[final]['costo'])
    lblpesoTraf = Label(root, text=peso, bg="#E5E5E5")
    lblpesoTraf.place(relx=0.76,rely=0.11)
    
    linea=""

    for element in range(len(informacionNodo[final]['pred'])):
      if element != len(informacionNodo[final]['pred']) - 1:
        linea+=str(informacionNodo[final]['pred'][element])+" -> "+str(informacionNodo[final]['pred'][element+1])+" ; "
      else:
        linea+=str(informacionNodo[final]['pred'][element])+" -> "+str(final)

    lbl2w_3 = Label(root, text=linea,bg="#E5E5E5")
    lbl2w_3.place(relx=0.1,rely=0.35)
            
    nx.draw(G,with_labels=True,node_color="red",node_size=1000,font_color="white",font_size=20,font_family="Times New Roman",font_weight="bold")
    plt.margins(0.2)
    plt.show()
    g2=cambiarDiccionario(g)
    new_nodo(g2,inicio,final,root)
    
    
        
    
        
    
    
    
def cambiarDiccionario(diccionario):
  llaves=dict.keys(diccionario)
  
  for llave in llaves:
    llaves2=list(dict.keys(diccionario[llave]))
    for i in range(len(diccionario[llave])-1):
        diccionario[llave][llaves2[i-1]]=random.randint(1,10)

  return diccionario
#g2=cambiarDiccionario(g)
#def imprevistos(g,inicio,final):
    #mostrar_nodo(g2,inicio,final)
#Funcion del botón para abrir la segunda ventana
def mostrarRestaurantes():
    ventanaRES=Tk()
    ventanaRES.geometry("600x300")
    lblres1=Label(ventanaRES,text="1) El Fogón Del Asador Parrillas & Cocina Rústica - MAGDALENA en Av. Brasil 3781",bg="#E5E5E5").pack()
    lblres2=Label(ventanaRES,text="2) El Barquero Restaurante en Jr. Tacna 885",bg="#E5E5E5").pack()
    lblres3=Label(ventanaRES,text="3) Los Esteros De Tumbes en Jr. Tacna 896",bg="#E5E5E5").pack()
    lblres4=Label(ventanaRES,text="4) La Antojería Juan de Aliaga en Av. Juan de Aliaga 401",bg="#E5E5E5").pack()
    lblres5=Label(ventanaRES,text="5) Mar de Mares en Jirón San Martin 503",bg="#E5E5E5").pack()
    lblres6=Label(ventanaRES,text="6) Elia en Jirón Daniel Carrión 299",bg="#E5E5E5").pack()
    lblres7=Label(ventanaRES,text="7) La casita del chef en Jr. Bolognesi 156",bg="#E5E5E5").pack()
    lblres8=Label(ventanaRES,text="8) Travesura Marina - Barra Cevichera en Mercado de Magdalena Puestos 12, 62 y 63",bg="#E5E5E5").pack()
    lblres9=Label(ventanaRES,text="9) El Pulpito en Jr.Leoncio Prado 811",bg="#E5E5E5").pack()
    lblres10=Label(ventanaRES,text="10) Las Vegas en Jr. Bolognesi 295",bg="#E5E5E5").pack()
    

def segundaVentana ():
    
    #Nueva ventana
    ventana2 = Tk()
    varini = StringVar()
    varfin = StringVar()    
    ventana2.title("RuTop")
    ventana2.iconbitmap("ping.ico")
    ventana2.config(background='#9CDCE8')
    ventana2.geometry("800x600")
    lbl2w_0= Label(ventana2, text="Ingresar punto incial")
    lbl2w_0.place(relx=0.07,rely=0.05)
    
    write2w_0=Entry(ventana2,width=20,borderwidth=2, textvariable=varini)#INGRESO
    write2w_0.place(relx=0.3,rely=0.055)
    
    lbl2w_1 = Label(ventana2, text="Ingresar punto final")
    lbl2w_1.place(relx=0.07,rely=0.15)
    
    write2w_1 = Entry(ventana2, width=20, borderwidth=2, textvariable=varfin)#FINAL
    write2w_1.place(relx=0.3,rely=0.15)
    
        
    lbl2w_2 = Label(ventana2, text="El mejor camino a tomar: ", bg="#E5E5E5")
    lbl2w_2.place(relx=0.09,rely=0.3)
    lbl2w_6 = Label(ventana2, text="El mejor camino a tomar con imprevistos presentados: ", bg="#E5E5E5")
    lbl2w_6.place(relx=0.05,rely=0.4)
    
    
    
    lbl2w_4 = Label(ventana2, text="Peso total recorrido sin imprevistos", bg="#E5E5E5")
    lbl2w_4.place(relx=0.65,rely=0.05)
    
    lbl2w_5 = Label(ventana2, text="Peso total recorrido con imprevistos", bg="#E5E5E5")
    lbl2w_5.place(relx=0.65,rely=0.17)
    
    
    btn2w_1=Button(ventana2,text="Mostrar Recorrido",bg="#71A7A2",command=lambda:mostrar_nodo(g,write2w_0.get(),write2w_1.get(),ventana2))
    btn2w_1.place(relx=0.23,rely=0.22)
        
    btnres=Button(ventana2,text="Mostrar Restaurantes",command=mostrarRestaurantes,bg="#71A7A2")
    btnres.place(relx=0.69,rely=0.4)