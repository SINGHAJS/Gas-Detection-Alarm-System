# Gas Detection Alarm System

The Gas Detection Alarm System is a Raspberry Pi-based project that aims to enhance safety by detecting the presence of harmful gases and alerting users in real-time. By utilizing a Raspberry Pi 3B, an I2C LCD1602 Module, a Dual Color LED and a Gas Sensor, this system provides an solution for gas detecting gas in various environments. The system detects the gas and dispays a relevant message on an LCD screen when the gas concentration exceeds a predefined threshold along with switching the LED color from green to red.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

1. **Gas Detection:** The primary function of the system is to detect the presence of gas in the surrounding environment. 

2. **Alarm System:** The I2C LCD1602 Module is used to display real-time information about the detected gas. The system is equipped with a configurable threshold for gas concentration. When the detected gas concentration crosses this threshold, a relevant message is displayed on the LCD and the LED light changes accordingly. 

## Technologies Used

- Raspberry Pi 3B
- I2C LCD1602 Module
- Gas Sensor
- Dual Color LED

## Installation

1. Clone the repository: `git clone https://github.com/SINGHAJS/Gas-Detection-Alarm-System.git`
2. Connect the Gas Sensor and I2C LCD1602 Module to the Raspberry Pi 3B.
3. Open the project directory on the Raspberry Pi.
4. Open terminal in the project directory and enter `pipenv install`
5. In terminal enter `pipenv shell`
6. Once the virtual environment activates, enter `python3 src/main.py`

## Usage

Upon setting up and running the Gas Detection Alarm System, you'll interact with the following components:

1. **LCD Display:** The LCD screen will provide visual feedback about the current air quality. If the gas level is low, it will display "SAFE GAS LEVEL" and if it is high, it will display "WARNING HIGH GAS".

2. **Threshold Configuration:** Adjust the threshold for gas concentration based on your preferences and the specific gas you're monitoring.

3. **LED Light Indication:** When the detected gas concentration exceeds the threshold, the system will change the colour of the LED light. When the gas is in safe level, the LED light is green. When the gas level exceeds the safe level, the ligth switches to red.

By following these instructions, you can effectively set up and utilize the Gas Detection Alarm System to detect hazardous gas levels.
