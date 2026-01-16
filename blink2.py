from machine import Pin
import time
# ڕێکخستنی LED (GP25 کە LEDی ناوخۆیی پیکۆیە)
LED_PIN = 25  # GP25 for Raspberry Pi Pico (built-in LED)
# دانانی LED وەک دەرچوون
led = Pin(LED_PIN, Pin.OUT)
def setup():
    """دانانی سەرەتایی"""
    print("LED Blink Program Started")
    print("Built-in LED on GP25")
def loop():
    """لووبی سەرەکی"""
    # ڕووناککردنی LED
    led.value(1)  # Equivalent to digitalWrite(LED_PIN, HIGH)
    print("LED ON")
    time.sleep(1)  # Wait for 1 second (equivalent to delay(1000))
    # خاموشکردنی LED
    led.value(0)  # Equivalent to digitalWrite(LED_PIN, LOW)
    print("LED OFF")
    time.sleep(1)  # Wait for 1 second (equivalent to delay(1000))
# ڕێکخستنی سەرەتایی
setup()
# لووبی سەرەکی
while True:
    loop()
