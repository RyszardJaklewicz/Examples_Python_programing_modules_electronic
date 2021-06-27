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
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#os.system("python /home/pi/start.py")

#Obsluga przerwania wykonywania programu przez klawisze ctrl+C
CONTROL_C = False
def program_exit():
    # You may do some clean-up here, but you don't have to.
    print "\n"
    print "Exiting application... Thnxs"
    GPIO.cleanup()
    subprocess.call('setterm -cursor on', shell=True)
    subprocess.call('spincl -ib', shell=True) 
    print " "

#db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")
#cursor = db.cursor()

#Pobranie danych z konfiguracji np aby nie wykonac zadnych dzialan wystepujacych w petli
#cursor.execute("SELECT * FROM konfiguracja WHERE konfiguracja_id = 1")
#cursor = db.cursor()

#for rec in cursor.fetchall():
    #rec[1] to pole wlacz_proces_wlaczanie_odbiornikow
    #if(rec[1]=='N'):
        #exit()

#time.sleep(1)

licznik=0
while True:

    

    licznik=licznik+1

    ############### MYSQL ######################################################################

    #Tabela w ktørej zapisane sa aktualne parametry zwiazane z domem tabela aktualizowana co 2 sekundy
    #czyli jesli zmienila sie temperatura na jakims czujniku to jest ona zapisywana do tabeli co 2 sekundy

    #db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")    
    #cursor = db.cursor()

    #db.commit()

    #Pobranie danych z konfiguracji np aby nie wykonac zadnych dzialan wystepujacych w petli
    #cursor.execute("SELECT * FROM konfiguracja WHERE konfiguracja_id = 1")

    # rec[1] = odbiornik_pradu_1
    # rec[2] = odbiornik_pradu_2
    # rec[3] = odbiornik_pradu_3
    # rec[4] = odbiornik_pradu_4
    # rec[5] = odbiornik_pradu_5
    # rec[6] = odbiornik_pradu_6
    # rec[7] = odbiornik_pradu_7
    # rec[8] = odbiornik_pradu_8
    # rec[9] = odbiornik_pradu_9
    # rec[10] = odbiornik_pradu_10
    # rec[11] = odbiornik_pradu_11
    # rec[12] = odbiornik_pradu_12
    # rec[13] = odbiornik_pradu_13
    # rec[14] = odbiornik_pradu_14
    # rec[15] = odbiornik_pradu_15
    # rec[16] = odbiornik_pradu_16
    # rec[17] = odbiornik_pradu_17
    # rec[18] = odbiornik_pradu_18
    # rec[19] = odbiornik_pradu_19
    # rec[20] = odbiornik_pradu_20
    #
    # rec[21] = temperatura_czujnik_1
    # rec[22] = temperatura_czujnik_2
    # rec[23] = temperatura_czujnik_3
    # rec[24] = temperatura_czujnik_4
    # rec[25] = temperatura_czujnik_5
    # rec[26] = temperatura_czujnik_5
    # rec[27] = temperatura_czujnik_6
    # rec[28] = temperatura_czujnik_7
    # rec[29] = temperatura_czujnik_8
    # rec[30] = temperatura_czujnik_9
    # rec[31] = temperatura_czujnik_10
    #
    #
    #
    #
    #
    #
    #



    db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")
    cursor = db.cursor()
   
    #cursor = db.cursor()       
    
    cursor.execute("SELECT * FROM stan_biezacy_domu WHERE stan_biezacy_id = 1")
    
    for rec in cursor.fetchall():

        #Wlaczenie i wylaczenie odbiornika nr 1 - odbiornik sterowany sygnalem z pinu GPIO 2

        if(rec[1]=='T'):
            GPIO.output(2, GPIO.HIGH)
            print("Wlacz odbiornik nr 1")

        if(rec[1]=='N'):
            GPIO.output(2, GPIO.LOW)
            print("Wylacz odbiornik nr 1")


        #Wlaczenie i wylaczenie odbiornika nr 2 - odbiornik sterowany sygnalem z pinu GPIO 3

        if(rec[2]=='T'):
            GPIO.output(3, GPIO.HIGH)
            print("Wlacz odbiornik nr 2")

        if(rec[2]=='N'):
            GPIO.output(3, GPIO.LOW)
            print("Wylacz odbiornik nr 2")


        #Wlaczenie i wylaczenie odbiornika nr 3 - odbiornik sterowany sygnalem z pinu GPIO 4

        if(rec[3]=='T'):
            GPIO.output(4, GPIO.HIGH)
            print("Wlacz odbiornik nr 3")

        if(rec[3]=='N'):
            GPIO.output(4, GPIO.LOW)
            print("Wylacz odbiornik nr 3")


        #Wlaczenie i wylaczenie odbiornika nr 4 - odbiornik sterowany sygnalem z pinu GPIO 14

        if(rec[4]=='T'):
            GPIO.output(14, GPIO.HIGH)
            print("Wlacz odbiornik nr 4")

        if(rec[4]=='N'):
            GPIO.output(14, GPIO.LOW)
            print("Wylacz odbiornik nr 4")


        #Wlaczenie i wylaczenie odbiornika nr 5

        if(rec[5]=='T'):
            GPIO.output(15, GPIO.HIGH)
            print("Wlacz odbiornik nr 5")

        if(rec[5]=='N'):
            GPIO.output(15, GPIO.LOW)
            print("Wylacz odbiornik nr 5")



        #Wlaczenie i wylaczenie odbiornika nr 6


        if 1==2:
            if(rec[6]=='T'):
                GPIO.output(17, GPIO.HIGH)
                print("Wlacz odbiornik nr 6")

            if(rec[6]=='N'):
                GPIO.output(17, GPIO.LOW)
                print("Wylacz odbiornik nr 6")


            #Wlaczenie i wylaczenie odbiornika nr 7

            if(rec[7]=='T'):
                GPIO.output(22, GPIO.HIGH)
                print("Wlacz odbiornik nr 7")

            if(rec[7]=='N'):
                GPIO.output(22, GPIO.LOW)
                print("Wylacz odbiornik nr 7")


        cursor.close()

        print("\n--------------------------------------------\n")

    
    ############## END MYSQL ####################################################################
        
    time.sleep(2)

    #if(licznik==15):
        #sys.exit(0)
     
    if CONTROL_C: sys.exit(0)
exit (0)
