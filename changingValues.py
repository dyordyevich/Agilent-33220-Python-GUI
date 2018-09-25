#-*- coding:utf-8 -*-
## Modules
#MOdule for GUI
from Tkinter import *
#Module for communication with device
import visa
#Module sys
import sys
#Date and time module
import datetime

def set_frekvencija(instrument,polje1,obavestenje,var1):
    #Getting value from entry
    vrednostStr=str(polje1.get())
    #Program is checking which function is chosen
    instrument.write("FUNCtion?")
    funkcija=str(instrument.read())
    instrument.write("*CLS")

    #Program is checking which unit is chosen
    if var1.get()==u"Hz":
        instrument.write("FREQuency "+vrednostStr)
        #Showing note about last change
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    elif var1.get()==u"kHz":

        instrument.write("FREQuency "+vrednostStr+"E+3")
        #Showing note about last change
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    elif var1.get()==u"MHz":

        instrument.write("FREQuency "+vrednostStr+"E+6")
        #Showing note about last change
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    else:

        obavestenje.config(text="Нисте изабрали јединицу!")



def set_napon(instrument,polje2,obavestenje,var2):
    #Getting value from entry
    vrednostStr=str(polje2.get())
    #Program is checking which function is chosen
    instrument.write("FUNCtion?")
    funkcija=str(instrument.read())
    instrument.write("*CLS")

    #Program is checking which unit is chosen
    if var2.get()==u"mV":
        instrument.write("VOLTage "+vrednostStr+"E-3")
        #Showing note about last change
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Амплитуда је промењена! " + vreme)

    elif var2.get()==u"V":
        instrument.write("VOLTage "+vrednostStr)
        #Showing note about last change
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Амплитуда је промењена! " + vreme)

    else:

        obavestenje.config(text="Нисте изабрали јединицу!")
