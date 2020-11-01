"""
Refuerzo de Semana 3, Fundamentos de Programación (Ruta 2)

@author: Juan Sebastián González Rojas
@email: js.gonzalez15@uniandes.edu.co
"""
import numpy as np

#Declaración de listas como arreglos de valores aleatorios entre 0 y 10
lista1=np.random.rand(20)*10
lista2=np.random.rand(20)*10
lista3=np.random.rand(20)*10
lista4=np.random.rand(20)*10
lista5=np.random.rand(20)*10

print("Las listas a obtener sus promedios son:")
print("Lista 1:")
print(lista1)
print("Lista 2:")
print(lista2)
print("Lista 3:")
print(lista3)
print("Lista 4:")
print(lista4)
print("Lista 5:")
print(lista5)

#arreglo de promedios para todas las listas (puede obtenerse el resultado con la funcion np.max pero lo implemento con condicionales)
promedioVentanaAzul= np.array([np.mean(lista1[0:5]),np.mean(lista2[0:5]),np.mean(lista3[0:5]),np.mean(lista4[0:5]),np.mean(lista5[0:5])])
promedioVentanaVerde= np.array([np.mean(lista1[5:10]),np.mean(lista2[5:10]),np.mean(lista3[5:10]),np.mean(lista4[5:10]),np.mean(lista5[5:10])])
promedioVentanaNaranja= np.array([np.mean(lista1[10:15]),np.mean(lista2[10:15]),np.mean(lista3[10:15]),np.mean(lista4[10:15]),np.mean(lista5[10:15])])
promedioVentanaGris= np.array([np.mean(lista1[15:20]),np.mean(lista2[15:20]),np.mean(lista3[15:20]),np.mean(lista4[15:20]),np.mean(lista5[15:20])])

print("Los promedios por ventana son:")
print("Promedios Azul:")
print(promedioVentanaAzul)
print("Promedios Verde:")
print(promedioVentanaVerde)
print("Promedio Naranja:")
print(promedioVentanaNaranja)
print("Promedio Gris:")
print(promedioVentanaGris)


#valores referencia
maxAzulRef=np.ndarray.max(promedioVentanaAzul)
maxVerdeRef=np.ndarray.max(promedioVentanaVerde)
maxNaranjaRef=np.ndarray.max(promedioVentanaNaranja)
maxGrisRef=np.ndarray.max(promedioVentanaGris)

#valores obtenidos por condicionales
maxAzul=0
for azul in range(len(promedioVentanaAzul)):
    if(promedioVentanaAzul[azul] >maxAzul):
        maxAzul=promedioVentanaAzul[azul]
maxVerde=0
for verde in range(len(promedioVentanaVerde)):
    if(promedioVentanaVerde[verde] >maxVerde):
        maxVerde=promedioVentanaVerde[verde]
maxNaranja=0
for naranja in range(len(promedioVentanaNaranja)):
    if(promedioVentanaNaranja[naranja] >maxNaranja):
        maxNaranja=promedioVentanaNaranja[naranja]
maxGris=0
for gris in range(len(promedioVentanaGris)):
    if(promedioVentanaGris[gris] >maxGris):
        maxGris=promedioVentanaGris[gris]

print("El máximo del promedio de ventana azul es igual a: "+str(maxAzul)+" referencia:" +str(maxAzulRef))
print("El máximo del promedio de ventana verde es igual a: "+str(maxVerde)+" referencia:" +str(maxVerdeRef))
print("El máximo del promedio de ventana naranja es igual a: "+str(maxNaranja)+" referencia:" +str(maxNaranjaRef))
print("El máximo del promedio de ventana gris es igual a: "+str(maxGris)+" referencia:" +str(maxGrisRef))