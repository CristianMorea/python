####### RECURCION EN EL PARADICMA FUNCIONAL


####FUNCION ITERABLE
def fun_sumLista_iter(lista):
    for n in lista:
        sum = sum+n
        return sum
    
##FUNCION RECURCIVA
def fun_sumLista_recu(lista):
    if not lista:
        return 0
    else:
        return lista[0]+fun_sumLista_recu(lista[1:])
    
def fun_sumaLista_rec_ht(lista):
    if not lista:
        return 0
    else:
        ##separa la lista en un elemento inicial y el resto
    
        head, *tail = lista
        return head + fun_sumaLista_rec_ht(tail)



##filtrar lista con los elementos > a limite
def filtra_lista(lista, limite):
    # Caso base: la lista está vacía
    if not lista:
        return []

    # Obtiene el primer elemento (head) y el resto de la lista (tail)
    head, *tail = lista

    # Verifica si el primer elemento cumple con el límite
    if head > limite:
        # Agrega el elemento al resultado y llama recursivamente con la cola (tail)
        return [head] + filtra_lista(tail, limite)

    # Si el primer elemento no cumple con el límite, simplemente llama recursivamente con la cola (tail)
    return filtra_lista(tail, limite)

# Ejemplo de uso
mi_lista = [1, 5, 8, 3, 7, 2, 10]
limite = 5

resultado_filtrado = filtra_lista(mi_lista, limite)
print(resultado_filtrado)


##EJERCICIO:

#INVERTIT UNA LISTA DE OBJETOS

# INVERTIR UNA CADENA

# FIBONNACCI 

