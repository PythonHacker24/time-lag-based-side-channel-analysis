// Define the pin connected to the LED
const int ledPin = D0;

// Define the correct password
const String password = "password";

void setup() {
  // Set the LED pin as output
  pinMode(ledPin, OUTPUT);

  // Start serial communication at 9600 baud
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read from serial
  if (Serial.available() > 0) {
    // Read the data from serial
    String input = Serial.readStringUntil('\n');
    input.trim(); // Remove leading and trailing whitespace
    
    // // Check if the input matches the password
    // if (input.equals(password)) {
    //   Serial.println("Correct password entered. Turning on the LED.");
    //   digitalWrite(ledPin, HIGH); // Turn on the LED
    // } else {
    //   Serial.println("Incorrect password. Please try again.");
    // }

    bool correctPassword = true;

    for (int i = 0; i < input.length(); i++) {
      // Check if the characters at the corresponding positions are not equal
      if (input.charAt(i) != password.charAt(i)) {
        correctPassword = false;
        break; // Break out of the loop since the password is incorrect
      }
    }

    if (correctPassword) {
      Serial.println("Correct password entered. Turning on the LED.");
      digitalWrite(ledPin, HIGH); // Turn on the LED
    } else {
      Serial.println("Incorrect password. Please try again.");
    }
  }
}
