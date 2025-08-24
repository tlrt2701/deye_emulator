# SDM630 Emulator für Deye Wechselrichter

Dieses Add-on simuliert einen SDM630-Stromzähler und sendet Modbus RTU-Telegramme über TCP an den Meter-Port eines Deye-Wechselrichters. Ideal für Einspeisebegrenzung oder Batteriesteuerung.

## Konfiguration

- `mqtt_broker`: Adresse des MQTT-Brokers (z. B. `core-mosquitto`)
- `mqtt_topic`: Topic mit dem Leistungswert
- `waveshare_ip`: IP-Adresse des RS485-TCP-Moduls
- `waveshare_port`: Port (meist `502`)
- `slave_id`: Modbus-ID (meist `1`)
