from machine import Pin, I2C
import time
import network
import urequests
from bme680 import BME680_I2C
from ssd1306 import SSD1306_I2C

# ==== CONFIG ====
SSID = "Redmi Note 11T 5G"
PASSWORD = "9494081952"
THINGSPEAK_API_KEY = "92CCOLTLA067FC35"

TEMP_THRESHOLD = 35        # Celsius
GAS_THRESHOLD = 10000       # Ohms
HUMIDITY_THRESHOLD = 80     # %
DELAY = 15                  # Seconds
# =================

# Connect to Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print("✅ Connected:", wlan.ifconfig())

# Send data to ThingSpeak
def send_to_thingspeak(api_key, temp, hum, gas, flame, status_code):
    url = "https://api.thingspeak.com/update"
    data = {
        "api_key": api_key,
        "field1": temp,
        "field2": hum,
        "field3": gas,
        "field4": flame,
        "field5": status_code
    }
    try:
        response = urequests.post(url, json=data)
        print("📡 ThingSpeak:", response.text)
        response.close()
    except Exception as e:
        print("❌ ThingSpeak Error:", e)

# I2C setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # GP1 = SCL, GP0 = SDA

# OLED display
oled = SSD1306_I2C(128, 64, i2c)

# BME680 sensor
try:
    bme = BME680_I2C(i2c=i2c)
    print("✅ BME680 initialized.")
except Exception as e:
    print("❌ BME680 Error:", e)
    bme = None

# Inputs/Outputs
flame_sensor = Pin(2, Pin.IN)        # GP2
led_alarm = Pin(15, Pin.OUT)         # GP15

# Connect Wi-Fi
connect_wifi(SSID, PASSWORD)

# Main Loop
while True:
    oled.fill(0)
    try:
        # Sensor Readings
        if bme:
            temp = bme.temperature
            hum = bme.humidity
            gas = bme.gas
        else:
            temp = hum = gas = -1

        flame = flame_sensor.value() == 0  # LOW = flame detected

        # Alarm logic
        alarm_on = False
        if temp > TEMP_THRESHOLD:
            alarm_on = True
        if gas < GAS_THRESHOLD:
            alarm_on = True
        if flame:
            alarm_on = True
        if hum > HUMIDITY_THRESHOLD:
            alarm_on = True

        status_str = "ALARM" if alarm_on else "Safe"
        status_code = 0 if alarm_on else 1
        led_alarm.value(1 if alarm_on else 0)

        # OLED display
        oled.text("Temp: {:.1f}C".format(temp), 0, 0)
        oled.text("Hum: {:.1f}%".format(hum), 0, 10)
        oled.text("Gas: {:.0f}Ω".format(gas), 0, 20)
        oled.text("Flame: {}".format("Yes" if flame else "No"), 0, 30)
        oled.text("Status: {}".format(status_str), 0, 50)
        oled.show()

        # Console Log
        print("Temp: {:.2f}°C | Hum: {:.2f}% | Gas: {:.0f}Ω".format(temp, hum, gas))
        print("Flame:", "Yes" if flame else "No", "| Status:", status_str)
        print("-" * 40)

        # Upload to ThingSpeak
        send_to_thingspeak(THINGSPEAK_API_KEY, temp, hum, gas, int(flame), status_code)

        time.sleep(DELAY)

    except Exception as e:
        print("❌ Loop Error:", e)
        oled.fill(0)
        oled.text("Sensor Error!", 0, 0)
        oled.show()
        led_alarm.value(1)
        time.sleep(3)