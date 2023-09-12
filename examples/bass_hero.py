from random import randint
from machine import Pin
from util import LCD, color_rgb

# Set up button pins
btn_a = Pin(15, Pin.IN, Pin.PULL_UP) 
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

# Initialise LCD
lcd = LCD() 

# Set up colors
BLACK = color_rgb(0, 0, 0)
RED = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)
BLUE = color_rgb(0, 0, 255)

# Static positions and sizes
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240
LINE_POS = 200
LINE_WIDTH = 20
RECT_WIDTH = 20
BUTTON_DIST = 60

BUTTONS = [btn_a, btn_b, btn_x, btn_y]
NUM_OF_BUTTONS = len(BUTTONS)

def get_rand_note_length():
    return randint(RECT_WIDTH, RECT_WIDTH * 4)

# Notes
POSITIONS = [randint(-SCREEN_WIDTH, 0)] * NUM_OF_BUTTONS
LENGTHS = [get_rand_note_length()] * NUM_OF_BUTTONS
COLORS = [BLUE] * NUM_OF_BUTTONS

points = 0

while True:
    lcd.fill(BLACK)

    # Draw a cool grid of blue rectangles
    cell_size = 16 # 240/15
    for x in range(0, SCREEN_WIDTH, cell_size):
        for y in range(0, SCREEN_HEIGHT, cell_size):
            c = color_rgb(0, 0, randint(0, 128))
            lcd.rect(x, y, cell_size, cell_size, c)

    # Display banner and points
    lcd.text('ONLINE @ KANTEGA', 10, 10, RED)
    lcd.text('POINTS:%d' % points, 10, 20, RED)
    
    # Line that holds buttons
    lcd.rect(LINE_POS, 0, LINE_WIDTH, SCREEN_WIDTH, RED)
    
    for i in range(NUM_OF_BUTTONS):
        # Reset note position if offscreen
        if POSITIONS[i] >= SCREEN_WIDTH:
            POSITIONS[i] = randint(-SCREEN_WIDTH, 0)
            LENGTHS[i] = get_rand_note_length()
            COLORS[i] = BLUE
        
        # Render note
        POSITIONS[i] += 5
        lcd.rect(POSITIONS[i], RECT_WIDTH + i * BUTTON_DIST, LENGTHS[i], RECT_WIDTH, COLORS[i])
        
        button_pos = RECT_WIDTH + i * BUTTON_DIST
        # Button not clicked
        if BUTTONS[i].value():
            lcd.rect(LINE_POS, button_pos, RECT_WIDTH, RECT_WIDTH, RED)
            
            # Note passed by line without being hit
            if POSITIONS[i] >= LINE_POS + RECT_WIDTH and COLORS[i] != GREEN:
                COLORS[i] = RED
                points -= 1
        # Button clicked
        else:                        
            # Note was hit
            if POSITIONS[i] + LENGTHS[i] >= LINE_POS and POSITIONS[i] <= LINE_POS + LINE_WIDTH:
                COLORS[i] = GREEN
                lcd.rect(LINE_POS, button_pos, RECT_WIDTH, RECT_WIDTH, GREEN)
                points += 1
            # Clicking button but not on note
            else:
                lcd.rect(LINE_POS, button_pos, RECT_WIDTH, RECT_WIDTH, BLUE)
                points -= 1

    lcd.show()
