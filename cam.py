import picamera
import time

def grabar_video(nombre_archivo, duracion_segundos):
    try:
        # Inicializar la cámara
        with picamera.PiCamera() as camera:
            # Configurar resolución y framerate según sea necesario
            camera.resolution = (640, 480)
            camera.framerate = 30

            # Esperar unos segundos para que la cámara se estabilice
            time.sleep(2)

            # Grabar video
            camera.start_recording(nombre_archivo)
            print(f"Grabando video: {nombre_archivo}")
            camera.wait_recording(duracion_segundos)
            camera.stop_recording()
            print("Video grabado con éxito.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    nombre_archivo = 'video_grabado.h264'  # Puedes cambiar el nombre del archivo si lo deseas
    duracion_segundos = 10  # Duración del video en segundos

    grabar_video(nombre_archivo, duracion_segundos)
