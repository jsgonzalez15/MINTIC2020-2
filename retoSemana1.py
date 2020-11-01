import numpy as np

cantidadVentas=np.array([20,23,15,32,31,8]) #arreglo de cantidades vendidas por dia
precioUnidad=np.array([3500,3400,3800,3200,3100,4000]) #arreglo de precios por dia
porcentajeUtilidad=0.1 #porcentaje estimado de ganancia

dineroRecaudado=np.dot(cantidadVentas,precioUnidad) #producto punto (suma de cantidades vendidas por precios respectivos)
gananciasPorDia=np.multiply(cantidadVentas,precioUnidad)*porcentajeUtilidad #arreglo producto element-wise (cantidad por precio)
gananciasTotales=np.sum(gananciasPorDia) #ganancias totales como suma de ganancias por dia

sumaCantidadVentas=np.sum(cantidadVentas) #suma de cantidades para cantidad total

print("Cantidad total de productos vendidos: "+str(sumaCantidadVentas))
print("Dinero total recaudado: " + str(dineroRecaudado))
print("Ganancias totales de producto nuevo: "+ str(gananciasTotales))
print("Las ganancias totales por día con su respectiva cantidad se ilustran a continuación: ")

print("Lunes: cant(" +str(cantidadVentas[0])+") ganancias("+str(gananciasPorDia[0])+")")
print("Martes: cant(" +str(cantidadVentas[1])+") ganancias("+str(gananciasPorDia[1])+")")
print("Miércoles: cant(" +str(cantidadVentas[2])+") ganancias("+str(gananciasPorDia[2])+")")
print("Jueves: cant(" +str(cantidadVentas[3])+") ganancias("+str(gananciasPorDia[3])+")")
print("Viernes: cant(" +str(cantidadVentas[4])+") ganancias("+str(gananciasPorDia[4])+")")
print("Sábadp: cant(" +str(cantidadVentas[5])+") ganancias("+str(gananciasPorDia[5])+")")

