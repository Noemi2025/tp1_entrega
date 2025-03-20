import random
# Se importa el modulo sys para que el juego termine si el usuario elige 
# respuestas que no están en la lista de opciones
import sys  

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Inicialización del puntaje
puntaje = 0

# Se combina las preguntas, respuestas y respuestas correctas en una lista
combined_questions = list(zip(questions, answers, correct_answers_index))

# Se seleccionan 3 preguntas aleatorias de la lista de preguntas sin repeticiones
questions_to_ask = random.sample(combined_questions, 3)

# El usuario deberá contestar 3 preguntas
for question, possible_answers, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(possible_answers): 
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        # Se solicita la respuesta del usuario
        user_input = input("Respuesta: ")

        # verifica si la entrada del usuario no es un número entero válido (positivo o negativo).
        if not user_input.lstrip('-').isdigit():  
            print("Respuesta no válida. Debe ser un número entre 1 y 4.")
            print("Fin del juego.")
            sys.exit(1)  
        else:
            # Convertir la respuesta a un número entero
            user_answer = int(user_input)

            # Verificar que el número esté en el rango correcto (1 a 4)
            if user_answer < 1 or user_answer > 4:
                print("Respuesta no válida. Debe ser un número entre 1 y 4.")
                print("Fin del juego.")
                sys.exit(1)  
            else:
                # Ajustar el índice para que coincida con las opciones (0-3)
                user_answer -= 1

                # Se verifica si la respuesta es correcta
                if user_answer == correct_index:
                    print("¡Correcto!")
                    puntaje = puntaje + 1
                    break  
                else:
                    print("Incorrecto. Intenta de nuevo.")
                    puntaje = puntaje - 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(possible_answers[correct_index])

    # Se imprime un blanco al final de la pregunta
    print()
    
    # Se muestra el puntaje del usuario
    print(f"Tu puntaje es: {puntaje}")