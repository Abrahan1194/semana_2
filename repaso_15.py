lista_frutas = []
for i in range(3):  
    nombre = input("Introduce el nombre fruta: ")
    lista_frutas.append((nombre))    
    break

fruta = input("Introduce el nombre de la fruta que desea eliminar: ")       
if fruta in lista_frutas:
    lista_frutas.remove(fruta)
    print("La fruta ha sido eliminada")

