#crear menú empanadas

#El que me guarda todo es una lista

i=0
empanadas=[]


print("***EMPANADAS INTELIGENTES***")
print("1. Agregar empanadas")
print("2. Mostrar empanada")
print("3. Salir")

while(i!=3):
    ingredientes=[]
    empanada={}
    i=int(input("Digite una opción del menú: "))
    if(i==1):
        print("Agregando el pedido de empanadas\n")
        empanada['nombre']=input(f'Ingrese el nombre de la empanada: ')
        
        for i in range(3):
            ingredientes.append(input(f'Digite el ingrediente: {i+1}: '))
        
        empanada['ingredientes']=ingredientes
        empanada['precio']=input(f'Ingrese el precio de la empanada: ')
        empanadas.append(empanada)
        
    elif(i==2):
        print("Mostrando empanadas\n")
        print(empanadas)
    elif(i==3):
        break
    else:
        print("Digite una opción correcta: ")