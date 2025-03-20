import random
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
    ( "// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario", ),
    ("=", "==", "!=", "==="),]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Combinar en una lista de tuplas
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
#Inicializar el puntaje
puntaje=0
# El usuario deberá contestar 3 preguntas
for question, answer_options, correct_index in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para respondercorrectamente
    errores=0
    for intento in range(2):
        user_answer = input ("Respuesta: ")
        if user_answer.isdigit():  # Verificar si es un número
            user_answer = int(user_answer) - 1  # Convertir a índice base 0
            if 0 <= user_answer < len(answer_options): # Verificar rango
                # Se verifica si la respuesta es correcta
                if user_answer == correct_index:
                    print("¡Correcto!")
                    puntaje += 1  # Sumar 1 punto por acierto
                    break
                else:
                    print("Incorrecto. Intenta de nuevo.")
                    errores += 1
            else:
                print("Respuesta no válida")
                sys.exit(1)
        else:
            print("Respuesta no válida")
            sys.exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_index])
    puntaje= puntaje - (0.5*errores)
    # Se imprime un blanco al final de la pregunta
    print()

# Mostrar puntaje final

print(f"Tu puntaje final es: {puntaje}")