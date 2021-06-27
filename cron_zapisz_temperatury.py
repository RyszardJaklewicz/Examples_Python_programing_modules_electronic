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

#użycie numeracji pinów według BMC
#GPIO.setmode(GPIO.BCM)

#Pin nr 1 ustawiamy w tryb wyjscia
#GPIO.setup(30, GPIO.OUT)

#Na pinie 1 ustawiamy napięcie stanu NISKIEGO
#GPIO.output(30, GPIO.LOW)


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

db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")
#cursor = db.cursor()

print("\nPID:\n")
mypid = os.getpid()
print(mypid)

licznik=0
while True:
    
    licznik=licznik+1
    zawartosc_pliku_temperatura_czujnik_1 = ''
    zawartosc_pliku_temperatura_czujnik_2 = ''
    zawartosc_pliku_temperatura_czujnik_3 = ''
    zawartosc_pliku_temperatura_czujnik_4 = ''
    temperatura_czujnik_1_do_dzielenia = ''
    temperatura_czujnik_2_do_dzielenia = ''
    temperatura_czujnik_3_do_dzielenia = ''
    temperatura_czujnik_4_do_dzielenia = ''
    temperatura_czujnik_1 = ''
    temperatura_czujnik_2 = ''
    temperatura_czujnik_3 = ''
    temperatura_czujnik_4 = ''

    #Petla jest wykonywana w nieskonczonosc z interwalem okreslonym w sekundach w time.sleep(2)
    #Plik jest uruchamiany co minute przez CRON

    ################################################################################################
    ############ Odczyt danych z czujnikow temperatury #############################################

    #wiersz_temperatura_czujnik_1 = linecache.getline('/sys/bus/w1/devices/28-0000062395b7/w1_slave',2)
    #wiersz_temperatura_czujnik_1 = linecache.getline('/sys/bus/w1/devices/28-000006beee3c/w1_slave',2)

    plik_temperatura_czujnik_1 = open('/sys/bus/w1/devices/28-000006beee3c/w1_slave') #otwarcie pliku
    plik_temperatura_czujnik_2 = open('/sys/bus/w1/devices/28-0000062395b7/w1_slave') #otwarcie pliku
    plik_temperatura_czujnik_3 = open('/sys/bus/w1/devices/28-000005ceb2ef/w1_slave') #otwarcie pliku
    plik_temperatura_czujnik_4 = open('/sys/bus/w1/devices/28-000005ce60b2/w1_slave') #otwarcie pliku

    zawartosc_pliku_temperatura_czujnik_1 = plik_temperatura_czujnik_1.read()
    zawartosc_pliku_temperatura_czujnik_2 = plik_temperatura_czujnik_2.read()
    zawartosc_pliku_temperatura_czujnik_3 = plik_temperatura_czujnik_3.read()
    zawartosc_pliku_temperatura_czujnik_4 = plik_temperatura_czujnik_4.read()

    plik_temperatura_czujnik_1.close()
    plik_temperatura_czujnik_2.close()
    plik_temperatura_czujnik_3.close()
    plik_temperatura_czujnik_4.close()
    
    info_blad_czujnik_1 = zawartosc_pliku_temperatura_czujnik_1[36:39]
    temperatura_czujnik_1_do_dzielenia = zawartosc_pliku_temperatura_czujnik_1[69:81]
    temperatura_czujnik_1_do_dzielenia = float(temperatura_czujnik_1_do_dzielenia)#rzutowanie na liczbe calkowita
    temperatura_czujnik_1 = temperatura_czujnik_1_do_dzielenia/1000

    info_blad_czujnik_2 = zawartosc_pliku_temperatura_czujnik_2[36:39]
    temperatura_czujnik_2_do_dzielenia = zawartosc_pliku_temperatura_czujnik_2[69:81]
    temperatura_czujnik_2_do_dzielenia = float(temperatura_czujnik_2_do_dzielenia)#rzutowanie na liczbe calkowita
    temperatura_czujnik_2 = temperatura_czujnik_2_do_dzielenia/1000

    info_blad_czujnik_3 = zawartosc_pliku_temperatura_czujnik_3[36:39]
    temperatura_czujnik_3_do_dzielenia = zawartosc_pliku_temperatura_czujnik_3[69:81]
    temperatura_czujnik_3_do_dzielenia = float(temperatura_czujnik_3_do_dzielenia)#rzutowanie na liczbe calkowita
    temperatura_czujnik_3 = temperatura_czujnik_3_do_dzielenia/1000

    info_blad_czujnik_4 = zawartosc_pliku_temperatura_czujnik_4[36:39]
    temperatura_czujnik_4_do_dzielenia = zawartosc_pliku_temperatura_czujnik_4[69:81]
    temperatura_czujnik_4_do_dzielenia = float(temperatura_czujnik_4_do_dzielenia)#rzutowanie na liczbe calkowita
    temperatura_czujnik_4 = temperatura_czujnik_4_do_dzielenia/1000

    print "\n\n",zawartosc_pliku_temperatura_czujnik_1, "\n\n",
    print "\n\n",zawartosc_pliku_temperatura_czujnik_2, "\n\n",
    print "\n\n",zawartosc_pliku_temperatura_czujnik_3, "\n\n",
    print "\n\n",zawartosc_pliku_temperatura_czujnik_4, "\n\n",

    print "Temperatura czujnik 1", temperatura_czujnik_1, " stopni C\n\n",
    print "Temperatura czujnik 2", temperatura_czujnik_2, " stopni C\n\n",
    print "Temperatura czujnik 3", temperatura_czujnik_3, " stopni C\n\n",
    print "Temperatura czujnik 4", temperatura_czujnik_4, " stopni C\n\n",
    
    data_godzina =  time.strftime("%Y-%m-%d %H:%M:%S")
    
    zapisz_temperatury=1
    if(info_blad_czujnik_1!='YES'):
        zapisz_temperatury=0
    if(info_blad_czujnik_2!='YES'):
        zapisz_temperatury=0
    if(info_blad_czujnik_3!='YES'):
        zapisz_temperatury=0
    if(info_blad_czujnik_4!='YES'):
        zapisz_temperatury=0

    ############### START MYSQL ######################################################################

    #Tabela w ktørej zapisane sa aktualne parametry zwiazane z domem tabela aktualizowana co 4 sekundy
    #czyli jesli zmienila sie temperatura na jakims czujniku to jest ona zapisywana do tabeli co 4 sekundy
        
    #db = MySQLdb.connect("127.0.0.1", "root", "era123zx", "pomiary_elektryczne")
    cursor = db.cursor()

    #if(temperatura_czujnik_1!=127.937 and temperatura_czujnik_2!=127.937 and temperatura_czujnik_3!=127.937 and temperatura_czujnik_4!=127.937):  

    if(zapisz_temperatury==1):
        cursor.execute("""
                UPDATE stan_biezacy_domu
                SET
                temperatura_czujnik_1 = %s,
                temperatura_czujnik_2 = %s,
                temperatura_czujnik_3 = %s,
                temperatura_czujnik_4 = %s
                WHERE stan_biezacy_id=%s
            """,(temperatura_czujnik_1, temperatura_czujnik_2, temperatura_czujnik_3, temperatura_czujnik_4, '1'))
        db.commit()

        sql = "INSERT INTO pomiary_temperatura_archiwum(temperatura_czujnik_1, \
                  temperatura_czujnik_2, temperatura_czujnik_3, temperatura_czujnik_4, data_godzina) \
                  VALUES ('%s', '%s', '%s', '%s', '%s')" % \
                    (temperatura_czujnik_1, temperatura_czujnik_2, temperatura_czujnik_3, temperatura_czujnik_4, data_godzina)
        cursor.execute(sql)
        db.commit()
        cursor.close()
    
    print("\n--------------------------------------------\n")

    ############## END MYSQL ####################################################################
        
    time.sleep(3)
    #if(licznik==6):
        #sys.exit(0)

    if CONTROL_C: sys.exit(0)
    #exit(0)

GPIO.cleanup()

