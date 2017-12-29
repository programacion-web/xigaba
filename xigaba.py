#!/usr/bin/env python3
# Author: raul@ninja-code.de

import time
import subprocess

print ('Xigaba')

while 1 < 2:
    time.sleep(0.5)
    second_test = time.strftime('%S')
    minute_test = time.strftime('%M')
    hour_test = time.strftime('%H')
    print (hour_test + minute_test + second_test)

    if int(minute_test) == int(00) and int(second_test) == int(00):
        print ('llego al hora exacta')
        filen = 'HRS' + hour_test + '_O.mp3.mp3'
        print (filen)
        subprocess.Popen(["play", filen]).communicate()
    elif int(second_test) == int(00):
        print ('llego al minuto')
        filen = 'HRS' + hour_test + '.mp3'
        filen2 = 'MIN' + minute_test + '.mp3.mp3'
        print (filen)
        print (filen2)
        subprocess.Popen(["play", filen]).communicate()
        subprocess.Popen(["play", filen2]).communicate()

print ('Algo salio Mal')
