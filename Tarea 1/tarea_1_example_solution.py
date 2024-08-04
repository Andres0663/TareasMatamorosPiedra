def operation_selector(num1, num2, operator):
    '''
    Autores:
        Andrés Matamoros
        Ismael Piedra

    Esta funcion recibe dos numeros enteros y un operador, y retorna el resultado de la operacion
    correspondiente. Los operadores permitidos son: +, -, *, &.

    Parametros:
        num1 (int): Primer operando
        num2 (int): Segundo operando
        operator (str): Operador a utilizar

    Retorna:
        int: Estado de la operacion
        int: Resultado de la operacion  
    '''
    # Validacion de los operandos
    if not isinstance(num1, int) or not isinstance(num2, int) or \
            isinstance(num1, bool) or isinstance(num2, bool):
        return -50, None

    # Validacion del tipo del operador
    if not isinstance(operator, str):
        return -60, None

    # Validacion del operador
    if operator not in ["+", "-", "*", "&"]:
        return -70, None

    # Realiza la operacion
    if operator == "+":
        return 0, num1 + num2
    elif operator == "-":
        return 0, num1 - num2
    elif operator == "*":
        return 0, num1 * num2
    elif operator == "&":
        return 0, num1 & num2
    

def calculo_promedio(lista):
    '''
    Autores:
        Andrés Matamoros
        Ismael Piedra

    Esta funcion recibe una lista de numeros enteros y retorna el promedio de los elementos de la lista.

    Parametros:
        lista (list): Lista de numeros enteros

    Retorna:
        int: Estado de la operacion
        float: Promedio de los elementos
    '''
    # Validacion de los elementos de la lista
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in lista):
        return -80, None

    # Validacion de la cantidad de elementos
    if len(lista) > 10:
        return -90, None

    # Calculo del promedio
    return 0, sum(lista)/len(lista)
