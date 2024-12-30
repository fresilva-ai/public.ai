# Contador de Personas en una Maratón utilizando YOLO y DeepSORT

## Introducción

Hola, soy el desarrollador de este proyecto, y quiero compartir contigo cómo he creado una solución para contar personas en un video de una maratón sin duplicar los registros. Este proyecto combina la potencia de YOLOv8 para la detección de objetos y DeepSORT para el seguimiento y asignación de IDs únicos a cada persona. El objetivo es garantizar un conteo preciso, evitando que una misma persona se registre más de una vez.

---

## Caso de Uso

En eventos como maratones, es crucial contar con precisión la cantidad de participantes, ya sea por razones logísticas, análisis estadístico o por simple interés de monitorear el flujo de personas. Este proyecto resuelve el problema utilizando visión por computadora para:

1. Detectar personas en tiempo real en un video de una maratón.
2. Asignar a cada persona un ID único para garantizar que no se cuente dos veces.
3. Mostrar un conteo acumulativo de participantes en pantalla.

---

## Tecnologías Utilizadas

1. **Python**: Lenguaje de programación principal.
2. **OpenCV**: Para manipulación de video y visualización.
3. **YOLOv8**: Modelo de detección de objetos, especializado en identificar personas.
4. **DeepSORT**: Algoritmo de seguimiento que asigna IDs únicos a los objetos detectados.

---

## ¿Cómo Funciona?

1. **Detección con YOLOv8**:
   - Se utiliza el modelo YOLOv8 preentrenado para identificar personas en cada cuadro del video.
   - Sólo se consideran detecciones con una alta confianza para reducir falsos positivos.

2. **Seguimiento con DeepSORT**:
   - Cada persona detectada se asocia con un ID único utilizando DeepSORT.
   - El sistema asegura que incluso si una persona se oculta momentáneamente, no se cree un nuevo ID.

3. **Conteo Acumulativo**:
   - Se lleva un registro de los IDs únicos asignados, lo que permite contar cuántas personas han sido detectadas en total sin duplicar datos.

---

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta el script principal:
   ```bash
   python maraton_recognition.py
   ```

4. Disfruta viendo cómo se detectan y cuentan las personas en el video de la maratón. Puedes detener el programa presionando la tecla `q`.

---

## Requisitos Previos

1. Python 3.8 o superior.
2. Paquetes instalados:
   - OpenCV
   - Ultralytics
   - DeepSORT

---

## Ejemplo de Resultado

Al ejecutar el programa, verás el video con cuadros delimitadores alrededor de cada persona detectada, junto con su ID único. En la esquina superior izquierda de la pantalla, se mostrará el conteo total de personas detectadas.

---

## Próximos Pasos

- Implementar una línea de interés (ROI) para contar solo a las personas que cruzan una línea específica.
- Optimizar el rendimiento para manejar videos de alta resolución en tiempo real.
- Añadir soporte para múltiples clases de detección, como ciclistas o vehículos.

---

## Conclusión

Este proyecto es un ejemplo práctico de cómo la inteligencia artificial y la visión por computadora pueden aplicarse para resolver problemas del mundo real. Si tienes sugerencias, comentarios o ideas para mejorar este proyecto, ¡estaré encantado de escucharlas!
