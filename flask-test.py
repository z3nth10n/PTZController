# https://carlrowan.wordpress.com/2018/12/23/ip-camera-control-using-python-via-onvif-for-opencv-image-processing/

from flask import Flask, Response
import cv2

app = Flask(__name__)

# URL del stream RTSP (reemplaza con tu enlace)
rtsp_url = ""

def generate_frames():
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        print("No se puede conectar al stream RTSP")
        exit()

    while True:
        # Leer frame por frame
        success, frame = cap.read()
        if not success:
            break
        else:
            # Codificar el frame en formato JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Usar yield para enviar el frame en tiempo real
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    # Retorna la respuesta con el contenido de los frames generados
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)