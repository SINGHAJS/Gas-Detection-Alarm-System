from rpi_lcd import LCD
from dual_color_led import set_safe_alert_color, set_danger_alert_color

lcd = LCD() # Create LCD instance

# Function to update the status of gas alarm on LCD screen
def update_gas_alarm_status(gas_value):
    
    # Display relevant message based on the gas level 
    if gas_value > 45 :
        lcd.text('WARNING HIGH GAS', 1)
        set_danger_alert_color(True)
        set_safe_alert_color(False)
    else:
        lcd.text('SAFE GAS LEVEL', 1)
        set_safe_alert_color(True) 
        set_danger_alert_color(False)


lcd.clear() # Clear LCD screen