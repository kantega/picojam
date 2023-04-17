from random import randint
from machine import Pin
from util import LCD, color_rgb
           

# 1
# Set up button pins.
# These are all instances of machine.Pin.
# See docs at https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin
btn_a = Pin(15, Pin.IN, Pin.PULL_UP) 
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

# 2
# Set up joystick pins.
# These are also machine.Pin instances.
joy_up = Pin(2, Pin.IN, Pin.PULL_UP)
joy_down = Pin(18, Pin.IN, Pin.PULL_UP)
joy_left = Pin(16, Pin.IN, Pin.PULL_UP)
joy_right = Pin(20, Pin.IN, Pin.PULL_UP)

# 3
# Initialise LCD. 
# This is a framebuf.FrameBuffer instance. See docs at: 
# https://docs.micropython.org/en/latest/library/framebuf.html
lcd = LCD() 

# 4
# Create some colors.
# color_rgb is a function from our utility library.
BLACK = color_rgb(0, 0, 0)
RED = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)

# 5
# Size of the display in pixels.
WIDTH = 240
HEIGHT = 240


# Position of green box
green_box_x = 70
green_box_y = 100


# Position of red box
red_box_x = 150
red_box_y = 100


while True:
    # Fill the screen with black color.
    lcd.fill(BLACK)

    # Display a nice banner.
    lcd.text('ABAKUS @ KANTEGA', 60, 60, RED)

    # Move the green box UP and DOWN on the screen if the joystick is UP or DOWN
    if joy_up.value() == 0:
        green_box_y -= 5
    if joy_down.value() == 0:
        green_box_y += 5
    # TODO 1: move green box LEFT or RIGHT if the joystick is LEFT or RIGHT

    # Add rectangle for green box to LCD
    lcd.fill_rect(green_box_x, green_box_y, 20, 50, GREEN)

    # Move the red box LEFT and RIGHT on the screen if X or Y is pressed
    if btn_x.value() == 0:
        red_box_x -= 5
    if btn_y.value() == 0:
        red_box_x += 5
    # TODO 2: move red box UP or DOWN if A or B is pressed

    # Add rectangle for red box to LCD
    lcd.fill_rect(red_box_x, red_box_y, 20, 50, RED)

    # Render everything to screen...
    lcd.show()
