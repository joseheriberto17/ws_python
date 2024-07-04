# 3. An Informal Introduction to Python

# Calculadora

# division: /
# division entera: //
# resto: %
# potencia: **

# ejemplo para usar un ans en python 
# a = 1
# a
# 1 (salida)
# 5 + _ (ans) (no se puede asignar a una variable , solo lectura)
# b
# 6

# texto

s = 'First line.\nSecond line.'  # \n means newline

print(s)  # con print(), interpreta los caracteres especiales, \n produce una nueva linea

print(r'C:\some\name')  # la r ante de la cadena genera una cadena sin formato no interpreta \n

# texto multilinea (\ evita incluir una linea en blanco)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print('frase unida, ('+ 3*'na' +') 3 veces')

print('cadenas '
      'concatenadas')

variable_srt = "variables "

print(variable_srt + 'concatenadas')

# indexacion de cadenas

word = 'pythonista'

print('index: 5 de pythonista es '+ word[5])
print('index: 0 al (5-1) de pythonista es '+ word[0:5]) # rebanadas (slicing)
print('index: -3 de pythonista es '+ word[-3])
print('completa es: '+ word[:4] + word[4:])

#word[0] = 'J' (no se puede la cadena es inmutable)

word_2 = 'J' + word[1:]
print(word_2)  # nueva cadena

len(word) # longitud del caracter

# listas

datos = [1,2,3,4,5] # datos son mutables (cambiar su contenido), se puede indexar, concatenar con variables mismas.
print('longitud de lista datos es: ' + str(len(datos))) # longitud de listas.

datos.append(2*3)
print('nuevo dato es: '+ str(datos[-1]))

datos_2 = datos # no copia la variable sino la referencia de la varible ,si una cambia todas cambia
datos_3 = datos_2[:] # esto si copia solamente (shallow copy)
datos_2.append(7)

print('datos_2: '+ str(datos_2[-1]))
print('datos_3: '+ str(datos_3[-1]))

# la index puede vaciar una lista o reemplazar

#tambien se puede concatenar una lista dentro de otra lista

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n] #x[0] => '['a', 'b', 'c']' | x[0][1] => '['b']'

