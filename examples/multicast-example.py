from machine import Pin
from util import LCD, color_rgb

# network-related imports
import network
import socket
import json

btn_a = Pin(15, Pin.IN, Pin.PULL_UP)
btn_b = Pin(17, Pin.IN, Pin.PULL_UP)
btn_x = Pin(19, Pin.IN, Pin.PULL_UP)
btn_y = Pin(21, Pin.IN, Pin.PULL_UP)

lcd = LCD()

# 4
# Create some colors.
# color_rgb is a function from our utility library.
BLACK = color_rgb(0, 0, 0)
RED   = color_rgb(255, 0, 0)
GREEN = color_rgb(0, 255, 0)
BLUE  = color_rgb(0, 0, 255)
YELLOW = color_rgb(255, 255, 0)
WHITE = color_rgb(255, 255, 255)

# https://docs.micropython.org/en/latest/library/socket.html

# Pico can only listen to this address
IN_UDP_IP = '255.255.255.255'

# mac cannot listen to above address, so must send to this one
# if you want to send to another Pico, just use IN_UDP_IP
OUT_UDP_IP = '239.255.255.255'

UDP_PORT = 1900

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# SSID and password
sta_if.connect('KantegaGuest', 'GjestKantega')

# socket for reading
in_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
in_sock.bind((UDP_IP, UDP_PORT))
in_sock.settimeout(0.1)

# socket for writing
out_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

q = None
answerNum = -1
attempts = 10

while attempts > 0:

    lcd.text('Kahoot', 50, 5, WHITE)

    # render before we wait for network messages
    lcd.show()

    if sta_if.isconnected():
        try:
            message = str(in_sock.recv(1024), 'UTF-8')
            print('Received message: ' + message)
            json_obj = json.loads(message)
            if json_obj['to'] == 'kahoot-players':
                q = json_obj
                print('Question: ' + q['q'])
                answerNum = -1
        except OSError as exc:
            # timeout gives exception            
            print(str(exc))
            attempts -= 1

    # clear screen
    lcd.fill(BLACK)

    # show the question and options
    if q != None:
        lcd.text(str(q['q']), 15, 30, WHITE)
        lcd.text(str(q['a']), 15, 60, BLUE)
        lcd.text(str(q['b']), 15, 80, YELLOW)
        lcd.text(str(q['c']), 15, 100, GREEN)
        lcd.text(str(q['d']), 15, 120, RED)
        if answerNum >= 0:
            lcd.text('*', 5, 60 + answerNum * 20, WHITE)

    # if waiting for an answer, check the buttoms
    if q != None and answerNum < 0:
        if btn_a.value() == 0:
            answerNum = 0
        if btn_b.value() == 0:
            answerNum = 1
        if btn_x.value() == 0:
            answerNum = 2
        if btn_y.value() == 0:
            answerNum = 3
        if answerNum >= 0:
            print('User chose option ' + str(answerNum))
            message = '{"to":"kahoot-server", "a":' + str(answerNum) + '}'
            print('Sending '  + message + ' to ' + UDP_IP + ':' + str(UDP_PORT))
            out_sock.sendto(message.encode('utf-8'), (OUT_UDP_IP, UDP_PORT))
            attempts = 10
