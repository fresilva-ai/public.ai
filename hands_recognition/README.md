# Detección de Manos y Conteo de Dedos usando OpenCV y CVZone

Este proyecto utiliza Python, OpenCV y la biblioteca CVZone para detectar manos en tiempo real a través de una cámara web y contar la cantidad de dedos levantados. El script dibuja cajas delimitadoras alrededor de las manos detectadas y proporciona retroalimentación en tiempo real sobre gestos, como cuando se levantan todos los dedos.

## Funcionalidades
- Detecta manos en tiempo real utilizando una cámara web.
- Identifica el tipo de mano detectada (derecha o izquierda).
- Cuenta la cantidad de dedos levantados.
- Resalta las manos detectadas con cajas delimitadoras.
- Muestra un mensaje cuando se reconoce un gesto específico (por ejemplo, todos los dedos levantados).

## Requisitos Previos
Antes de ejecutar el script, asegúrate de tener lo siguiente instalado:
- Python 3.6 o superior.
- OpenCV.
- CVZone.
- MediaPipe.

Para instalar las bibliotecas necesarias, ejecuta:
```bash
pip install opencv-python cvzone mediapipe

Cómo Ejecutar
	1.	Clona este repositorio o copia el script en tu máquina local.
	2.	Abre una terminal y navega al directorio donde está el script.
	3.	Ejecuta el script con:

python hands_recognition.py

	4.	Asegúrate de que tu cámara web esté conectada y funcionando correctamente.

Cómo Funciona
	1.	El script inicializa la cámara web y el detector de manos de la biblioteca CVZone.
	2.	En cada cuadro de video:
	•	Detecta manos y sus cajas delimitadoras.
	•	Cuenta la cantidad de dedos levantados usando el método fingersUp.
	•	Dibuja cajas delimitadoras y muestra mensajes para gestos específicos en el video procesado.
	3.	El programa se ejecuta en tiempo real y se detiene al presionar la tecla q.

Ejemplo de Salida

Cuando el script se está ejecutando, verás:
	•	Cajas delimitadoras alrededor de las manos detectadas.
	•	Retroalimentación en tiempo real en la consola:
	•	Tipo de mano (Derecha/Izquierda).
	•	Centro de la palma.
	•	Número de dedos levantados.
	•	Indicadores visuales para gestos específicos en el video procesado.

Solución de Problemas
	•	No detecta los dedos: Asegúrate de tener buena iluminación y un fondo claro para mejorar la precisión de la detección.
	•	La cámara no funciona: Verifica el índice de la cámara en el script (cv2.VideoCapture(0)). Cambia el 0 por 1 u otro índice si es necesario.
	•	Error ModuleNotFoundError: Instala las dependencias faltantes con pip install.

Mejoras Futuras
	•	Añadir soporte para gestos personalizados.
	•	Mejorar el rendimiento en sistemas de gama baja.
	•	Extender la funcionalidad para soportar múltiples cámaras.

Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT. Siéntete libre de usarlo y modificarlo según sea necesario.
