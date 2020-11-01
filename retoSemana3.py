"""
Reto de Semana 3, Fundamentos de Programación (Ruta 2)

@author: Juan Sebastián González Rojas
@email: js.gonzalez15@uniandes.edu.co
"""


nombre=input("Ingrese el nombre del usuario: ") #nombre del usuario
listaRestante=input("Ingrese la lista restante, ejemplo: '125121'") #codigos a ser ingresados por teclado
precioNeto=0 #precio sin descuentos a ser obtenido
tipoCliente="" #tipo de cliente a ser obtenido
paqueteServicios="" #paquete de Servicios utilizado
descuento=0 #descuentos a ser obtenidos

aplicaDescuentosPar="10%"+ " descuento" #boolean para aplicar a descuentos
aplicaDescuentosAdicionales=False #boolean para aplicar a descuentos adicionales
descuentoAdicional=""

if listaRestante[0]=="1": #Tipo de cliente inicializado
    tipoCliente="Afiliado"
elif listaRestante[0]=="2":
    tipoCliente="Persona Particular"

edadCliente= int(listaRestante[1]+listaRestante[2]) #Edad numérica del cliente

if listaRestante[3]=="1": #Paquete del servicio utilizado
    paqueteServicios="Deportes"
    precioNeto=500000
elif listaRestante[3]=="2":
    paqueteServicios="Artes y Música"
    precioNeto=870000
elif listaRestante[3]=="3":
    paqueteServicios="Gastronomía"
    precioNeto= 1230000

if int(listaRestante[4])+int(listaRestante[5])%2==0: #Descuento regular
    descuento=0.1
else:
    descuento=0.2
    aplicaDescuentosPar="20%"+ " descuento"

if tipoCliente=="Afiliado" and edadCliente<15:
    descuento=descuento+0.05
    aplicaDescuentosAdicionales=True
    descuentoAdicional="5%"+ " por ser menor de 15 años y ser Afiliado"
if tipoCliente=="Afiliado" and edadCliente>50:
    descuento=descuento+0.25
    aplicaDescuentosAdicionales=True
    descuentoAdicional="25%"+ " por ser mayor de 50 años y ser Afiliado"
if tipoCliente=="Afiliado" and edadCliente<=50 and edadCliente>=15:
    descuentoAdicional=" no tiene descuento adicional porque no es menor a 15 años o mayor de 50 años y ser Afiliado"
if tipoCliente=="Persona Particular" and edadCliente>30:
    descuento=descuento+0.1
    aplicaDescuentosAdicionales=True
    descuentoAdicional="10%"+ " por ser mayor de 30 años y ser Persona Particular"
if tipoCliente=="Persona Particular" and edadCliente<=30:
    descuentoAdicional=" no tiene descuento adicional por ser menor de 30 años y ser Persona Particular"


valorPagar=precioNeto*(1-descuento)

print("Nombre el Cliente: "+nombre)
print("Tipo de Cliente: "+tipoCliente)
print("Edad del Cliente: "+str(edadCliente)+ "años")
print("Servicio Utilizado: "+paqueteServicios)
print("El valor del porcentaje de descuento que tiene el cliente:" +aplicaDescuentosPar)
if aplicaDescuentosAdicionales:
    print("El cliente "+nombre+" aplica para descuentos adicionales:")
    print("El cliente " + nombre+" tiene descuento adicional del " +descuentoAdicional)
else:
    print("El cliente"+nombre+" no aplica para descuentos adicionales:")
    print("El cliente " + nombre+ descuentoAdicional)
print("Valor a pagar $: " +str(valorPagar))