# Gas Detection Alarm System

The Gas Detection Alarm System is a Raspberry Pi-based project that aims to enhance safety by detecting the presence of harmful gases and alerting users in real-time. By utilizing a Raspberry Pi 3B, an I2C LCD1602 Module, and a Gas Sensor, this system provides an efficient and reliable solution for gas detection in various environments. The system detects the gas and dispays a relevant message on an LCD screen when the gas concentration exceeds a predefined threshold.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

1. **Gas Detection:** The primary function of the system is to detect the presence of gas in the surrounding environment. 

2. **Alarm System:** The I2C LCD1602 Module is used to display real-time information about the detected gas concentration. The system is equipped with a configurable threshold for gas concentration. When the detected gas concentration crosses this threshold, a relevant message is displayed on the LCD. 

## Technologies Used

- Raspberry Pi 3B
- I2C LCD1602 Module
- Gas Sensor

## Installation

1. Clone the repository: `git clone https://github.com/SINGHAJS/Gas-Detection-Alarm-System.git`
2. Connect the Gas Sensor and I2C LCD1602 Module to the Raspberry Pi 3B.
3. Open the project directory on the Raspberry Pi.
4. Open terminal in the project directory and enter `pipenv install`
5. In terminal enter `pipenv shell`
6. Once the virtual environment activates, enter `python3 src/main.py`

## Usage

Upon setting up and running the Gas Detection Alarm System, you'll interact with the following components:

1. **LCD Display:** The LCD screen will showcase real-time gas concentration information and provide visual feedback about the current air quality.

2. **Threshold Configuration:** Adjust the threshold for gas concentration based on your preferences and the specific gas you're monitoring.

3. **Alarm Notifications:** When the detected gas concentration exceeds the threshold, the system will trigger alarm. The visual warnings on the LCD screen will be activated.

4. **Data Analysis:** Access the logged data to review historical gas concentration trends and make informed decisions about the environment's safety.

By following these instructions, you can effectively set up and utilize the Gas Detection Alarm System to detect hazardous gas levels.
