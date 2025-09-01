# Programa que genera las tablas de multiplicar según el numero ingresado por el usuario.

from os import system


# Bloque de mensajes que el programa mostrará eventualmente. 

def encabezado():
    print("*" * 60)
    print("                    Generador de Tablas de Multiplicar")
    print("*" * 60)

def mensaje_campo_vacio():
    print("No debes dejar el campo vacio. Intentalo de nuevo..")

def mensaje_no_digito():
    print("Debes ingresar solo numeros enteros. Intentalo de nuevo..")

def mensaje_fuera_del_rango():
    print("El numero debe ser del 1 al 10. Intentalo de nuevo..")

def mensaje_no_letra():
    print("Debes ingresar s/n. Intentalo de nuevo..")

def mensaje_despedida():
    print("Gracias por participar, nos vemos.")

# Separadores visuales que haran mas legible el programa.
def espacio():
    print("\n")

def separador():
    print("-" * 60)

# Bloque de solicitudes de datos al usuario.
def numero_usuario():
    espacio()
    respuesta = input("Ingresa un numero del 1 al 10, para generar una tabla de multiplicar: ")
    return respuesta

def pregunta_seguir_multiplicando():
    return input("¿Quieres seguir multiplicando?:  (s/n)  ")


# Bloque de verificaciones independientes del programa.

# Función que verifica si el usuario ha dejado el campo vacio con el metodo strip().
def campos_vacios(numero):
    if numero.strip() == "":
        return True
# Función que verifica si el usuario ha ingresado un digito y no una letra o caracter.
def digito(numero):
    if numero.isdigit():
        return True
# Función que verifica si el dato ingresado por el usuario esta dentro del rango establecido.
def fuera_rango(numero):
    if int(numero) <= 0 or int(numero) > 10:
        return True
# Función que verifica si el dato ingresado por el usuario es un caracter y no un número.
def es_letra(letra):
    if letra.isalpha():
        return True

# Bloque de la verificación completa para el dato inicial ingresado por el usuario:

# Función que realiza las siguientes verificaciones:
    # Se verifica si el usuario no dejó el campo vacio, si es asi, se le hace saber.
    # Se veririca que, el numero ingresado por el usuario sea un numero y no una letra o caracter, si es asi, se le hace saber.
    # Se verifica que, el numero del usuario esta en el rango de numeros establecido: mayor que 1 y menos que 10 para poder generar la tabla de multiplicar.
    # En el caso de que el numero solicitado, se haya ingreado de manera corecta, se realizan la siguientes acciones:
        # El numero ingresado se convierte a entero.
        # La variable "valido" se reasigna como "True" para que el bucle finalice y se siga con el flujo del programa.
        # Se retorna la variable "numero" que contiene el numero ingresado por el usuario.

def verificacion():
    valido = False
    while not valido:
        numero = numero_usuario()
        if campos_vacios(numero):
            mensaje_campo_vacio()
        elif not digito(numero):
            mensaje_no_digito()
        elif fuera_rango(numero):
            mensaje_fuera_del_rango()
        else:
            numero = int(numero)
            valido = True
    return numero

# Función que, mediante el numero ingresado por el usuario, se genera la tabla de multiplicar de la siguiente manera:
    # Se muestra una linea de guiones como separador de esta función.
    # Se muestra el mensaje, indicando de que numero será la tabla de multiplicar.
    # Se deja un espacio.
    # Mediante un bucle for, se va multiplicando la iteracion correspondiente por el numero ingresado por el usuario, en un rango del 1 al 11.
    # El rango va del 1 al 11 para poder mostrar la multiplicacion por 10.
    # Se muestra la multiplicacion presente de manera sucesiva, asi como el resultado.
    # Se muestra un separador de guiones, dando paso a la siguiente indicación del programa.
def multiplicacion(numero):
    separador()
    print(f"Tabla del numero: {numero}")
    espacio()
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    separador()

# Bloque de logica princial que realiza las siguientes operaciones:
    # Mediante el bucle while se verifica que, mientras la bandera "seguir_multiplicando" se mantenga en modo "False" se realizarán las siguientes operaciones:
        # Se mostrará el encabezado.
        # Se almacenará el numero que devuelve la verificación completa.
        # Se mostrar un espacio.
        # Se realizará la multiplicación del numero del usuario por la iteración del bucle.
        # Se mostrara un espacio separador.
        # Mediante otro bucle while, se verificará que, mientras la bandera "valido" no cambie a "False", se realizarán las siguientes operaciones:
        # Se almacena el caracter devuelto por la pregunta al usuario para que siga multiplicando, en el caso de que, asi lo decida.
        # Se realiza el estandar de verificaciónes correspondientes:
            # Si el usuario ha dejado el campo vacio.
            # Si el dato ingresado por el usuario es un caracter y no un numero.
            # Se verifica que, si el dato ingresado por el usuario es diferente a los caracteres establecidos, se le hace saber para solitarlos de nuevo.
            # En el caso de que, el dato ingresado sea igual a "n", el programa muestra un mensaje de despedida y posteriormente finaliza.
            # En el caso de que, el dato ingresado sea igual a "s", el programa cambia la bandera "valido" a "True" para salir del bucle y limpia la pantalla....
            # para mostrar de nuevo el encabezado y solicitar de nuevo un numero para multiplicar.
seguir_multiplicando = False

while not seguir_multiplicando:
    encabezado()
    numero = verificacion()
    espacio()
    multiplicacion(numero)
    espacio()

    valido = False
    while not valido:

        respuesta = pregunta_seguir_multiplicando().lower()
        if campos_vacios(respuesta):
            mensaje_campo_vacio()
        elif not es_letra(respuesta):
            mensaje_no_letra()
        elif respuesta != "s" and respuesta != "n":
            mensaje_no_letra()
        elif respuesta == "n":
            mensaje_despedida()
            valido = True
            seguir_multiplicando = True
        elif respuesta == "s":
            valido = True
            system("cls")
       
# Fin del programa.

