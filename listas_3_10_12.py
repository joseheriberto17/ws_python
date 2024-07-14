### codigo de prueba para las listas en  python 3.12.4

# seleccione la ejecucion por partes

###listas

#---- append
a = [[1,2,3]]
a[:].append([1,2]) # agregar un item en la ultima lista mas externa
#[[1, 2, 3], [1, 2]]

#---- clear
a = [[1,2,3],[4,5,6]]
a[0].clear() # vaciar la lista
#[[],[4,5,6]]

#---- copy
a = [1,2,3]
b = a[:].copy() # permite hacer copia de los datos de la lista

a[1]="a"

print(a)
print(b)

#---- count 
a = [2,2,2,2,3]
print(a[:].count(2)) # muestra n° item que se repiten con el argumento

#---- extend
a = [[2,2,2,2,3]]
b = [[1,2]]

a[:].extend(b) # agrega un item iterable

print(a)
print(b)
# [[2, 2, 2, 2, 3], 1, 2]
# [1, 2]

#---- index
a = [[1,2],6,7,8,9,10,11]
try:
    # retorna error o posicion del primer objeto dentro de item iterable 
    print(a[:].index(9)) 
except ValueError:
    pass
# 5

#---- insert
a=[[1,2,3],[4,5,6],[7,8,9]]
a.insert(1,["a","b","c"])
# [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]]

#---- pop
a=[[1,2,3],[4,5,6],[7,8,9]]
a.pop(1) #remueve un item en la posicion fija
# [[1, 2, 3], [7, 8, 9]]

#---- remove
a = [[1,2],6,7,8,9,10,11]
try:
    # retorna none o no la lista con un item fijo removido 
    a.remove(6)
except ValueError:
    pass
#[[1, 2], 7, 8, 9, 10, 11]

#---- reserve
a = [[1,2],6,7,8,9,10,11]
a.reverse()# invierte la lista de item
#[11, 10, 9, 8, 7, 6, [1, 2]]

#---- sort
a=[[1,2],[4,5,6,4],[7,8,9]]
# organiza la lista por el tamano de las lista en orden desendente
a.sort(key=len,reverse=True) 
#[[4, 5, 6, 4], [7, 8, 9], [1, 2]]
