import network
import urequests
import machine
import time
import dht
from machine import I2C, Pin, ADC
import ssd1306

# Wi-Fi credentials
WIFI_SSID = 'Wokwi-GUEST'
WIFI_PASSWORD = ''

# ThingSpeak credentials
THINGSPEAK_API_KEY = 'T4Y0V15NW5KMMWJL'

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print("Connected:", wlan.ifconfig())

connect_wifi()

# OLED setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Sensors setup
dht_sensor = dht.DHT22(Pin(15))
mq2 = ADC(Pin(26))               # Analog MQ2 gas sensor at GPIO26 (ADC0)
pir_pin = Pin(17, Pin.IN)        # PIR motion sensor
buzzer = Pin(16, Pin.OUT)

# Thresholds
TEMP_THRESHOLD = 35.0
HUMIDITY_THRESHOLD = 80.0
GAS_THRESHOLD = 60000  # ADC value threshold (adjust as needed)

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        gas_level = mq2.read_u16()
        motion_detected = pir_pin.value()

        # Determine if gas alert should trigger
        gas_alert = gas_level > GAS_THRESHOLD

        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Gas: {}".format("HIGH" if gas_alert else "NORMAL"))
        print("Motion Detected:", motion_detected)

        # OLED display
        oled.fill(0)
        oled.text("Temp: {:.1f} C".format(temp), 0, 0)
        oled.text("Humidity: {:.1f}%".format(humidity), 0, 12)
        oled.text("Gas: {}".format("HIGH" if gas_alert else "NORMAL"), 0, 24)
        oled.text("Motion: {}".format("YES" if motion_detected else "No"), 0, 36)

        if (temp > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD or gas_alert or motion_detected):
            buzzer.on()
            oled.text("ALERT!", 0, 48)
        else:
            buzzer.off()
            oled.text("Safe", 0, 48)

        oled.show()

        # Send data to ThingSpeak
        url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}&field5={}".format(
            THINGSPEAK_API_KEY, temp, humidity, gas_level, motion_detected, int(gas_alert))
        response = urequests.get(url)
        response.close()

    except Exception as e:
        print("Error:", e)
        buzzer.off()

    time.sleep(15)  # ThingSpeak allows one update every 15 seconds