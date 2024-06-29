import cv2

# Inicializa la cámara
camara = cv2.VideoCapture(0)

# Verifica si la cámara se abrió correctamente
if not camara.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Lee cuadros de la cámara
while True:
    # Lee un cuadro de la cámara
    ret, frame = camara.read()

    # Verifica si se pudo leer el cuadro
    if not ret:
        print("No se pudo leer el cuadro de la cámara")
        break

    # Muestra el cuadro en una ventana
    cv2.imshow('Cámara', frame)

    # Espera hasta que se presione la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
camara.release()
cv2.destroyAllWindows()
