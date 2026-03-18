import random
# agrego mas palabras y mas categorias
categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "animales": ["perro", "gato", "elefante", "jirafa", "tigre", "caballo", "conejo", "delfin"],
    "ciudades": ["paris", "roma", "londres", "necochea", "pinamar", "moscu", "viena", "budapest"],
    "deportes": ["futbol", "tenis", "natacion", "ciclismo", "boxeo", "rugby", "voley", "basquet"],
    "comidas": ["pizza", "pasta", "asado", "empanada", "milanesa", "sushi", "hamburgesa", "tacos"],
    "frutas": ["manzana", "banana", "naranja", "uva", "pera", "mango", "sandia", "frutilla"],
}
#muestro las categorias
print("Categorías disponibles:")
for categoria in categorias:
    print(f"- {categoria}")
#con esta iteracion nos aseguramos que no haya errores en el ingreso de la categoria    
categoria_elegida = input("Elegí una categoría: ")
while categoria_elegida not in categorias:
    print("Categoría no válida, intentá de nuevo.")
    categoria_elegida = input("Elegí una categoría: ")
    
word = random.choice(categorias[categoria_elegida])
guessed = []
attempts = 6
puntaje = 6
print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    
    print(progress) # Verificar si el jugador ya adivinó la palabra completa
    
    if "_" not in progress:
        print("¡Ganaste!")
        print(f"Puntaje final: {puntaje}")
        break
        
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():#si se ingresa mas de una letra o algo que no sea una letra le notificara al usuario que no se puede
        print("Entrada no válida")
        continue # si ocurre salta a la proxima iteracion del while
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {puntaje}")