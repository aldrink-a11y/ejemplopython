def mostrar_estado(nombre, dinero, dignidad, hambre):
    """Función para mostrar las estadísticas actuales del jugador."""
    print("\n" + "="*30)
    print(f"ESTADO DE {nombre.upper()}:")
    print(f"💰 Dinero:   {dinero}")
    print(f"🧠 Dignidad: {dignidad}")
    print(f"🍔 Hambre:   {hambre}")
    print("="*30 + "\n")

# --- Inicio del Programa ---
nombre = input("¿Cuál es tu nombre? ").strip()
print(f"\n¡Hola, {nombre}! Bienvenido a tu nueva vida financiera.\n")

# Variables iniciales
dinero = 100
dignidad = 50
hambre = 0
jugando = True

while jugando:
    mostrar_estado(nombre, dinero, dignidad, hambre)
    
    print("¿Qué desea hacer el jugador?")
    print("1. Gastar dinero en fiestas")
    print("2. Invertir una parte")
    print("3. Ahorrar")
    print("4. Salir del juego")

    opcion = input("\nIngrese el número de la opción: ")

    if opcion == "1":
        dinero -= 20
        dignidad -= 10
        hambre += 5
        print(">> Te fuiste de fiesta. Perdiste dinero pero... ¿valió la pena?")
    
    elif opcion == "2":
        dinero -= 30
        dignidad += 5
        hambre += 2
        print(">> Inversión realizada. Tu futuro te lo agradecerá.")
        
    elif opcion == "3":
        dinero += 10
        dignidad += 2
        hambre -= 3
        print(">> Día tranquilo. Ahorraste y comiste en casa.")
        
    elif opcion == "4":
        print(f"¡Gracias por jugar, {nombre}!")
        jugando = False # Rompe el bucle para terminar
        
    else:
        print(" Opción no válida. Por favor, elige entre 1 y 4.")

    # Condición de derrota extra (opcional)
    if dinero <= 0:
        print("\n--- TE HAS QUEDADO EN LA QUIEBRA. GAME OVER ---")
        break