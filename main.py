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
RED   = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)
BLUE  = color_rgb(0, 0, 255)
YELLOW = color_rgb(255, 255, 0)


# 5
# Size of the display in pixels.
WIDTH = 240
HEIGHT = 240




# 6
# Position of green box.
green_box_x = 70
green_box_y = 100

# 7
# Position of red box.
red_box_x = 150
red_box_y = 100

# 8
# Position of bouncing ball.
bouncing_ball_x = 42
bouncing_ball_y = 0

# 9
# Speed of bouncing ball
bouncing_ball_vx = 2
bouncing_ball_vy = 3



while True:
    #
    # CLEAR SCREEN AND ADD BANNER
    #

    # Fill the screen with black color.
    lcd.fill(BLACK)

    # Display a nice banner.
    lcd.text('GAMEJAM @ KANTEGA', 60, 60, BLUE)
    # TODO 0:
    # Change the banner so it includes your name!

    #
    # GREEN BOX
    #

    # Move green box UP and DOWN on the screen if the joystick is UP or DOWN.
    if joy_up.value() == 0:
        green_box_y -= 5
    if joy_down.value() == 0:
        green_box_y += 5

    # TODO 1:
    # Add code for moving the green box LEFT or RIGHT if the joystick is LEFT or RIGHT.

    # Draw green box.
    lcd.fill_rect(green_box_x, green_box_y, 20, 50, GREEN)


    #
    # RED BOX
    #

    # TODO 2:
    # Add code for moving the red box using buttons X, Y, A, B (btn_x, btn_y, btn_a, btn_b)

    # Draw red box.
    lcd.fill_rect(red_box_x, red_box_y, 20, 50, RED)


    #
    # BOUNCING BALL
    #

    bouncing_ball_x += bouncing_ball_vx
    bouncing_ball_y += bouncing_ball_vy
    if bouncing_ball_x < 0 or bouncing_ball_x >= WIDTH:
        bouncing_ball_vx *= -1
    if bouncing_ball_y < 0 or bouncing_ball_y >= HEIGHT:
        bouncing_ball_vy *= -1
    lcd.pixel(bouncing_ball_x, bouncing_ball_y, YELLOW)

    # TODO 3:
    # Change the color of the text "GAMEJAM @ KANTEGA" to YELLOW for 5 frames every time the bouncing ball hits a wall.
    #
    # Tip: Set a variable flash_frames_remaining = 5 when the ball hits the wall, and use it to
    # determine which color to use in the call to lcd.text...


    #
    # FINAL DRAWING
    #

    # Render everything to screen...
    lcd.show()
