import os
import time


# Creamos una clase para manejar cualquier pin fácilmente
class PinDigital:
    def __init__(self, wpi_num):
        self.pin = wpi_num
        # Le dice a la consola que configure el pin como salida
        os.system(f"gpio mode {self.pin} out")

    def encender(self):
        os.system(f"gpio write {self.pin} 1")

    def apagar(self):
        os.system(f"gpio write {self.pin} 0")


# Inicializamos el LED en el pin wPi 2 (Físico 7)
led = PinDigital(2)

print("Iniciando parpadeo... Presiona Ctrl+C para detener.")

try:
    while True:
        led.encender()
        time.sleep(0.5)
        led.apagar()
        time.sleep(0.5)

except KeyboardInterrupt:
    # Apagado de seguridad al interrumpir
    led.apagar()
    print("\nPrograma terminado limpiamente.")