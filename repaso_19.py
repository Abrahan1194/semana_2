numeros_desorganizados = [5, 2, 9, 1, 5, 6]
buscado =int(input("Introduce el número a buscar: "))
if buscado in numeros_desorganizados:
    posicion = numeros_desorganizados.index(buscado)
    print("El número", buscado, "se encuentra en la lista en la posición", posicion+1)