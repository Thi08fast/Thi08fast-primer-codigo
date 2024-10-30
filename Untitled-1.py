import random

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
       
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Salir")
       
        eleccion_usuario = input("Ingresa el número de tu elección: ")

        if eleccion_usuario == '4':
            print("¡Gracias por jugar!")
            break
        
        if eleccion_usuario not in ['1', '2', '3']:
            print("Elección inválida. Inténtalo de nuevo.")
            continue
        eleccion_usuario = int(eleccion_usuario) - 1
        eleccion_usuario_texto = opciones[eleccion_usuario]
        eleccion_computadora = random.choice(opciones)

        print(f"\nTú elegiste: {eleccion_usuario_texto}")
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_usuario_texto == eleccion_computadora:
            print("---Es un empate!---")
        elif (eleccion_usuario_texto == "piedra" and eleccion_computadora == "tijera") or \
             (eleccion_usuario_texto == "papel" and eleccion_computadora == "piedra") or \
             (eleccion_usuario_texto == "tijera" and eleccion_computadora == "papel"):
            print("---¡Ganaste!---")
        else:
            print("---Perdiste---")



piedra_papel_tijera()
