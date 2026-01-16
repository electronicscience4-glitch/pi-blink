const int LED_PIN = 25; // GP25 for Raspberry Pi Pico (built-in LED)

void setup() {
 pinMode(LED_PIN, OUTPUT);
}
void loop() {
 //Turn LED ON
digitalWrite(LED_PIN, HIGH);// Equivalent to led.value(1)
delay(50);//Wait for 1 second
 
//Turn LED OFF
digitalWrite(LED_PIN, LOW);// Equivalent to led.value(0)
delay(50);// Wait for 1 second
}
