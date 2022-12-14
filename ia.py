from array import array
from random import random
import numpy as np
#....Sección de funciones.......................................
#....Función que captura el numero de individuos de la población
def cap_num_ind():
    t=int(input("Ingrese tamaño de la población: "))
    if (t%2!=0):
        t=t+1
    return t
#....Funcion que computa el tamaño del cromosoma de la especie...
def calc_num_bits(i,j,p):
    t=abs(b-a)
    t=(np.log(t*p)/np.log(2))
    t=round(t)
    t=int(t)
    return(t)
#....función que contruye una matriz (tam_pob x num_bits)........
def crea_matriz(tp,nb):
    t=np.zeros((2*tp,nb+1))
    return t
#....Inicializa la población que va a evolucionar
def inicia_pob(p,r,c):
    for i in range(r):
        for j in range(c):
            p[i][j]=array=np.random.randint(2)
#...Funcion que representa el medio ambiente donde evoluciona la poblacion
def f(t):
    return(t*np.sin(10*np.pi*t)+1.0)
#....Operador de Evaluacuin de aptitud de cada individiduo de la poblacion.........
def op_evaluacion(pob,a,b,pre,tp,nb):
    i=0
    while(i<tp):
        suma=0
        j=0
        while (j<nb):
            suma=suma+pob[i][j]*pob[i][j]*np.power(2,nb-1-j)
            j=j+1
        x=a+suma*np.abs(b-a)/(np.power(2,nb)-1)
        pob[i][nb]=f(x)
        i=i+1
#....ordenamiento................................................
def op_ordenamiento(pob,tp,nb):
    i=0
    while(i<tp):
        j=i+1
        while(j<tp):
            if (pob[i][nb]<pob[j][nb]):
                k=0
                while(k<=nb):
                    t=pob[i][nb]
                    pob[i][nb]=pob[j][nb]
                    pob[j][nb]=t
                    k=k+1
            j=j+1
        i=i+1
#....Operador de seleccion para intercambiar genes entre dos padres
def op_seleccion(pob,tp,nb):
    i=0
    pc=int(nb/2)
    while(i<tp):
        j=i+1
        k=0
        while(k<pc):
            pob[i+tp][k]=pob[i][k]
            pob[i+tp+1][k]=pob[j][k]
            k=k+1
        while(k<nb):
            pob[i+tp][k]=pob[j][k]
            pob[i+tp+1][k]=pob[i][k]
            k=k+1
        i=i+2

#....Mutacion....................................................
def op_mutacion(pob,nb,tp):
    num_mutaciones=int(nb/10)
    num_mutantes=int(tp/10)
    while(i<=num_mutantes):
        j=np.random.randint(tp)
        while(k<=num_mutaciones):
            p=np.random.randint(nb)
            if(pob[j][p]==0):
                pob[j][p]=1
            else:
                pob[j][p]=0
            k=k+1
        i=i+1
#....Sección principal...........................................
num_generaciones=1
tam_pobla=cap_num_ind()
a=float(input("a: "))
b=float(input("b: "))
presicion=float(input("presicion: "))
max_generaciones=int(input("Maximo numero de generaciones: "))
num_bits=calc_num_bits(a,b,presicion)
poblacion=crea_matriz(tam_pobla,num_bits)
inicia_pob(poblacion,tam_pobla,num_bits)
#....Comienza el ciclo evolutivo
while (num_generaciones<=max_generaciones):
    op_evaluacion(poblacion,a,b,presicion,tam_pobla,num_bits)
    op_ordenamiento(poblacion,tam_pobla,num_bits)
    op_seleccion(poblacion,tam_pobla,num_bits)
    num_generaciones=num_generaciones+1

print (poblacion)

#instalar matplot
#Tarea construir el algoritmo que de manera aleatoria selecciones o elija en cada generacion
#una de las 3 formas de formar pareja
#Aleatorio, elitista y vasconselos

#tarea
#Construir un programa en python que simule el automata que esta en el pizarron