import random
import textwrap
import sys
from collections import defaultdict

# --- BANCO DE PREGUNTAS MASIVO Y CATEGORIZADO ---
# Cada pregunta ahora tiene un "topic" para agruparlas como en el documento original.
from question_bank_300 import question_bank


def run_quiz():

    # --- NUEVO: Registro de preguntas respondidas correctamente ---
    preguntas_respondidas_bien = set()

    # --- Bucle principal para permitir repetir sets de preguntas ---
    while True:
        print("=====================================================")
        print("===   SIMULADOR DE CUADERNILLO DE PRÁCTICA        ===")
        print("=====================================================\n")

        print("-------------------- INSTRUCCIONES --------------------")
        print("Este es un test de práctica similar al documento ODF.")
        print("Lee cada pregunta y responde introduciendo la letra de la opción.")
        print("\n[!] Preguntas de Respuesta Múltiple:")
        print("    - Estarán marcadas con el texto '(varias opciones)'.")
        print("    - Para responder, ingresa todas las letras correctas juntas.")
        print("    - Ejemplo: si las opciones A y C son correctas, ingresa: AC\n")
        print("-------------------------------------------------------\n")

        # --- Selección de cantidad de preguntas ---
        while True:
            try:
                num_questions_str = input(f"¿Cuántas preguntas quieres en total? (mínimo 6): ")
                if not num_questions_str:
                    num_questions_total = 12
                    print(f"Tomando el valor por defecto: {num_questions_total} preguntas.")
                    break
                num_questions_total = int(num_questions_str)
                if num_questions_total >= 6:
                    break
                else:
                    print("Por favor, ingresa un número igual o mayor a 6.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        # --- Lógica para seleccionar preguntas por tema, excluyendo las ya respondidas bien ---
        questions_by_topic = defaultdict(list)
        for idx, q in enumerate(question_bank):
            # Usamos el id() del objeto pregunta o su hash, pero mejor usar el índice para evitar problemas
            if idx not in preguntas_respondidas_bien:
                questions_by_topic[q['topic']].append((idx, q))

        topics = list(questions_by_topic.keys())
        selected_questions = []

        num_topics = len(topics)
        if num_topics == 0:
            print("\n¡Felicidades! Ya has respondido correctamente todas las preguntas disponibles.")
            break

        questions_per_topic = num_questions_total // num_topics
        remainder = num_questions_total % num_topics

        for topic in topics:
            num_to_pick = questions_per_topic
            if remainder > 0:
                num_to_pick += 1
                remainder -= 1

            if num_to_pick > len(questions_by_topic[topic]):
                num_to_pick = len(questions_by_topic[topic])

            if num_to_pick > 0:
                selected_questions.extend(random.sample(questions_by_topic[topic], k=num_to_pick))

        random.shuffle(selected_questions)

        if not selected_questions:
            print("\nNo quedan preguntas nuevas para practicar. ¡Bien hecho!")
            break

        print(f"\nSe han seleccionado {len(selected_questions)} preguntas. ¡Mucha suerte!\n")

        user_responses = []
        current_topic = ""

        for i, (q_idx, q) in enumerate(selected_questions):
            if q['topic'] != current_topic:
                current_topic = q['topic']
                print(f"\n--- SECCIÓN: {current_topic} ---\n")

            q_type_text = "una opción" if q['type'] == 'single' else "varias opciones"

            print(f"{i+1}. ({q_type_text}) {q['question']} (Universo: {q['universe']})")

            for j, option in enumerate(q['options']):
                print(f"  {chr(65+j)}) [ ] {option}")

            prompt = "\n> Tu respuesta (letra): "
            if q['type'] == 'multiple':
                prompt = "\n> Tu respuesta (letras, ej: AC): "

            user_answer_str = input(prompt).upper().strip()

            user_answer_indices = []
            valid_input = True
            if not user_answer_str:
                valid_input = False
            else:
                for char in user_answer_str:
                    index = ord(char) - ord('A')
                    if 0 <= index < len(q['options']) and index not in user_answer_indices:
                        user_answer_indices.append(index)
                    else:
                        valid_input = False; break

            if not valid_input:
                print("\n** Respuesta inválida. Se tomará como incorrecta. **")
                user_answer_indices = []

            user_responses.append({"question_data": q, "user_indices": sorted(user_answer_indices), "q_idx": q_idx})
            print("\n" + "-"*70 + "\n")

        # --- FASE DE CORRECCIÓN Y FEEDBACK ---
        print("\n\n=============================================")
        print("===         RESULTADOS DEL TEST           ===")
        print("=============================================\n")

        score = 0
        incorrect_answers = []
        for response in user_responses:
            q_data = response['question_data']
            if response['user_indices'] == sorted(q_data['correct_answers']):
                score += 1
                preguntas_respondidas_bien.add(response['q_idx'])
            else:
                incorrect_answers.append(response)

        final_grade = (score / len(selected_questions)) * 10

        print(f"Respuestas correctas: {score} de {len(selected_questions)}")
        print(f"Tu nota final es: {final_grade:.2f} / 10.00\n")

        if final_grade >= 9: print("¡Excelente! Demuestras un dominio sólido de los conceptos.")
        elif final_grade >= 7: print("¡Muy buen trabajo! Tienes una base fuerte. Revisa los errores para perfeccionar.")
        elif final_grade >= 4: print("¡Buen esfuerzo! Hay conceptos clave que necesitas reforzar.")
        else: print("Necesitas repasar los temas fundamentales. La revisión te ayudará.")

        if incorrect_answers:
            print("\n\n--- REVISIÓN DETALLADA DE ERRORES ---\n")
            for i, response in enumerate(incorrect_answers):
                q_data = response['question_data']
                user_indices = response['user_indices']
                correct_indices = q_data['correct_answers']

                print(f"Pregunta fallada #{i+1}: {q_data['question']} (Sección: {q_data['topic']})")

                user_ans_letters = "".join([chr(65+idx) for idx in user_indices]) or "NINGUNA"
                correct_ans_letters = "".join([chr(65+idx) for idx in correct_indices])

                print(f"   -> Tu respuesta:      [{user_ans_letters}]")
                print(f"   -> Respuesta correcta: [{correct_ans_letters}]")

                # Mostrar justificación de la respuesta correcta
                for idx in correct_indices:
                    justif = q_data['justification'].get(str(idx), "(Sin justificación)")
                    print(f"   -> Justificación correcta ({chr(65+idx)}):\n" + '\n'.join(textwrap.wrap(justif, width=65, initial_indent='      ', subsequent_indent='      ')))

                # Si la respuesta del usuario es distinta, mostrar su justificación también
                for idx in user_indices:
                    if idx not in correct_indices:
                        justif = q_data['justification'].get(str(idx), "(Sin justificación)")
                        print(f"   -> Justificación de tu respuesta ({chr(65+idx)}):\n" + '\n'.join(textwrap.wrap(justif, width=65, initial_indent='      ', subsequent_indent='      ')))

                print("-" * 50 + "\n")

        # --- Preguntar si el usuario quiere seguir practicando ---
        seguir = input("¿Quieres practicar más preguntas? (s/n): ").strip().lower()
        if seguir != 's':
            print("\n¡Gracias por practicar! Hasta la próxima.")
            break

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nTest interrumpido. ¡Hasta la próxima!")
        sys.exit(0)