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

def set (instrument,obavestenje,var):
    if var.get()==u"синусоидални":
        instrument.write("APPLy:SINusoid")
        instrument.write("*CLS")
        obavestenje.config(text="Сигнал је сада синусоидални.")
    elif var.get()==u"правоугаони":
        instrument.write("APPLy:SQUare")
        instrument.write("*CLS")
        obavestenje.config(text="Сигнал је сада правоугаони.")
    elif var.get()==u"троугаони":
        instrument.write("APPLy:RAMP")
        instrument.write("*CLS")
        obavestenje.config(text="Сигнал је сада троугаони.")
    elif var.get()==u"импулсни":
        instrument.write("APPLy:PULSe")
        instrument.write("*CLS")
        obavestenje.config(text="Сигнал је сада импулсни.")
    elif var.get()==u"шум":
        instrument.write("APPLy:NOISe")
        instrument.write("*CLS")
        obavestenje.config(text="Сигнал је сада шум.")
    else:
        obavestenje.config(text="Нисте изабрали тип сигнала!")

    vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
    obavestenje.config(text="Вредности су ажуриране. " + vreme)
