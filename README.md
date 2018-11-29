# Movement Controller

Estandarización de la cinemática y control de diferentes formas de movimiento.

## - Motor paso-a-paso
Controlar un motor paso a paso.

### ArduinoController [arduino_controller/arduino_controller.ino]
El controlador de Arduino recibe el número de pasos que debe dar y cuando los realiza escribe por `Serial`: "done".
### PythonController [arduino_controller/python_controller.py]
Módulo encargado de la comunicación vía `Serial` con el arduino.

```python
arduino = PythonController("COM5", 3)   # Crear una nueva instancia, pasando como parámetros el puerto y el _timeout_ (en segundos)
arduino.move_steps(400).read_data()  # Enviar 400 pasos y esperar respuesta del arduino
arduino.close() # Cerrar conexión
```



### StepsMotor [steps_motor.py]
