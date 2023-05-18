import re

def remove_datetime_multimedia(chat):
    datetime_pattern = r'\d{2}/\d{2}/\d{2} \d{1,2}:\d{2} [ap]\. m\. - '
    chat_without_datetime = re.sub(datetime_pattern, '', chat)
    chat_without_multimedia = re.sub(r'<Multimedia omitido>', '', chat_without_datetime)
    chat_without_empty_names = re.sub(r'^[^:\n]+: $', '', chat_without_multimedia, flags=re.MULTILINE)
    chat_without_hyphens = chat_without_empty_names.replace(' - ', '')
    return chat_without_hyphens.strip()

def remove_duplicate_messages(chat):
    lines = chat.split('\n')
    unique_messages = set()
    chat_without_duplicates = []

    for line in lines:
        if line not in unique_messages:
            unique_messages.add(line)
            chat_without_duplicates.append(line)

    return '\n'.join(chat_without_duplicates)

def chat_statistics(chat):
    lines = chat.split('\n')

    total_messages = len(lines)
    unique_participants = set()
    message_count = {}

    for line in lines:
        if line.strip() != '':
            if ':' in line:
                participant, message = line.split(':', 1)
                participant = participant.strip()
                unique_participants.add(participant)
                message_count[participant] = message_count.get(participant, 0) + 1

    most_active_participant = max(message_count, key=message_count.get)

    print("Estadísticas del chat:")
    print("Total de mensajes: {}".format(total_messages))
    print("Total de participantes únicos: {}".format(len(unique_participants)))
    print("El participante más activo: {}".format(most_active_participant))
    print("Número de mensajes enviados por el participante más activo: {}".format(message_count[most_active_participant]))


def process_chat(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        chat_content = input_file.read()

    chat_without_datetime_multimedia = remove_datetime_multimedia(chat_content)
    chat_without_duplicates = remove_duplicate_messages(chat_without_datetime_multimedia)

    with open(output_filename, 'w') as output_file:
        output_file.write(chat_without_duplicates)

def menu():
    print("      _____ _           _  ______ _              ")
    print("     /  __ \ |         | | |  ___(_)              ")
    print("     | /  \/ |__   __ _| |_| |_   ___  _____ _ __ ")
    print("     | |   | '_ \ / _` | __|  _| | \ \/ / _ \ '__|")
    print("     | \__/\ | | | (_| | |_| |   | |>  <  __/ |   ")
    print("     \____/_| |_|\__,_|\__\_|   |_/_/\_\___|_|   ")
    print("")

    print("1. Procesar archivo de chat")
    print("2. Mostrar estadísticas del chat")
    print("3. Salir")

    while True:
        option = input("Selecciona una opción (1-3): ")

        if option == '1':
            input_filename = input("Ingresa el nombre del archivo de entrada: ")
            output_filename = input("Ingresa el nombre del archivo de salida: ")
            process_chat(input_filename, output_filename)
            print("El archivo ha sido procesado exitosamente.")
        elif option == '2':
            input_filename = input("Ingresa el nombre del archivo de chat: ")
            with open(input_filename, 'r', encoding='utf-8') as input_file:
                chat_content = input_file.read()
            chat_statistics(chat_content)
        elif option == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
