######### Python Code To Control Display Brightness ##########

import screen_brightness_control as sbc

"""
Adjust screen brightness.
level: Brightness level (integer between 0 and 100)
"""

def set_brightness(level):
    try:
        # Set the brightness
        sbc.set_brightness(level)
        print(f"Screen brightness set to {level}%")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
new_brightness = int(input("Enter brightness level (0-100): "))
set_brightness(new_brightness)
