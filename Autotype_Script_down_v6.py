# v6 DOWN

import time
import csv
import keyboard  # Importing keyboard library
from pynput import keyboard as kb_listener

# CSV file to read
csv_file = 'C:/Users/JoelTencer/Documents/autotype_down.csv'

# Global variable to track if the Escape key is pressed
escape_pressed = False

# Define listener to terminate script on Escape key press
def on_press(key):
    global escape_pressed
    if key == kb_listener.Key.esc:
        escape_pressed = True
        return False  # Stop the listener

# Start the keyboard listener
listener = kb_listener.Listener(on_press=on_press)
listener.start()

# Delay for ten seconds to switch to the desired window
time.sleep(10)

# Print don't close Window
print("Don't close this window until typing is finished")

# Print Press Esc to cancel
print("Press Esc to stop automatic typing")

# Open and read the CSV file with explicit encoding
with open(csv_file, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 3:
            print("Skipping row: Not enough columns")
            continue
        
        # Read columns
        first_column = row[0].strip()
        second_column = row[1].strip()
        third_column = row[2].strip()
        
        # Build the text to type with conditional spaces
        parts = []
        if first_column:
            parts.append(first_column)
        if second_column:
            parts.append(second_column)
        if third_column:
            parts.append(third_column)
        
        text_to_type = ' '.join(parts)
        
        # Check if the Escape key is pressed
        if escape_pressed:
            print("Escape key pressed. Exiting...")
            break
        
        # Type the line of text using the keyboard library
        keyboard.write(text_to_type)

        # Press the Down key to simulate typing
        keyboard.press_and_release('down')

        # Delay for a short interval between each line
        # time.sleep(2)

# Stop the keyboard listener
listener.stop()
