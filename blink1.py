import machine
import utime

# دانانی پین 25 وەک دەرچوو بۆ لیدی ناوەندی
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.on()          # لیدی تروکە
    utime.sleep(0.1)    # بوەستە بۆ ١ چرکە
    led.off()         # لیدی کوژە
    utime.sleep(0.1)    # بوەستە بۆ ١ چرکە
    
    