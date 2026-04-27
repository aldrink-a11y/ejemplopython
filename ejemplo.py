nombre = input("¿Cuál es tu nombre? ")
print("¡Hola, " + nombre + "! Bienvenido al mundo de la programación en Python.")
print(f"Bienvenido al mundo de la programación en Python, {nombre}!")

dinero = 100
dignidad = 50
hambre = 0

print("El jugador ha recibido su herencia.")

print("¿Que desea hacer el jugador?")
print("1. Gastar dinero en fiestas")
print("2. Invertir una parte")
print("3. Ahorrar")

opcion = input("Ingrese el número de la opción que desea elegir: ")
if opcion == "1":
    dinero -= 20
    dignidad -= 10
    hambre += 5
    print("El jugador ha gastado dinero en fiestas. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)
elif opcion == "2":
    dinero -= 30
    dignidad += 5
    hambre += 2
    print("El jugador ha invertido una parte de su dinero. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)
elif opcion == "3":
    dinero += 10
    dignidad += 2
    hambre -= 3
    print("El jugador ha ahorrado dinero. Dinero:", dinero, "Dignidad:", dignidad, "Hambre:", hambre)