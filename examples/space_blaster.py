from random import randint
from machine import Pin
from util import LCD, color_rgb, detect_collision
from array import array
    
# Space Blaster game
# Example game for the Kantega Pico Pi Game Jam
# by Espen Hjertø
    

# Button pins
btn_a = Pin(15, Pin.IN, Pin.PULL_UP) 
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

# Joystick pins
joy_up = Pin(2, Pin.IN, Pin.PULL_UP)
joy_down = Pin(18, Pin.IN, Pin.PULL_UP)
joy_left = Pin(16, Pin.IN, Pin.PULL_UP)
joy_right = Pin(20, Pin.IN, Pin.PULL_UP)

# Init LCD
lcd = LCD()
WIDTH = 240
HEIGHT = 240

# Colors
BLACK = color_rgb(0, 0, 0)
RED = color_rgb(255, 0, 0)
STAR_BLUE = color_rgb(230,230,250)
LASER = color_rgb(255,200,200)
ASTEROID = color_rgb(230,230,230)
WHITE = color_rgb(255,255,255)

# Init variables
ship_speed = 5
torpedo_speed = 20
score = 0
game_over = False
level = 1
level_inc = 1

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 100
        self.poly = array('h',[0,0, 15, 5, 0, 5])
    
    def move(self):
        if (joy_up.value() == 0):
            self.y -= ship_speed
        if (joy_down.value() == 0):
            self.y += ship_speed
        if (joy_left.value() == 0):
            self.x -= ship_speed
        if (joy_right.value() == 0):
            self.x += ship_speed
            
        if (self.y < 0):
            self.y = 0
        if (self.y > 235):
            self.y = 235
        if (self.x < 0):
            self.x = 0
        if (self.x > 230):
            self.x = 230 
        
    def draw(self):
        lcd.poly(self.x, self.y, self.poly, 0x999ff, True)
        
        
class Torpedo():
    def __init__(self, ship):
        self.x = ship.x
        self.y = ship.y +4
        
    def move(self):
        self.y += torpedo_speed
            
class Torpedoes():
    def __init__(self):
        self.torpedoes = []
        self.shot_fired = 0
        
    def move(self):
        active_torpedoes = len(self.torpedoes)
        if (active_torpedoes == 0):
            return
        for i in range(active_torpedoes):
            t = self.torpedoes.pop(0)
            t.x += torpedo_speed
            if (t.x < 240):
                self.torpedoes.append(t)
            
    def shoot(self, ship):
        self.shot_fired -= 1
        
        if (btn_a.value() == 0 and self.shot_fired < 0):
            self.torpedoes.append(Torpedo(ship))
            self.shot_fired = 2
        
    def draw(self):
        for t in self.torpedoes:
            lcd.line(t.x, t.y, t.x  + torpedo_speed, t.y, LASER)
            lcd.line(t.x, t.y +3, t.x  + torpedo_speed, t.y +3, LASER)
        
class Star():
    def __init__(self):
        self.x = randint(0, 239)
        self.y = randint(0, 239)
        self.speed = randint(1, 4)
    
class Starfield():
    def __init__(self):
        self.stars = []
        for x in range(100):
            self.stars.append(Star())
    
    def update(self):
        for star in self.stars:
            star.x -= star.speed
            if (star.x  < 0):
                star.x = 220
    
    def draw(self):
        for star in self.stars:
            lcd.hline(star.x, star.y, star.speed, STAR_BLUE)

class Asteroid():
    def __init__(self):
        self.x = 250
        self.y = randint(5, 220)
        self.hp = 4
        self.speed = randint(1, 3)
        self.hitframes = 0
        r = randint(1,3) # random asteroid variations
        self.poly = array('h',[0,5, 15,0, 20,7, 17,10, 15,20, 5,20])
        if (r == 2):
            self.poly = array('h',[0,15, 7,3, 15,0, 19,7, 20,15, 10,20,])
        if (r == 3):
            self.poly = array('h',[0,12, 5,0, 20,7, 17,15, 10,20, 5,17])

class Asteroids():
    def __init__(self):
        self.asteroids = []
        
    def move(self):
        active_asteroids = len(self.asteroids)
        if (active_asteroids == 0):
            return
        for i in range(active_asteroids):
            a = self.asteroids.pop(0)
            a.x -= a.speed
            if (a.x > -10):
                self.asteroids.append(a)
            if (a.x < 0):
                global game_over
                game_over = True
                
    def draw(self):
        for a in self.asteroids:
            asteroid_color = ASTEROID
            if (a.hitframes > 0):
                asteroid_color = WHITE
                a.hitframes -=1
            
            lcd.poly(a.x, a.y, a.poly, asteroid_color, True) 
    
    def spawn(self):
        global level
        global game_over
        r = randint(0, 50 - (level * 3))
        if (level >= 99):
            game_over = True
        if (r == 0):
            self.asteroids.append(Asteroid())
            
        if (len(self.asteroids) == 0):
            self.asteroids.append(Asteroid())
            
        
def collision(torpedoes, asteroids):
    num_torp = len(torpedoes.torpedoes)
    
    if (num_torp == 0):
        return
    
    for t in range(num_torp):
        num_ast  = len(asteroids.asteroids)
        if (num_ast == 0):
            return
        torp = torpedoes.torpedoes.pop(0)
        collision = False
        for a in range(num_ast):
            ast = asteroids.asteroids.pop(0)
            collision = detect_collision([torp.x, torp.y, torpedo_speed, 1],[ast.x, ast.y, 20, 20])
            if (collision):
                ast.hp -= 1
                ast.hitframes = 3
            if (ast.hp > 0):
                    asteroids.asteroids.append(ast)
            if (ast.hp <= 0):
                global score
                global level
                global level_inc
                score += 1
                level_inc -= 1
                if (level_inc == 0):
                    level += 1
                    level_inc = level
                
        if (collision == False):
                torpedoes.torpedoes.append(torp)
              
def main():
    global score
    global game_over
    global level
 
    ship = Ship()
    starfield = Starfield()
    torpedoes = Torpedoes()
    asteroids = Asteroids()
    
    # Main game loop
    while (game_over == False):
        starfield.update()
        ship.move()
        asteroids.spawn()
        asteroids.move()
        torpedoes.shoot(ship)
        torpedoes.move()
        
        lcd.fill(BLACK)
        starfield.draw()
        ship.draw()
        torpedoes.draw()
        asteroids.draw()
        
        collision(torpedoes, asteroids)
        lcd.text('SCORE: %d' % score, 20, 220, lcd.green)
        lcd.text('LEVEL: %d' % level, 150, 220, lcd.green)
        lcd.show()
    
    # Game Over loop
    while (btn_y.value() == 1):
        starfield.update()
        lcd.fill(BLACK)
        starfield.draw()
        lcd.rect(50, 70, 150, 70, BLACK, True)
        lcd.rect(50, 70, 150, 70, RED, False)
        if (level >= 99):
            lcd.text(' WINNER! ', 90, 100, lcd.green)
        else:
            lcd.text('GAME OVER', 90, 90, lcd.green)
            lcd.text(' PRESS Y', 90, 110, lcd.green)
            
        lcd.text('SCORE: %d' % score, 20, 220, lcd.green)
        lcd.text('LEVEL: %d' % level, 150, 220, lcd.green)
        lcd.show()
        
    score = 0
    level = 1
    game_over = False
    main()
        
main()

    
