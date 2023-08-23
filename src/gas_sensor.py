from adafruit_pcf8591.pcf8591 import PCF8591
import RPi.GPIO as GPIO
import time
import board
import busio
from lcd import update_gas_alarm_status


DO = 17  # Digital Output: 17
GPIO.setmode(GPIO.BCM)  # Set GPIO mode to use BCM number scheme


# Analyse gas
def analyse_gas(pcf):
    prev_gas_value = 0

    while True:
        # Read gas value PCF8591 ADC in %
        current_gas_value = ((pcf.read(0) / 255) * 100)
        # Printing current gas value
        print(f'CURRENT GAS READING: {current_gas_value}')

        if current_gas_value != prev_gas_value:  # Gas value has changed
            # Validate gas value and update LCD display message
            update_gas_alarm_status(current_gas_value)
            # Set previous gas value to the current gas value
            prev_gas_value = current_gas_value

        time.sleep(0.5)


# Releases resources used by GPIO
def release_gpio():
    GPIO.cleanup()  # Release resources used by GPIO


# Main process
def start_gas_analysis_process():
    try:
        # Initialize communication with SCL and SDA pins
        i2c = busio.I2C(board.SCL, board.SDA)
        pcf = PCF8591(i2c)  # Create instance of PCF8591
        GPIO.setup(DO, GPIO.IN)
        analyse_gas(pcf)  # Starts analysing the gas
    except KeyboardInterrupt:
        release_gpio()
    finally:
        release_gpio()
