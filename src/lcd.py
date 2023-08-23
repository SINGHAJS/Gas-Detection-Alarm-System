from rpi_lcd import LCD
import time
import threading
from dual_color_led import set_safe_alert_color, set_danger_alert_color

lcd = LCD() # Create LCD instance


def display_safe_message(flg):
    while flg: 
        lcd.text('SAFE GAS LEVEL', 1)
        time.sleep(2)
        lcd.text('No Gas Detected', 1)
        time.sleep(2)


def display_danger_message(flg):
    while flg: 
        lcd.text('WARNING! HIGH', 1)
        time.sleep(2)
        lcd.text('Gas Detected!', 1)
        time.sleep(2)

# Function to update the status of gas alarm on LCD screen
def update_gas_alarm_status(gas_value):
    
    # Display relevant message based on the gas level 
    if gas_value > 45 :
        lcd.text('WARNING HIGH GAS', 1)
        set_danger_alert_color(True)
        set_safe_alert_color(False)
        # display_safe_message(True)
        # display_danger_message(False)
        # danger_message_thread = threading()

    else:
        lcd.text('SAFE GAS LEVEL', 1)
        set_safe_alert_color(True) 
        set_danger_alert_color(False)
        # display_safe_message(True)
        # display_danger_message(False)







lcd.clear() # Clear LCD screen
