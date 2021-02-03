# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # incializacion y declaracion de numeros (int, float..)
    numero = 10.56
    print_hi('PyCharm')
    # mostrar variables
    print(numero)
    # saber que tipo de dato es la variable creada
    print(type(numero))

    # inicializacion y declaracion de cadenas (string...)
    cadena = 'cadena de texto'
    print(cadena)
    print(type(cadena))

    # inicializacion y declaracion de booleanos
    valor = True  # debe ser siempre con mayusculas
    print(valor)
    print(type(valor))

    # operaciones aritmeticas
    v1 = 13
    v2 = 10
    suma = v1 + v2
    print(suma)

    resultado = v1 * (v1 + v2) - v2
    print('El resultado es', resultado)

    # tipado dinamico
    value = 10
    print(value)
    value = 'Valor Cambiado'
    print(value)

    # operadores aritmeticos (+,/,//,%, **)
    # el // permite dividir y redondear a la baja
    print(v1 / v2)
    print(v1 // v2)
    # modulo, retorna el resto
    print(v1 % v2)
    # exponentes
    v1 = 2
    v2 = 5
    print(v1 ** v2)

    # operadores relacionales (<,>,==,!=)
    print(v1 == v2)
    v1 = 10
    v2 = 10
    print(v1 == v2)
    v3 = 20
    print(v1 + v2 != v3)  # devuleve siempre booleanos

    # operadores logicos (and, or, not)
    print((v1 < v2) and (v2 < v3))
    v2 = 15
    print((v1 == v2) or (v2 < v3))  # basta con uno se cumpla para que sean los dos verdaderos
    print(not (v1 == v2))

    # operadores de asignacion -> para acortar el codigo
    v1 = 9
    v1 += 1  # suma en asignacion
    v2 *= 3  # division en asignacion
    v2 **= 4  # potencia en asignacion
    v2 %= 5  # modulo de asignacion
    print(v1)
    print(v2)

    # Salida de datos
    cadena1 = 'Miguel'
    cadena2 = 'Fran'
    # 3 formas (normal, format, f)
    print('Hola', cadena2, 'soy', cadena1)
    print('Hola {} soy {}'.format(cadena2, cadena1))
    print(f'Hola {cadena2} soy {cadena1}')

    # entrada de datos
    mi_nombre = input('Digite su nombre completo...')
    print_hi(mi_nombre)

    mi_number = float(input('Digite su numero coma flotante...'))
    print('f tu numero era ...', {mi_number + 1.20})

    # casting en python y funciones integradas
    mi_number = hex(34)
    print(mi_number)

    mi_number = bin(34)
    print(mi_number)

    mi_number = round(5.6)  # redondea al numero mas cercano
    print(mi_number)

    mi_number = len(mi_nombre)  # cuenta los caracteres que conforman el objeto
    print(mi_nombre)
    
     # Ejercicio 1 : Resolucion de operacion aritmrtica
    input_a = float(input('Digite el valor para almacenar en a...'))
    print(f'el valor almacenado en a es: ', {input_a})

    input_b = float(input('Digite el valor para almacenar en b...'))
    print(f' el valor almacenado en b es: ', {input_b})

    input_c = float(input('Digite el valor para almacenar en c...'))
    print(f'el valor almacenado en c es: ', {input_c})

    resultado = (input_a ** 3 * (input_b ** 2 - 2 * input_a * input_c)) / 2 * input_b
    print(f'el resultado es...', {round(resultado)})

    # Ejercicio 2 : Resolucion de operacion logica
    resultado_1 = (3 + 5 * 8)
    resultado_2 = ((-6 / 3 * 4) + 2)
    input_a = input('Digite el valor para almacenar en a...')
    input_b = input('Digite el valor para almacenar en b...')

    print((resultado_1 < 3) and (resultado_2 < 2) or (input_a > input_b))

    # Ejercicio 3 : Hacer un programa para intercambiar variables
    input_a = input('Digite el valor para almacenar en a...')
    print(f'El valor es...', {input_a})
    input_b = input('Digite el valor para almacenar en b...')
    print(f'El valor es...', {input_b})

    input_a, input_b = input_b, input_a
    print(f'El nuevo valor de a es...', {input_a})
    print(f'El nuevo valor de b es...', {input_b})

    # Ejercicio 4 : Programa para calcular el área y la longitud de una circunferencia dado el radio
    radio = float(input('Digite el radio de la circunferencia...'))
    import math
    area = math.pi*radio**2
    longitud = 2*math.pi*radio
    print(f'El area es...', {round(area)})
    print(f'La longitud es...', {round(longitud)})

    # Ejercicio 5 : Calcular porcentajes (descuentos...)
    price = float(input('Digite el precio del producto...'))
    descuento = (price*15)/100
    price_final = price - descuento
    print(f'El precio final a pagar es de ',{round(price_final)},'$')

    # Condicionales
    if price_final<12:
        print(f'El ', {round(price_final)}, ' es menor que 12')
    elif price_final ==12:
        print(f'El ', {round(price_final)}, ' es 12, ni menor ni mayor que el')
    else:
        print(f'El ', {round(price_final)}, ' es mayor que 12')
       
    # Condicionales Anidados (garantia antes excepciones)
    edad = int(input('Digite su edad...'))
    if 0 >= edad >= 100:
        print('Edad incorrecta')
    else:
        print('Edad correcta')
        if edad >= 18:
            print('Eres mayor de edad')
        else:
            print('No eres mayor de edad')

    # Ejericio 6 : Pares, impares o los dos

    mi_number1 = int(input('Digite un numero entero...'))
    mi_number2 = int(input('Digite un numero entero...'))

    if mi_number1 % 2 == 0 and mi_number2 % 2 == 0:
        print('Los dos numeros son pares.')
    else:
        if mi_number1 % 2 == 0:
            print('Solo el primer numero es par')
        else:
            print('Solo el segundo numero es par')

    # Ejercicio 7 : cual es mayor de 3 numeros

    mi_number1 = int(input('Digite el primer numero...'))
    mi_number2 = int(input('Digite el primer numero...'))
    mi_number3 = int(input('Digite el primer numero...'))

    if mi_number1 >= mi_number2 and mi_number1 >= mi_number3:
        print(f'El numero mayor es {mi_number1}')
    if mi_number2 >= mi_number1 and mi_number2 >= mi_number3:
        print(f'El numero mayor es {mi_number2}')
    if mi_number3 >= mi_number1 and mi_number3 >= mi_number2:
        print(f'El numero mayor es {mi_number3}')

    # Ejercicio 8 : calibrar caracteres

    letra = input('Digite el caracter:').lower()
    # el metodo lower hace que el caracter lo transforme a minuscula y lo guarda dentro de letra

    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('Es vocal')
    else:
        print('No es vocal')

    # Ejercicio 9 : Calculadora

    mi_number1 = int(input('Digite un entero...'))
    mi_number2 = int(input('Digite el segundo...'))

    operacion = input('Digite la operacion...').upper()

    if operacion == 'S':
        print('\nLa suma es ...', mi_number1 + mi_number2)
    if operacion == 'R':
        print('\nla resta es...', mi_number1 - mi_number2)

    # Ejercicio 10 : operaciones en un cajero

    saldo = 1000
    print('\t.:MENU:.')
    print('1. Ingresar dinero')
    print('2. Retirar dinero')
    print('3. Mostrar cartera')
    print('4. Salir')
    opcion = int(input('Digite una opcion de menu...'))
    print('\n')

    if opcion == 1:
        extra = float(input('Digite dinero a ingresar...'))
        saldo += extra
        print(f'la cuenta ahora tiene ...{saldo}$')
    elif opcion == 2:
        retiro = float(input('Digite dinero a retirar...'))
        if retiro > saldo:
            print('No tiene tal cantidad')
        else:
            saldo -= retiro
            print(f'la cuenta ahora tiene ...{saldo}$')
    elif opcion == 3:
        print(f'la cuenta ahora tiene ...{saldo}$')
    elif opcion == 4:
        print('Saliste...')
    else:
        print('Opcion incorrecta')
       
    # Uso de listas (arrays en Java)
    lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 5.60]
    print(lista)
    print(lista[0])  # lunes
    print(lista[0:3])  # Lunes, martes y miercoles
    print(lista[5])  # 5.60

    lista.append(34)  # se añade al final de la lista el valor introducido
    lista.insert(2, 'Saludos')  # (indice, valor)
    lista.extend([56, 78, 90])  # añade una lista a la otra creada dentro del ()

    print(lista)
    print('Martes' in lista)  # permite saber si un dato esta en la lista (devuelve un booleano)
    print(lista.index('Martes'))  # devuelve la posicion/indice donde se encuentra
    lista.append(34)
    print(lista.count(34))  # permite saber las veces que aparece un determinado valor en la lista

    lista.pop()  # elimina el ultimo elemento
    print(lista)
    lista.pop(2)  # elimina el elemento en la posicion
    print(lista)
    lista.remove('Martes')  # elimina el elemento donde este
    print(lista)
    # lista.clear(), elimina todos los elementos de la lista quedando vacia
    # lista.sort(), ordena los elemntos
    # lista.sort(reverse = True), ordena los elementos de mayor a menor

    # Tuplas = listas inmutables (no se pueden modificar)
    tupla = ('Miguel', 5, 67.89)
    mi_lista = list(tupla)
    print(mi_lista)

    # Conjuntos

    mi_conjunto = set()
    mi_conjunto = {1.0, 2.0, 3.0}
    mi_conjunto.add(4.0)  # lo añade donde quiere
    mi_conjunto.add('Adios')
    mi_conjunto.add(6)
    print(mi_conjunto)

    mi_conjunto.discard('Adios')
    print(mi_conjunto)
    print(3 not in mi_conjunto)
    print(1.0 in mi_conjunto)

    a = {1, 2, 3, 4}
    b = {5, 6, 7, 8, 3}

    print(a == b)  # da igual el orden, si tiene los mismos elementos devuelve True
    print(len(a))  # saber cuantos elemento tiene un conjunto

    # operaciones de conjuntos
    print(a | b)  # union (Solo salen los elementos una vez)
    print(a & b)  # interseccion
    print(a - b)  # elementos que estan en a que no estan en b
    print(a ^ b)  # diferencia simentria (estan en a o en b, pero no en los dos)
    print(a.issubset(b))  # saber si los elementos de un conjunto estan en otro conjunto

    # Diccionarios

    mi_diccionario = {'rojo': 'red', 'azul': 'blue'}
    print(mi_diccionario)
    print(mi_diccionario['rojo']) # el valor de la clave que se desee

    del(mi_diccionario['rojo']) # para eliminar
    print(mi_diccionario.get('azul','Valor no encontrado'))
    print(mi_diccionario.values())
    print(len(mi_diccionario))
    
    # Pilas

    mi_pila = [1, 2, 3, 4]
    mi_pila.append(5)  # para añadir elementos al final
    print(mi_pila)
    mi_pila.pop()  # saca el ultimo elemento de la pila
    print(mi_pila)
    last = mi_pila.pop()
    print(last)

    # colas

    mi_cola = ['Miguel', 'Fran', 'Xhema']
    print(mi_cola)
    mi_cola.append('Jose Luis')  # agregar elementos
    print(mi_cola)
    # sacar elementos desde el principio (diferencia con las pilas)
    first_element = mi_cola.pop(0)
    print(first_element)
    print(mi_cola)

    # Ejercicio 11 : lista eliminar elementos repetidos

    mi_lista = [1, 2, 3, 2, 4, 5, 3]

    mi_conjunto = set(mi_lista)

    mi_lista = list(mi_conjunto)

    # podria resolverse unicamente asi: mi_lista = list(set(mi_lista))

    print(mi_lista)

    # Ejercicio 12 : crear listas a partir de listas

    lista_1 = [1, 2, 1, 5, 5, 6, 7]
    lista_2 = [2, 2, 3, 4, 4, 7, 8]

    conjunto_1 = set(lista_1)
    conjunto_2 = set(lista_2)

    union = list(conjunto_1 | conjunto_2)
    print(union)
    interseccion = list(conjunto_1 & conjunto_2)
    print(interseccion)
    solo_1 = list(conjunto_1 - conjunto_2)
    print(solo_1)
    solo_2 = list(conjunto_2 - conjunto_1)
    print(solo_2)

    # Bucle while

    import math

    numero = int(input('Digite un numero'))
    while numero < 0:
        print('Ingrese un numero mas pequeño')
        numero = int(input('Digite un numero'))
    raiz = round(math.sqrt(numero))
    print(raiz)

    # uso de iteradores
    i = 0
    while i < 10:
        print('+1')
        i += 1

    # Bucle for (sabemos cuantas veces se repite, numero determinado de iteraciones)

    for i in [1,2,3,4,5,'Miguel','Fran',8.90]:
        print_hi(f'elemento:{i}')

    coleccion = {'Miguel':19,'Javier':23}
    for clave,valor in coleccion.items():
        print(f'{clave} -> {valor}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
