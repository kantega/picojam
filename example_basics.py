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

# 5
# Size of the display in pixels.
WIDTH = 240
HEIGHT = 240


while True:
    # QUESTION: What happens if we don't call lcd.fill ?
    lcd.fill(BLACK)

    # Draw a random grid of blue rectangles.
    cell_size = 16 # 240/15 
    for x in range(0, WIDTH, cell_size):
        for y in range(0, HEIGHT, cell_size):
            c = color_rgb(0, 0, randint(0, 128))
            lcd.rect(x, y, cell_size, cell_size, c)

    # Display a nice banner.
    lcd.text('ABAKUS @ KANTEGA', 20, 150, RED)

    # Show state of the buttons.
    lcd.text('A=%d' % btn_a.value(),      20,  80, RED)
    lcd.text('B=%d' % btn_b.value(),      60,  80, RED)
    # TODO: Add the remaining two buttons. 

    # Show state of the joystick.
    lcd.text('UP=%d' % joy_up.value(),     20, 100, RED)
    # TODO: Add the remaining three directions.


    # QUESTION: What happens if we don't call lcd.show ?
    lcd.show()
