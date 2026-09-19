import wiringpi
import time

# Inicializar el sistema usando la numeración wPi
wiringpi.wiringPiSetup()

# El Pin físico 7 es el wPi 2
LED = 2

# Configurar el pin como salida (1 = Out)
wiringpi.pinMode(LED, 1)

print("Iniciando parpadeo... Presiona Ctrl+C para detener.")

try:
    while True:
        wiringpi.digitalWrite(LED, 1)  # Enviar voltaje (Encender)
        time.sleep(0.5)  # Esperar medio segundo
        wiringpi.digitalWrite(LED, 0)  # Cortar voltaje (Apagar)
        time.sleep(0.5)  # Esperar medio segundo

except KeyboardInterrupt:
    # Al presionar Ctrl+C, nos aseguramos de que el LED quede apagado
    wiringpi.digitalWrite(LED, 0)
    print("\nPrograma terminado.")