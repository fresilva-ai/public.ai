# instalar dependencias: pip install cvzone mediapipe opencv-python
import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)
video = cv2.VideoCapture(1)

if not video.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

print("Presiona 'q' para salir.")

while True:
    ret, frame = video.read()
    if not ret:
        print("No se pudo capturar el cuadro de video.")
        break
    
    hands, processed_frame = detector.findHands(frame)
    if hands:
        for hand in hands:
            handType = hand["type"]
            print(f"Mano detectada: {handType}")
            centerX, centerY = hand["center"]
            print(f"Centro de la palma: ({centerX}, {centerY})")
    
    cv2.imshow("Detección de Manos", processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()