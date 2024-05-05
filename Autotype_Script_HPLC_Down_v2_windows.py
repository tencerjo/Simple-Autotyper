# -*- coding: utf-8 -*-

import time
import pyautogui
from pynput import keyboard

# Text file to read
text_file = 'C:/Users/JoelTencer/Documents/autotype_HPLC.txt'

# Global variable to track if the Escape key is pressed
escape_pressed = False

# Define listener to terminate script on Escape key press
def on_press(key):
    global escape_pressed
    if key == keyboard.Key.esc:
        escape_pressed = True
        return False  # Stop the listener

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Delay for a few seconds to switch to the desired window
time.sleep(6)

# Print don't close Window
print("Don't close this window until typing is finished")

# Print Press Esc to cancel
print("Press Esc to stop automatic typing")

# Open and read the text file
with open(text_file, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Remove any leading or trailing whitespace
        line = line.strip()

        # Check if the Escape key is pressed
        if escape_pressed:
            print("Escape key pressed. Exiting...")
            break

        # Type the line of text
        pyautogui.write(line)

        # Press the Down key to simulate typing
        pyautogui.press('down')

        # Delay for a short interval between each line
        # time.sleep(0.5)

# Stop the keyboard listener
listener.stop()
