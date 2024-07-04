# 4. More Control Flow Tools

#sentencia if

number = int(input("digite un numero entero: "))

if number < 0:
    print('el numero: '+str(number)+' es negativo')
elif number == 0:
    print('el numero es igual a cero')
elif number == 1:
    print('el numero es igual a uno')
else:
    print('el numero es mayor a uno')

# sentencia for 

number_list = [7,5,4,1,7,5,6,7,7]
number_list_2 = []
for i in number_list:
    if i != 7:
        number_list_2.append(i)
        print(i)
        

# uso de range() 
for i in range(5): # iterar un print de 0 al 4
    print(i)

number_data = list(range(0,10+1,2)) # el numero desde 0 hasta n+1

for i in range(len(number_data)):
    print(number_data[i])

# Las sentencias break, continue, y else en bucles

for i in range(0,4):
    if i == 7:
        break
else: 
    print("no paso por un 7") # se ejecuta si el break no se a utilizado en el for o while

for i in range(11):
    if i == 3:
        continue # obliga al bucle que pase a la siguiente iteracion sin que se ejecute el resto de codigo
    print(i)

# uso de pass
'''
while True:
    pass

class MyEmptyClass:
    pass

def prueba(*args):
    pass
'''



