# version de pythno 3.12.3
"""
2. Using the Python Interpreter

puedes usar el python interactivo como para ejecutar una linea
"""

# ejecutamos una linea de python (-c => cadena)

# python -c "print('Hola, mundo')"

# agrega argumentos al script de python (-m => modulo)

# python3 -m mi_modulo [arg1] [arg2] ...
# python3 -m topic_2 'hola'



import sys

print(sys.argv[1])

'''
Comportamiento específico de comando python con argumentos:

- Si ejecutas un script sin proporcionar ningún argumento, sys.argv[0] 
    (el primer elemento de la lista) será una cadena vacía.
- Si el nombre del script es - (lo que significa entrada estándar), sys.argv[0] 
    se establecerá en '-'.
- Si ejecutas Python con la opción -c para ejecutar un comando, sys.argv[0] se 
    establecerá en '-c'.
- Si ejecutas Python con la opción -m para ejecutar un módulo, sys.argv[0] 
    contendrá el nombre completo del módulo.
'''
