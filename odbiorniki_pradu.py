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

#Obsluga przerwania wykonywania programu przez klawisze ctrl+C
CONTROL_C = False
def program_exit():
    # You may do some clean-up here, but you don't have to.
    print "\n"
    print "Exiting application... Thnxs                                             "
    GPIO.cleanup()
    subprocess.call('setterm -cursor on', shell=True)
    subprocess.call('spincl -ib', shell=True) 
    print " "

while True:

    #Petla jest wykonywana w nieskonczonosc z interwalem okreslonym w sekundach w time.sleep(2)
    #Plik jest uruchamiany co minute przez CRON

    ############### MYSQL ######################################################################

    #Tabela w ktørej zapisane sa aktualne parametry zwiazane z domem tabela aktualizowana co 2 sekundy
    #czyli jesli zmienila sie temperatura na jakims czujniku to jest ona zapisywana do tabeli co 2 sekundy
        
    db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")
    cursor = db.cursor()
    
    #cursor.execute("INSERT INTO pomiary_elektryczne_archiwum VALUES('',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(pom_napiecia_po_kalibracji, pom_pradu_po_kalibracji, temp_czujnik_wewn, temp_czujnik_zewn, temp_czujnik_3, czujka_napiecia_dwanascie_v_dziob, czujka_napiecia_dwanascie_v_rufa, czujka_napiecia_dwiesciedwadz_v_dziob, czujka_napiecia_dwiesciedwadz_v_rufa, data_godzina))
    cursor.execute("SELECT * FROM stan_biezacy_domu WHERE stan_biezacy_id = 1")
    #cursor.execute("SELECT * FROM stan_biezacy_domu WHERE stan_biezacy_id = 2")
    #rows = cursor.fetchall()
    #for row in rows:
    #print row["odbiornik_pradu_1"]
    #print cursor.fetchall() #to dziala pobiera dane z tabeli z bazy

    #cursor.close()
    #db.commit()

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


    print("\n--------------------------------------------\n")

    


    ############## END MYSQL ####################################################################
        
    time.sleep(2)
     
    if CONTROL_C: sys.exit(0)
exit (0)
