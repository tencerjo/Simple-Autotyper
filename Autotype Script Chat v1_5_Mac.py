# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import pyautogui
from pynput import keyboard

# Define listener to terminate script on Escape key press
# Global variable to track if the Escape key is pressed
escape_pressed = False

def on_press(key):
    global escape_pressed
    if key == keyboard.Key.esc:
        escape_pressed = True
        return False  # Stop the listener
    
#define on release, is this necessary?
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
def type_text_from_file(file_path):
    with open(file_path, 'r') as file:
        # Delay for a few seconds to switch to the desired window
        time.sleep(3)

        # Start the keyboard listener
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

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
            
            # Press the Enter key to simulate typing
            pyautogui.press('enter')

            # Delay for a short interval between each line
            time.sleep(0.5)

        # Stop the keyboard listener
        listener.stop()

# Example usage
text_file = 'C:\Users\joelt\OneDrive\Documents.txt'
type_text_from_file(text_file)
