"""
Reto de Semana 2, Fundamentos de Programación (Ruta 2)

@author: Juan Sebastián González Rojas
@email: js.gonzalez15@uniandes.edu.co
"""
import numpy as np

salMin=877802 #Salario Mínimo
nominaTotalPamplona=0 #Gastos totales en nomina Universidad de Pamplona
p=["Nombre","Edad","Escolaridad","Genero","Ingreso"] #Formato de lista

#Informacion con salario a ser actualizado
p1=["Juan Ortiz",34,2,"M",0]
p2=["Oscar Cajigas",44,2,"M",0]
p3=["Carlos Rojas",32,3,"M",0]
p4=["Daniel Gonzalez",28,1,"M",0]
p5=["Sofia Arellano",46,3,"F",0]
p6=["Zara Amortegui",51,4,"F",0]
p7=["Hellen Avila",28,2,"F",0]
p8=["Chimuelo Guevara",40,2,"M",0]
p9=["Esteban Aristizabal",28,4,"M",0]
p10=["Dominic Dominguez",25,2,"M",0]
p11=["Jorge Colunge",60,4,"M",0]
p12=["Flor Serna",65,4,"F",0]
p13=["Maria Fuentes",29,4,"F",0]
p14=["Dario Ruiz",35,3,"M",0]
p15=["Ariana Torres",55,4,"F",0]

trabajadoresPamplona=np.array([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]) #Matriz con informacion de trabajadores
porcentajeSalarios=[] #Lista de porcentajes de Salarios
nombresTrabajadores=[] #Lista de nombres
ingresosTrabajadores=[] #Lista de ingresos de empleados
edadTrabajadores=[] #Lista de edades de los trabajadores
#print(trabajadoresPamplona)

for p in trabajadoresPamplona:
    p[4]=int(p[2])*salMin #actualizacion de salario
    nominaTotalPamplona+=int(p[4])
    porcentajeSalarios.append(int(p[4])) #inicializacion con salario 
    nombresTrabajadores.append(p[0])
    edadTrabajadores.append(int(p[1]))

ingresosTrabajadores=porcentajeSalarios #Ingresos de cada empleado    
porcentajeSalarios=np.array(porcentajeSalarios)/nominaTotalPamplona #Porcentaje SalarioIndividual/NominaTotal
nombresTrabajadores.sort()
ingresosTrabajadores.sort()
edadTrabajadores.sort()
sueldoMax=ingresosTrabajadores[-1]
sueldoMin=ingresosTrabajadores[0]
edadMax=edadTrabajadores[-1]
edadMin=edadTrabajadores[0]

print("Los nombres de los trabajadores en orden alfabético son:")
print(nombresTrabajadores)
print("Los ingresos organizados en orden ascendente son:")
print(ingresosTrabajadores)
print("Los ingresos máximo y mínimo para los Trabajadores de la Universidad de Pamplona son respectivamente: COP" +str(sueldoMax)+" y COP"+str(sueldoMin))
print("Las edades máxima y mínima de los Trabajadores de la Universidad de Pamplona actualmente es: " +str(edadMax)+" años y "+str(edadMin)+" años")