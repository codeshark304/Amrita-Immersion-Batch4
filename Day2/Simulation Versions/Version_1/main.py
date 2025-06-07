from machine import Pin, ADC
import dht, utime

# Sensors
dht_sensor = dht.DHT22(Pin(15))  # DATA pin of DHT22 connected to GPIO15
mq2 = ADC(Pin(26))               # Analog gas sensor at GPIO26 (ADC0)
pir_sensor = Pin(14, Pin.IN)     # PIR motion sensor

# Thresholds
TEMP_THRESHOLD = 30     # Celsius
HUMIDITY_THRESHOLD = 70 # Percentage
GAS_THRESHOLD = 20000   # ADC value (adjust as needed)

def read_sensors():
    # Read temperature and humidity
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
    except:
        temp = None
        humidity = None

    # Read gas level
    gas_level = mq2.read_u16()

    # Read PIR motion
    motion = pir_sensor.value()

    return temp, humidity, gas_level, motion

def main():
    while True:
        temp, humidity, gas_level, motion = read_sensors()

        # Print sensor data
        print("=== Sensor Data ===")
        if temp is not None:
            print("Temperature: {:.1f} C".format(temp))
            if temp > TEMP_THRESHOLD:
                print("ALERT: High Temperature!")
        else:
            print("Temperature: ---")

        if humidity is not None:
            print("Humidity: {:.1f} %".format(humidity))
            if humidity > HUMIDITY_THRESHOLD:
                print("ALERT: High Humidity!")
        else:
            print("Humidity: ---")

        print("Gas Level: {}".format(gas_level))
        if gas_level > GAS_THRESHOLD:
            print("ALERT: Gas Leak Detected!")

        if motion:
            print("ALERT: Motion Detected!")
        else:
            print("Motion: No motion")

        print("====================\n")

        utime.sleep(2)

main()
