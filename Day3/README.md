#  Day 3 – Hardware Simulation & Cloud Integration 


---

##  Overview

On Day 3, we successfully **completed the hardware simulation** of our hazardous environment monitoring system using the **Raspberry Pi Pico W**. We integrated key components like environmental and flame sensors, OLED display, and LED alarm. The system sends real-time data to **ThingSpeak**, enabling safety alerts based on environmental thresholds.

---

##  Components Used

| Component           | Description                              |
|---------------------|------------------------------------------|
| Raspberry Pi Pico W | Microcontroller with Wi-Fi support       |
| BME680              | Environmental sensor (Temp, Humidity, Gas) |
| IR Flame Sensor     | Detects presence of flame                |
| SSD1306 OLED        | 128x64 OLED for data display             |
| LED                 | Alarm indicator                          |
| ThingSpeak          | IoT cloud platform for data visualization|

---

##  Circuit Diagram

![Circuit Diagram](https://github.com/user-attachments/assets/68ded8c7-f200-4a9a-9a8d-12cc1bad6c99)


**GPIO Mappings:**

- `GP0 (SDA)` and `GP1 (SCL)` → I2C for BME680 and OLED  
- `GP2` → Flame sensor input  
- `GP15` → LED alarm output

---

##  Program Logic

1. Connects to Wi-Fi using Pico W.
2. Initializes sensors and OLED.
3. Continuously reads temperature, humidity, gas resistance, and flame presence.
4. Displays data on OLED.
5. Triggers LED alarm if any value crosses defined hazard thresholds.
6. Sends data to ThingSpeak for cloud-based monitoring.

---

##  Threshold Settings

| Parameter   | Threshold    | Condition                        |
|-------------|--------------|----------------------------------|
| Temperature | > 35°C       |  High heat warning               |
| Humidity    | > 80%        |  Excess moisture warning         |
| Gas         | < 60,000 Ω   |  Gas contamination danger        |
| Flame       | Detected     |  Fire hazard                     |

If any hazard is detected, the **LED turns ON** and **OLED shows ALERT**.

---

##  ThingSpeak Integration

| Field | Data             |
|-------|------------------|
| 1     | Temperature (°C) |
| 2     | Humidity (%)     |
| 3     | Gas Resistance (Ω) |
| 4     | Flame (0 = No, 1 = Yes) |
| 5     | Safety Status (0 = ALARM, 1 = Safe) |

Real-time sensor values are sent to ThingSpeak every 15 seconds.

---

##  Files in the Folder

- `feeds_from_ThingSpeak.csv` – Logged data from ThingSpeak.
- `synthetic_generated_7_days.csv` – Expanded dataset for ML training.
- `demo_video.mp4` – Working demo of simulation.
- `main.py` – Full MicroPython script for the project.




> © 2025 – Hazardous Environment Monitoring using Raspberry Pi Pico W | Powered by MicroPython & ThingSpeak
