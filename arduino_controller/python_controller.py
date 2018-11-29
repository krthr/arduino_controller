#-------------------------------------------------------------------------------
# Name:        Arduino Controller
# Purpose:
#
# Author:      krthr <twilson@uninorte.edu.co>
#
# Created:     27/11/2018
# Copyright:   (c) twilson 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import serial, time

class PythonController():
    """PythonController.
        Comunicate with Arduino, sending the steps.
    """

    def __init__(self, port, timeout=5):
        self.arduino = serial.Serial(port, timeout=timeout)
        time.sleep(2)
        self.done = False

    def move_steps(self, data):
        """Send steps to the Arduino
        """
        self.done = False
        self.arduino.write(b"{}".format(data))

        return self

    def read_data(self):
        """Read data from the serial
        """

        while self.arduino.inWaiting() == 0:
            pass

        self.last_reading = self.arduino.readline()
        self.done = self.last_reading.find("done") != -1

    def close(self):
        """Close the Serial connection
        """
        self.arduino.close()

if __name__ == "__main__":
    controller = PythonController("COM5", 3)

    for i in range(1, 6):
        controller.move_steps(i * 100).read_data()

    controller.close()

