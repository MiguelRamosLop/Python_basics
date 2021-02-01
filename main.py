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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
