# Day 2 – Sensor Integration & IoT Prototyping

Welcome to the Day 2 folder of our internship repository. Today, we focused on building a microcontroller-based sensor monitoring system using Wokwi Simulator and the Raspberry Pi Pico W. We progressively developed the project through three versions, each adding a new layer of complexity.

---

## Overview

The goal was to simulate a hazardous environment monitoring system by integrating the following sensors:

-  *DHT22* – Temperature & Humidity
-  *MQ2* – Gas detection
-  *PIR Sensor* – Motion detection
-  *SSD1306 OLED* – Data visualization
-  *ThingSpeak API* – Cloud data logging (in Version 3)

---

## Project Versions

###  *Version 1: Basic Sensor Output*
- Reads data from DHT22, MQ2, and PIR sensors
- Prints the values to the serial monitor
- No display or cloud integration
- Useful for testing raw sensor outputs



---

###  *Version 2: OLED Display Integration*
- Adds I2C SSD1306 OLED display
- Displays temperature, humidity, gas status, and motion detection
- Buzzer triggers in case of unsafe readings


---

###  *Version 3: Cloud Integration with ThingSpeak*
- All features of Version 2 retained
- Real-time sensor values are sent to ThingSpeak using an API key
- Simulates a real-world IoT dashboard environment


---

##  Tech Stack

- *Microcontroller:* Raspberry Pi Pico W (RP2040)
- *View the Simulation here:** [Wokwi Simulator](https://wokwi.com/projects/433087745117047809)
- *Programming Language:* MicroPython
- *Cloud:* ThingSpeak API for data logging
- *Display:* SSD1306 OLED (128x64)
