numeros =[]
for i in range(5):
    numero = int(input(f"Introduce un número: {i+1}"))
    if numero % 2 == 0:
        numeros.append(numero)

print("Lista de números pares:", numeros)
