nota = input("Introduce la nota del alumno 0 a 10: ")      
if nota >= "0" and nota <= "10":
    if nota >= "5" and nota <= "7":
        print("Aprobado")
elif nota > "7": 
    print("sobresaliente")
elif nota < "5":
    print("reprobado")
else:
    print("Nota no valida")