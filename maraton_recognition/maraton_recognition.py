import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Inicializar YOLOv8
model = YOLO('yolov8n.pt')  # Usa la versión YOLOv8 pequeña para rapidez

# Inicializar DeepSORT
tracker = DeepSort(max_age=30, n_init=3, nn_budget=20)

# Cargar el video
cap = cv2.VideoCapture("/Users/fredysilva/Python/public.ai/maraton_recognition/maraton_ia.mp4")
total_count = set()  # IDs únicos de personas contadas

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar personas usando YOLO
    results = model(frame, stream=True)
    detections = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas del cuadro delimitador
            conf = box.conf[0]  # Confianza
            cls = int(box.cls[0])  # Clase (0 es 'persona' en COCO)

            if cls == 0 and conf > 0.5:  # Solo detecciones de personas con confianza > 50%
                detections.append(([x1, y1, x2, y2], conf))

    # Realizar seguimiento con DeepSORT
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed() or track.time_since_update > 1:
            continue

        track_id = track.track_id  # ID único del objeto
        bbox = track.to_ltrb()  # Caja delimitadora (left, top, right, bottom)
        x1, y1, x2, y2 = map(int, bbox)

        # Dibujar el cuadro y mostrar el ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Añadir IDs únicos al conteo total
        total_count.add(track_id)

    # Mostrar el conteo total
    cv2.putText(frame, f"Total Count: {len(total_count)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Mostrar el frame
    cv2.imshow("Marathon Counting", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
