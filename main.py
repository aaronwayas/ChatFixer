import re
import zipfile
import os


# Funciones para chatfixer

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

def process_chat(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        chat_content = input_file.read()

    chat_without_datetime_multimedia = remove_datetime_multimedia(chat_content)
    chat_without_duplicates = remove_duplicate_messages(chat_without_datetime_multimedia)

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(chat_without_duplicates)

    print("El archivo ha sido procesado exitosamente.")


def chat_statistics(chat):
    lines = chat.split('\n')
    total_messages = len(lines)
    participants = set()
    participant_messages = {}

    for line in lines:
        if line:
            if ':' in line:
                participant, message = line.split(':', 1)
                participants.add(participant)
                participant_messages[participant] = participant_messages.get(participant, 0) + 1

    unique_participants = len(participants)
    most_active_participant = max(participant_messages, key=participant_messages.get)
    most_active_participant_messages = participant_messages[most_active_participant]

    print("Estadísticas del chat:")
    print(f"Total de mensajes: {total_messages}")
    print(f"Total de participantes únicos: {unique_participants}")
    print(f"El participante más activo: {most_active_participant}")
    print(f"Número de mensajes enviados por el participante más activo: {most_active_participant_messages}")

def chatfixer_menu():
    print("=== Chatfixer ===")
    print("1. Procesar archivo de chat")
    print("2. Estadísticas del chat")
    print("3. Volver al menú principal")
    print()

    while True:
        option = input("Ingresa el número de la opción deseada: ")

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
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Funciones para chatZIP

def compress_file(input_file, output_file):
    with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(input_file, os.path.basename(input_file))

    print("El archivo ha sido comprimido exitosamente.")

def decompress_file(input_file, output_file):
    with zipfile.ZipFile(input_file, 'r') as zipf:
        zipf.extractall(output_file)

    print("El archivo ha sido descomprimido exitosamente.")

def get_file_info(file_path):
    file_size = os.path.getsize(file_path)
    print(f"Información del archivo:")
    print(f"Ruta: {file_path}")
    print(f"Tamaño: {file_size} bytes")

def chatZIP_menu():
    print("=== ChatZIP ===")
    print("1. Comprimir archivo")
    print("2. Descomprimir archivo")
    print("3. Obtener información del archivo")
    print("4. Volver al menú principal")
    print()

    while True:
        option = input("Ingresa el número de la opción deseada: ")

        if option == '1':
            input_file = input("Ingresa el nombre del archivo a comprimir: ")
            output_file = input("Ingresa el nombre del archivo comprimido de salida: ")
            compress_file(input_file, output_file)
        elif option == '2':
            input_file = input("Ingresa el nombre del archivo comprimido: ")
            output_file = input("Ingresa el nombre del archivo descomprimido de salida: ")
            decompress_file(input_file, output_file)
        elif option == '3':
            file_path = input("Ingresa el nombre del archivo: ")
            get_file_info(file_path)
        elif option == '4':
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Menú principal

def main_menu():
    print("")
    print(" ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄    ▄ ▄▄   ▄▄ ")
    print("█       █  █ █  █      █       █  █▄█  █       █  █  █ █  █ █  █")
    print("█       █  █▄█  █  ▄   █▄     ▄█       █    ▄▄▄█   █▄█ █  █ █  █")
    print("█     ▄▄█       █ █▄█  █ █   █ █       █   █▄▄▄█       █  █▄█  █")
    print("█    █  █   ▄   █      █ █   █ █       █    ▄▄▄█  ▄    █       █")
    print("█    █▄▄█  █ █  █  ▄   █ █   █ █ ██▄██ █   █▄▄▄█ █ █   █       █")
    print("█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█ █▄▄▄█ █▄█   █▄█▄▄▄▄▄▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█")
    print("")
    print("1. Chatfixer")
    print("2. ChatZIP")
    print("3. Salir")
    print()

    while True:
        option = input("Ingresa el número de la opción deseada: ")

        if option == '1':
            chatfixer_menu()
        elif option == '2':
            chatZIP_menu()
        elif option == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el menú principal
main_menu()
