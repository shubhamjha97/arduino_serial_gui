# arduino_serial_gui

A simple python program that provides a GUI to control an Arduino via Serial.

### Files-
1. serial_led_gui.ino- Arduino code that accepts commands over Serial comminucation.
2. gui.py- A simple Tkinter based GUI.
3. controller.py- Python program to control the Arduino.

### Classes-
1. component- Provides functions for connecting to the Arduino and controlling different components connected to it.

### How to use-
1. Upload the 'serial_led_gui' sketch onto your arduino board.
2. Make sure that the Arduino is connected to your PC and run 'gui.py'.

### Further improvements-
1. Add support for multiple components such as motors, servos, etc.
2. Add a dashboard to visualize and log sensor data. 
