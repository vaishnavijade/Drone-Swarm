#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
import os
import signal
import sys
from dronekit import connect

from bdffont import *
from matrixbuffer import *
from weather import *
import time 
vehicle = connect("/dev/ttyACM0")
print("connected")

# matrix rows and cols in pixels
MATRIX_ROWS = 16
MATRIX_COLS = 16
RPI_HOSTNAME = "raspberrypi"
prv_mapped_value = -1

# set display wrapper to either terminal or neopixel based on hostname
if socket.gethostname() == RPI_HOSTNAME:
	from neopixelwrapper import *
	display_wrapper = NeopixelWrapper()
else:
	from terminalwrapper import *
	display_wrapper = TerminalWrapper()

font = BDFFont("fonts/5x7.bdf")
mb = MatrixBuffer(MATRIX_ROWS, MATRIX_COLS, font, display_wrapper)
#mb.clear()
#mb.write_string("a", (0,0,255), mb.ALIGN_RIGHT)
#mb.show()

def print_message(self, attr, val):
    pwm_val = val.chan8_raw
    print(pwm_val)
    mapped_value = map_pwm_to_range(pwm_val)
    if prv_mapped_value == mapped_value:
        return
    else:
        prv_mapped_value == mapped_value
    if 0 <= mapped_value <= 25:
        x = chr(mapped_value+ord('A'))
        mb.clear()
        mb.write_string(x, (0,0,255), mb.ALIGN_LEFT)
        mb.show()

vehicle.add_message_listener("RC_CHANNELS", print_message)

def map_pwm_to_range(pwm, min_pwm=794, max_pwm=2384, new_min=0, new_max=30):
    mapped_value = int(((pwm - min_pwm)/(max_pwm-min_pwm))*(new_max-new_min)+new_min)
    return mapped_value

time.sleep(100)