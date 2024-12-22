import cv2
import numpy as np

# Ruta a los archivos de YOLO
config_path = "/Users/fredysilva/Python/public.ai/public.ai/object_recognition/yolov4.cfg"
weights_path = "/Users/fredysilva/Python/public.ai/public.ai/object_recognition/yolov4.weights"
classes_path = "/Users/fredysilva/Python/public.ai/public.ai/object_recognition/coco.names"

# Cargar las clases de COCO
with open(classes_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Configuración de YOLO
net = cv2.dnn.readNet(weights_path, config_path)
layer_names = net.getLayerNames()
#output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# Obtener los nombres de las capas de salida
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


# Configuración de colores para las clases
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Captura desde la cámara
cap = cv2.VideoCapture(0)  # 0 para webcam; cambia a ruta de video si es necesario

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # Procesar la imagen
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    # Extraer información de los objetos detectados
    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Umbral de confianza
                # Obtener las coordenadas del objeto
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Coordenadas de la caja delimitadora
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplicar supresión no máxima
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]

            # Dibujar la caja delimitadora y el texto
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Mostrar la imagen con los objetos detectados
    cv2.imshow("Object Detection", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
