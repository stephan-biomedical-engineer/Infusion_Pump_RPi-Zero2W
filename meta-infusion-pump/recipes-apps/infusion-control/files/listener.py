import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
import time
import threading

# --- CONFIGURAÇÃO HARDWARE ---
MOTOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.output(MOTOR_PIN, GPIO.LOW) 

# --- CONFIGURAÇÃO MQTT ---
BROKER = "127.0.0.1"
PORTA = 1883
TOPICO_CMD = "bomba/comando"
TOPICO_STATUS = "bomba/status"

estado_bomba = {"rodando": False, "velocidade": 0}

# --- FUNÇÕES MQTT (Atualizadas para v2.0) ---

# NOTA: A assinatura mudou! Agora recebe 'properties' no final
def ao_conectar(client, userdata, flags, rc, properties):
    print(f"Conectado ao Broker! Código: {rc}")
    client.subscribe(TOPICO_CMD)

def ao_receber(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Comando recebido: {payload}")
    
    try:
        if payload == "LIGAR":
            estado_bomba["rodando"] = True
            print(">>> MOTOR ATIVADO")
        elif payload == "PARAR":
            estado_bomba["rodando"] = False
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            print(">>> MOTOR PARADO")
    except Exception as e:
        print(f"Erro ao processar comando: {e}")

# --- LOOP DE CONTROLE ---
def loop_motor():
    while True:
        if estado_bomba["rodando"]:
            GPIO.output(MOTOR_PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(MOTOR_PIN, GPIO.LOW)
            time.sleep(0.1)
        else:
            time.sleep(0.5)

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    try:
        print("Iniciando Sistema da Bomba de Infusão (Paho v2)...")
        
        t_motor = threading.Thread(target=loop_motor)
        t_motor.daemon = True
        t_motor.start()

        # --- MUDANÇA PRINCIPAL AQUI ---
        # Agora precisamos definir explicitamente a versão da API de callback
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        
        client.on_connect = ao_conectar
        client.on_message = ao_receber
        
        client.connect(BROKER, PORTA, 60)
        
        client.loop_start()
        
        while True:
            msg_status = json.dumps(estado_bomba)
            client.publish(TOPICO_STATUS, msg_status)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nDesligando...")
        GPIO.cleanup()
        client.loop_stop()
