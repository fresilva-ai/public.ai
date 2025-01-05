# Proyecto: Detección de Tumores Cerebrales

Este proyecto realiza el preprocesamiento avanzado de un conjunto de datos de **MRI de cerebros** para facilitar la detección automática de tumores cerebrales mediante algoritmos de aprendizaje profundo. El script implementa técnicas personalizadas de recorte y aumento de datos para mejorar la calidad del conjunto de entrenamiento.

## Características del proyecto

1. **Recorte automático de la región cerebral**:
   - Se utiliza un algoritmo de detección de contornos para identificar y recortar automáticamente la región del cerebro en las imágenes.
   - Esto ayuda a eliminar el fondo innecesario y mejora el enfoque del modelo en la región relevante.

2. **Transformaciones avanzadas de aumento de datos**:
   - Redimensionamiento a **224x224** píxeles.
   - Rotaciones aleatorias, traslación, escalado y cizallamiento.
   - Desenfoque gaussiano y ajustes de brillo.
   - Estas transformaciones aumentan la diversidad del conjunto de datos y ayudan a prevenir el sobreajuste.

## Estructura del código

- **Clase `CropExtremePoints`**:
  Implementa un método para recortar automáticamente la región del cerebro en las imágenes utilizando los puntos extremos del contorno más grande detectado.

- **Transformaciones**:
  Se aplica una serie de transformaciones aleatorias para aumentar la variabilidad del conjunto de datos y mejorar la robustez del modelo durante el entrenamiento.

- **Visualización**:
  Se generan visualizaciones de las imágenes transformadas para verificar la efectividad del preprocesamiento.

## Requisitos

Para ejecutar este proyecto, se requieren las siguientes bibliotecas:

- `numpy`
- `pandas`
- `matplotlib`
- `PIL` (Python Imaging Library)
- `cv2` (OpenCV)
- `imutils`
- `torch`
- `torchvision`

## Uso

1. Monta Google Drive en tu entorno de Google Colab.
2. Asegúrate de que las imágenes estén organizadas en dos carpetas:
   - **`no`**: Imágenes de cerebros sin tumores.
   - **`yes`**: Imágenes de cerebros con tumores.
3. Ejecuta el script para realizar el preprocesamiento y visualizar las transformaciones.

## Resultados esperados

- Imágenes preprocesadas con la región cerebral recortada y varias versiones aumentadas mediante transformaciones aleatorias.
- Gráficos que muestran ejemplos de las imágenes transformadas para ambas categorías (con y sin tumores).

## Aplicaciones

Este proyecto es un paso preliminar fundamental en el desarrollo de modelos de clasificación de tumores cerebrales mediante aprendizaje profundo. Las imágenes preprocesadas pueden utilizarse para entrenar redes neuronales convolucionales (CNN) u otros modelos avanzados de detección de anomalías.

## Autor

Desarrollado por: **Fredy Silva O.**

Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
