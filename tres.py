#El que me guarda todo es una lista
#crear un menu de dos opciones

i=0
empanadas=[]
#MENÚ DE OPCIONES

print("***ENAMÓRATE DE ANTIOQUIA***")
print("1. Agregar pueblo")
print("2. Mostrar ruta")
print("3. Salir")
pueblos=[]
while(i!=3):
    pueblo={}
    i=int(input("Digite una opción del menú: "))
    if(i==1):
        print("Agregando pueblo")
        pueblo['nombre']=input(f'Ingrese el nombre del pueblo: ')
        pueblo['distancia']=input(f'Ingrese la distancia al pueblo: ')
        pueblo['poblacion']=input(f'Ingrese la cantidad de habitantes del pueblo: ')
        pueblos.append(pueblo)
    elif(i==2):
        print("Mostrando ruta")
        print(pueblos)
    elif(i==3):
        break
    else:
        print("Digite una opción válida")
print("Gracias")