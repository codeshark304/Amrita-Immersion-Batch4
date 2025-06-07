import machine
import time
import dht
from machine import I2C, Pin, ADC
import ssd1306

# OLED setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# DHT22 sensor
dht_sensor = dht.DHT22(Pin(15))

# MQ2 gas sensor (digital pin)
mq2 = ADC(Pin(26))      

# PIR motion sensor
pir_pin = Pin(17, Pin.IN)

# Buzzer
buzzer = Pin(16, Pin.OUT)

# Thresholds
TEMP_THRESHOLD = 35.0
HUMIDITY_THRESHOLD = 80.0
GAS_THRESHOLD = 60000.0

while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        gas_level = mq2.read_u16()
        motion_detected = pir_pin.value()

        gas_alert = gas_level > GAS_THRESHOLD

        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Gas: {}".format("HIGH" if gas_alert else "NORMAL"))
        print("Motion Detected:", motion_detected)

        # Clear OLED
        oled.fill(0)

        # Show sensor values
        oled.text("Temp: {:.1f} C".format(temp), 0, 0)
        oled.text("Humidity: {:.1f}%".format(humidity), 0, 12)
        oled.text("Gas: {}".format("HIGH" if gas_alert else "NORMAL"), 0, 24)
        oled.text("Motion: {}".format("YES" if motion_detected else "No"), 0, 36)

        # Trigger alarm if motion + (any danger condition)
        if (temp > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD or gas > GAS_THRESHOLD or motion_detected):
            buzzer.on()
            oled.text("ALERT!", 0, 48)
            print("Alert!!")
        else:
            buzzer.off()
            oled.text("Safe", 0, 48)

        oled.show()

    except Exception as e:
        print("Error:", e)
        buzzer.off()

    time.sleep(2)
