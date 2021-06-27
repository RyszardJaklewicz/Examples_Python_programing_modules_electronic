#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import linecache #biblioteka do pobierania danych z plikow
import time
import os
import sys
import RPi.GPIO as GPIO
from decimal import *
import atexit
import signal
import subprocess



#TRYB GPIO BCM
GPIO.setmode(GPIO.BCM)

#Piny GPIO ustawiamy w tryb WYJSCIA

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
