import socket, struct, os
import paho.mqtt.client as mqtt

IP = os.getenv("waveshare_ip", "192.168.1.100")
PORT = int(os.getenv("waveshare_port", "502"))
TOPIC = os.getenv("mqtt_topic", "homeassistant/sensor/go_econtroller_910332_grid_power/state")
BROKER = os.getenv("mqtt_broker", "core-mosquitto")
SLAVE_ID = int(os.getenv("slave_id", "1"))

def build_frame(slave_id, value):
    function_code = 4
    byte_count = 4
    payload = struct.pack(">f", value)
    frame = struct.pack("BBB", slave_id, function_code, byte_count) + payload
    crc = calc_crc(frame)
    return frame + crc

def calc_crc(data):
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            crc = (crc >> 1) ^ 0xA001 if crc & 1 else crc >> 1
    return struct.pack("<H", crc)

def send_frame(value):
    frame = build_frame(SLAVE_ID, value)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, PORT))
        s.sendall(frame)
        print(f"Gesendet: {value:.2f} W")

def on_message(client, userdata, msg):
    try:
        value = float(msg.payload.decode())
        send_frame(value)
    except Exception as e:
        print(f"Fehler: {e}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
client.loop_forever()
