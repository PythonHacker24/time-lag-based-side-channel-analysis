const int ledPin = D1;

const String password = "pbcdefghi";

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim(); 

    bool correctPassword = true;

    if (input.length() != password.length()) {
        correctPassword = false;
        Serial.println("Length error");
    } else {
      for (int i = 0; i < input.length(); i++) {
        if (input.charAt(i) != password.charAt(i)) {
          correctPassword = false;
          break; 
        }
      }
    }

    if (correctPassword) {
      Serial.println("Correct password entered. Turning on the LED.");
      digitalWrite(ledPin, HIGH); 
    } else {
      Serial.println("Incorrect password. Please try again.");
    }
  }
}
