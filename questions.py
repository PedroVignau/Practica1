import random

categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "animales": ["perro", "gato", "elefante", "jirafa", "tigre", "caballo", "conejo", "delfin"],
    "ciudades": ["paris", "roma", "londres", "necochea", "pinamar", "moscu", "viena", "budapest"],
    "deportes": ["futbol", "tenis", "natacion", "ciclismo", "boxeo", "rugby", "voley", "basket"],
    "comidas": ["pizza", "pasta", "asado", "empanada", "milanesa", "sushi", "hamburgesa", "tacos"],
    "frutas": ["manzana", "banana", "naranja", "uva", "pera", "mango", "sandia", "frutilla"],
}

print("¡Bienvenido al Ahorcado!")
print()

# Muestro las categorias disponibles
print("Categorías disponibles:")
for categoria in categorias:
    print(f"- {categoria}")

categoria_elegida = input("Elegí una categoría: ")

# Con esta iteracion nos aseguramos que no haya errores en el ingreso de la categoria
while categoria_elegida not in categorias:
    print("Categoría no válida, intentá de nuevo.")
    categoria_elegida = input("Elegí una categoría: ")

# random.sample() mezcla las palabras sin repetir
palabras_disponibles = random.sample(categorias[categoria_elegida], len(categorias[categoria_elegida]))

jugar_de_nuevo = "si"

while jugar_de_nuevo == "si":

    if len(palabras_disponibles) == 0:
        print("Ya jugaste con todas las palabras de esta categoría.")
        break

    word = palabras_disponibles.pop()# saca la ultima palabra de la lista y se le asigna a word, despues la palabra queda eliminada de la lista
    guessed = []
    attempts = 6
    puntaje = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        
        print(progress)
        
        if "_" not in progress:
            print("¡Ganaste!")
            print(f"Puntaje final: {puntaje}")
            break
            
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ")
        # Si se ingresa mas de una letra o algo que no sea una letra le notificara al usuario que no se puede
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue # Si ocurre salta a la proxima iteracion del while
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

    jugar_de_nuevo = input("¿Querés jugar de nuevo? (si/no): ")
while jugar_de_nuevo not in ["si", "no"]:# esta iteracion evita errores en el ingreso de si o no
    print("Entrada no válida, escribí 'si' o 'no'.")
    jugar_de_nuevo = input("¿Querés jugar de nuevo? (si/no): ")