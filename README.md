# ChatFixer

ChatFixer es una herramienta de procesamiento de archivos de chat que te permite limpiar, analizar y obtener estadísticas de tus conversaciones. Puedes utilizar este programa para eliminar información no deseada, eliminar mensajes duplicados y obtener información útil sobre el chat.

## Características

- Eliminación de información de fecha y multimedia.
- Eliminación de mensajes duplicados.
- Estadísticas del chat, incluyendo total de mensajes, participantes únicos y participante más activo.

## Requisitos

- Python 3.7 o superior

## Instalación

1. Clona el repositorio o descarga los archivos en tu computadora.
2. Asegúrate de tener Python 3.7 o superior instalado.
3. Instala las dependencias ejecutando el siguiente comando:

   ```shell
   pip install -r requirements.txt
   ```
## Uso

Para exportar un chat de WhatsApp y convertirlo en un archivo de texto, sigue estos pasos:

1. Abre la aplicación de WhatsApp y selecciona el chat que quieres exportar.
2. Toca el icono de los tres puntos en la esquina superior derecha y elige **Más** y luego **Exportar chat**.
3. Elige el método de exportación que prefieras, por ejemplo, enviarlo por correo electrónico o guardar un archivo .zip en tu dispositivo. (Si necesitas más ayuda, visita nuestro [repositorio en GitHub](https://github.com/conversor-de-chats)).
4. Una vez que tengas el archivo exportado en tu computadora, abre el programa y selecciona el archivo. (Asegurece que lo tenga instalado)
5. El programa creará un nuevo archivo de texto en la misma carpeta que el archivo original.
6. Revisa el archivo de texto y asegúrate de que esté correcto y sin errores.

## Ejemplos de Archivos de Chat
El archivo de chat debe estar en formato de texto plano y seguir una estructura similar a la siguiente:

```
01/01/22 10:00 a.m - Usuario1: ¡Hola a todos!
01/01/22 10:05 a.m - Usuario2: ¡Hola Usuario1! ¿Cómo estás?
01/01/22 10:10 a.m - Usuario1: ¡Bien, gracias! ¿Y tú?
```
Despues el programa le dara el siguiente texto:

```
Usuario1: ¡Hola a todos!
Usuario2: ¡Hola Usuario1! ¿Cómo estás?
Usuario1: ¡Bien, gracias! ¿Y tú?
```

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema, tienes una idea para mejorar el programa o deseas añadir nuevas características, no dudes en abrir un issue o enviar un pull request.
