# La sentencia match
# ejemplo 1: math simple 

data = 5
match data:
    case 1:
        print("el valor es 1")
    case 2 | 3 | 4: 
        print("el valor esta entre 2,3 o 4")
    case _: # valor por defecto
        print("el valor es diferente que del 1 al 4")

# ejemplo 2: math simple con cadena de formato       

lista_data = [2,0]

match lista_data:
    case [0,0]:
        print("Origen")
    case [0,y]: # lista de literal con variable
        print(f"eje y = {y},x = '0'") # f"..." cadena con formato  
    case [x,0]:
        print(f"eje y = '0',x = {x}")
    case [x,y]:
        print(f"eje y = {y},x = {x}")

# ejemplo 3: math como una funcion para clases  

class Data_2d:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def match_clase(data_2d):
    match data_2d:
        case Data_2d(x=0,y=0): # acepta como argumentos de la clase definida 'Data_2d'
            print("Origen")
        case Data_2d(x=0,y=y):
            print(f"eje y = {y},x = '0'") # f"..." cadena con formato  
        case Data_2d(x=x,y=0):
            print(f"eje y = '0',x = {x}")
        case Data_2d(x=x,y=y):
            print(f"eje y = {y},x = {x}")

# ejemplo 4: match para una lista de clases con posicionamiento en su argumentos
# analisis: parece que reconoce al menos los 2 primeros elementos de la clase

class Point:
    __match_args__ = ('x', 'y','z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

points = [Point(0,0,5),Point(0,0,7)] # el math se puede efectuar tanto para tupla, lista o diccionarios

match points:
    case []:
        print("No existe")
    case [Point(0, 0),*_]: # solo le interesa el primer item
        print("origen")
    case [Point(x,y,0)] if x == y: # condicion adicional
        print(f"x equal to y")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

# desempaquetado de una lista
a = [1,2,3]
a1,a2,*_ = a

# enumeracion  de una clase
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color('red')

match color:
    case Color.RED:
        print('es color rojo')
    case Color.BLUE:
        print('es color azul')
    case Color.GREEN:
        print('es color verde')

# creacion de funciones
def fib(num):
    ''' sumar el mismo numero anterior '''
    # 0 1 1 2 3 5 8
    a = 0
    b = 1
    while num < b:
        a = a + b
        print(b)
        b = a
