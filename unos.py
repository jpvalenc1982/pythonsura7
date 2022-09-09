#Variable con elementos del mismo tipo

#Lista número pares

numerosPares =[]

#Generear un ciclo while que de 10 vueltas

contador = 0

while(contador<10):
    numero=int(input(f'Digite un número par: '))

#se agrega mediante append

    if(numero%2==0):
        numerosPares.append(numero)
        contador+=1

    for observador in numerosPares:
        print(observador)

#print(f'Los números pares son: ')