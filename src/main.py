import threading
from gas_sensor import start_gas_analysis_process
from dual_color_led import start_dual_color_led

# Create gas sensor and dual color led threads
gas_sensor_thread = threading.Thread(target=start_gas_analysis_process)
dual_color_led_thread = threading.Thread(target=start_dual_color_led)

# Start the threads
gas_sensor_thread.start()
dual_color_led_thread.start()

# Stop the threads
gas_sensor_thread.join()
dual_color_led_thread.join()
