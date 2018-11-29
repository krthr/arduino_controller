//-------------------------------------------------------------------------------
// Name:        Arduino Controller
// Purpose:
//
// Author:      twilson <twilson@uninorte.edu.co>
//
// Created:     27/11/2018
// Copyright:   (c) twilson 2018
// Licence:     <your licence>
//-------------------------------------------------------------------------------

#include <Stepper.h>
#define MOTOR_STEPS 200
#define SPEED 200
Stepper motor(16 * MOTOR_STEPS, 3, 4);

void setup() {
  Serial.begin(9600);
  motor.setSpeed(SPEED);
}

void loop() {
  if (Serial.available()) {
    long stepsToMove = Serial.parseInt();
    if (stepsToMove) {      
      motor.step(stepsToMove);
      Serial.print("done\n");
    }
  }
}
