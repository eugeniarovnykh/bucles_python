# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

x = 0
# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración
max_valor = 6 

# reemplace "condicion" por lo que crea necesario
while x < max_valor:
    if x == 5:
        print('Bucle interrumpido en x=', x)
        break
# Coloque la línea de código para que "x" incremente "1"

    print('Valor x=', x)
    x += 1     

   





# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración
x = 5
max_valor = 0
while x >= max_valor: 
    x -= 1    # reemplace "condicion" por lo que crea necesario
if x < 0:

    print('Bucle interrumpido en x=', x)
   # break
# Coloque la línea de código para que "x" decremente "1"

    print("terminamos!")