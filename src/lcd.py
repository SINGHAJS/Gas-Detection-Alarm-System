from rpi_lcd import LCD
import time
import threading
from dual_color_led import set_safe_alert_color, set_danger_alert_color

lcd = LCD() # Create LCD instance
UPPER_GAS_LIMIT = 50 # Set to 50% for testing purposes

safe_message_thread = None
danger_message_thread = None

def start_safe_message_thread():
    global safe_message_thread
    safe_message_thread = threading.Thread(target=display_safe_message)
    safe_message_thread.start()


def start_danger_message_thread():
    global danger_message_thread
    danger_message_thread = threading.Thread(target=display_danger_message)
    danger_message_thread.start()

def display_safe_message():
    while True : 
        lcd.text('SAFE GAS LEVEL', 1)
        time.sleep(2)
        lcd.text('No Gas Detected', 1)            
        time.sleep(2)


def display_danger_message():
    while True: 
        lcd.text('WARNING! HIGH', 1)
        time.sleep(2)
        lcd.text('Gas Detected!', 1)            
        time.sleep(2)

# Function to update the status of gas alarm on LCD screen
def update_gas_alarm_status(gas_value):
    global safe_message_thread, danger_message_thread
    
    # Display relevant message based on the gas level 
    if gas_value > UPPER_GAS_LIMIT :
        lcd.text('WARNING HIGH GAS', 1)
        set_danger_alert_color(True)
        set_safe_alert_color(False)

        if safe_message_thread and safe_message_thread.is_alive():
            safe_message_thread.join()

        if danger_message_thread and not danger_message_thread.is_alive():
            start_danger_message_thread()

    else:
        lcd.text('SAFE GAS LEVEL', 1)
        set_safe_alert_color(True) 
        set_danger_alert_color(False)

        if danger_message_thread and danger_message_thread.is_alive():
            danger_message_thread.join()

        if safe_message_thread and not safe_message_thread.is_alive():
            start_safe_message_thread()


lcd.clear() # Clear LCD screen
