#-------------------------------------------------------------------------------
# Name:        StepsMotor
# Purpose:
#
# Author:      krthr <twilson@uninorte.edu.co>
#
# Created:     28/11/2018
# Copyright:   (c) twilson 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from movement_interface import MovementInterface

class StepsMotor(MovementInterface):

    def __init__(self, arduino_port, steps, dist):
        MovementInterface.__init__(self, arduino_port)
        self.STEPS_REV = steps * 1.0        # Pasos para dar una revolución
        self.DIST_REV = dist * 1.0          # Distancia que se recorre en una revolucion
        self.DIST_STEP = dist / (steps*1.0) # Distancia que se recorre por cada paso
        self.pos_actual = 0.0

        print arduino_port, steps, dist

    def move_to(self, b):
        dir = -1 if b - self.pos_actual < 0 else 1
        dist = abs(b - self.pos_actual)

        steps = int(round(dist / self.DIST_STEP, 0)) * dir

        # TODO: Calcular el numero de pasos para recorrer la distancia

        self.arduino.move_steps(steps).read_data()
        self.pos_actual += -dist if dir < 0 else dist

        print dir, dist, self.pos_actual, steps

    def update_pos(self, dist):
        self.pos_actual += -dist if self.dir < 0 else dist

motor = StepsMotor("COM4", steps=16*800, dist=8)
motor.move_to(24)
