lista =["coco", "piña", "mango"]
eliminar_ultimo = input("¿Desea eliminar el último elemento de la lista? (si/no): ")
if eliminar_ultimo.lower() == "si":
    if lista:  
        lista.pop()
        print("Último elemento eliminado.")
    else:
        print("La lista ya está vacía.")