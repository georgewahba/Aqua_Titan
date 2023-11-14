# Aqua Titan Project

Welcome to the Aqua Titan project! This project involves setting up various components for an aquaponics system. Follow the instructions below to configure and run each module.

## Connections

- GPS: Connect to the UART port.
- LED: Connect LEDs to D5 and D16 ports.
- Servo: Connect servo to the PWM port.
- Moisture Sensor: Connect to A0 port.

## Project Directory

Navigate to the project directory using the following command:

```bash
cd documents/aqua_titan

sudo su

python3 gps.py

python3 led.py

python3 moisture.py 0

python3 servo.py 12
