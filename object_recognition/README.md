```markdown
# 📷 Script de Reconocimiento de Objetos con Python

Este proyecto implementa un sistema de reconocimiento de objetos utilizando **Python** y **YOLOv4**.
Permite identificar y clasificar objetos en tiempo real usando la cámara de tu computadora o un archivo de video.

---

## ⚙️ Requisitos del Sistema

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- **Python 3.8 o superior**
- Sistema operativo Windows, macOS o Linux
- Cámara conectada (si usas detección en tiempo real)

---

## 📦 Instalación Paso a Paso

### 1. **Descargar el Repositorio**
Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2. **Descargar Archivos Necesarios**
Descarga los siguientes archivos y colócalos en la misma carpeta que el script `object_recognition.py`:

- **YOLOv4 Config**: [yolov4.cfg](https://github.com/AlexeyAB/darknet/blob/master/cfg/yolov4.cfg)
- **YOLOv4 Pesos**: [yolov4.weights](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights)
- **Clases de COCO**: [coco.names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

### 3. **Instalar Dependencias**
Ejecuta el siguiente comando en tu terminal para instalar las bibliotecas necesarias:
```bash
pip install opencv-python opencv-python-headless numpy
```

### 4. **Verificar la Cámara**
Si planeas usar la cámara, asegúrate de que esté conectada y funcionando. Si prefieres usar un video, actualiza esta línea en el script:
```python
cap = cv2.VideoCapture("ruta_al_video.mp4")
```

---

## 🚀 Ejecución del Script

1. Abre una terminal en la carpeta donde descargaste los archivos.
2. Ejecuta el script con:
   ```bash
   python object_recognition.py
   ```
3. La ventana mostrará el video con los objetos detectados resaltados con cuadros y etiquetas.

---

## 🛠 Solución de Problemas

### Error: "ModuleNotFoundError"
- Asegúrate de haber instalado todas las dependencias con `pip install -r requirements.txt`.

### Error: "Archivo no encontrado"
- Verifica que los archivos `yolov4.cfg`, `yolov4.weights` y `coco.names` estén en el mismo directorio que el script.

### La cámara no funciona
- Verifica que la cámara esté conectada y funcionando. Intenta con diferentes índices en:
  ```python
  cap = cv2.VideoCapture(0)  # Cambia 0 a 1, 2, etc.
  ```

---

## ✨ Notas Adicionales

- **Umbral de Confianza**: Ajusta la sensibilidad cambiando `confidence > 0.5` en el script.
- **Salidas Personalizadas**: Si deseas guardar el video con detecciones, implementa `cv2.VideoWriter` en el script.

---

¡Gracias por usar este proyecto! Si tienes dudas o sugerencias, no dudes en abrir un **issue** o contactarme.
```

Este `README.md` está diseñado para guiar a los usuarios paso a paso en la instalación y ejecución del script. ¡Solo necesitas personalizarlo con tus detalles!
