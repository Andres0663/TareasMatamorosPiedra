def ordenar_lista_descendente(lista):
    '''
    Ordena una lista de 5 números de mayor a menor. 
    Parámetros:  Lista de 5 números. 
    Retorna: Lista ordenada de mayor a menor.
    '''
    # Verificar que la lista tenga exactamente 5 elementos
    if len(lista) != 5: 
        raise ValueError("La lista debe contener exactamente 5 números.")

    # Ordenar la lista de mayor a menor
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada
