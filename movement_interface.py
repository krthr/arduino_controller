#-------------------------------------------------------------------------------
# Name:        MovementInterface
# Purpose:
#
# Author:      krthr <twilson@uninorte.edu.co>
#
# Created:     28/11/2018
# Copyright:   (c) twilson 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.path.append("./arduino_controller")
from python_controller import PythonController

class MovementInterface():

    def __init__(self, arduino_port):
        self.arduino = PythonController(arduino_port, 3)
