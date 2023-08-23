from rpi_lcd import LCD

lcd = LCD() # Create LCD instance

# Function to update the status of gas alarm on LCD screen
def update_gas_alarm_status(gas_value):
    
    # Display relevant message based on the gas level 
    if gas_value > 45 :
        lcd.text('WARNING HIGH GAS', 1)
    else:
        lcd.text('SAFE GAS LEVEL', 1) 


lcd.clear() # Clear LCD screen