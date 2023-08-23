import RPi.GPIO as GPIO
import time

LED_RED_PIN = 20
LED_GREEN_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED_PIN, GPIO.OUT)
GPIO.setup(LED_GREEN_PIN, GPIO.OUT)
GPIO.output(LED_RED_PIN, GPIO.LOW)
GPIO.output(LED_GREEN_PIN, GPIO.LOW)

led_red = GPIO.PWM(LED_RED_PIN, 2000)
led_green = GPIO.PWM(LED_GREEN_PIN, 2000)

# Set default light state to off
led_red.start(0)
led_green.start(0)


# Function to change the light to red if high gas detected
def set_danger_alert_color(is_danger):
    if is_danger:
        led_red.ChangeDutyCycle(100)
        led_green.ChangeDutyCycle(0)


# Function to change the light to green if the gas is within the safe params
def set_safe_alert_color(is_safe):
    if is_safe:
        led_green.ChangeDutyCycle(100)
        led_red.ChangeDutyCycle(0)


# Release all the resouces used by the dual color lcd
def release_dual_color_led_resources():
    led_green.stop()
    led_red.stop()
    GPIO.cleanup()