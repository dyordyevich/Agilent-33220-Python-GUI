#-*- coding:utf-8 -*-
## Модули
#Модул за графички кориснички интерфејс
from Tkinter import *
#Модул за комуникацију са уређајем
import visa
#Модул
import sys
#Модул за датум и време
import datetime

def set_frekvencija(instrument,polje1,obavestenje,var1):
    #Узимање вредности из поља
    vrednostStr=str(polje1.get())
    #Програм проверава која функција је тренутно изабрана
    instrument.write("FUNCtion?")
    funkcija=str(instrument.read())
    instrument.write("*CLS")

    #Проверава се коју јединицу је корисник изабрао
    if var1.get()==u"Hz":
        instrument.write("FREQuency "+vrednostStr)
        #Приказивање обавештења о последњој промени
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    elif var1.get()==u"kHz":

        instrument.write("FREQuency "+vrednostStr+"E+3")
        #Приказивање обавештења о последњој промени
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    elif var1.get()==u"MHz":

        instrument.write("FREQuency "+vrednostStr+"E+6")
        #Приказивање обавештења о последњој промени
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Фреквенција је промењена. " + vreme)

    else:

        obavestenje.config(text="Нисте изабрали јединицу!")



def set_napon(instrument,polje2,obavestenje,var2):
    #Узимање вредности из поља
    vrednostStr=str(polje2.get())
    #Програм проверава која функција је тренутно изабрана
    instrument.write("FUNCtion?")
    funkcija=str(instrument.read())
    instrument.write("*CLS")

    #Проверава се коју јединицу је корисник изабрао
    if var2.get()==u"mV":
        instrument.write("VOLTage "+vrednostStr+"E-3")
        #Приказивање обавештења о последњој промени
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Амплитуда је промењена! " + vreme)

    elif var2.get()==u"V":
        instrument.write("VOLTage "+vrednostStr)
        #Приказивање обавештења о последњој промени
        vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
        obavestenje.config(text="Амплитуда је промењена! " + vreme)

    else:

        obavestenje.config(text="Нисте изабрали јединицу!")
