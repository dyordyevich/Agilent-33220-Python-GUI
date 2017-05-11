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

def azuriranje(instrument,signal,f,obavestenje,vpp):

    ##Слање упита за тип функције
    #Слање команде
    instrument.write("FUNCtion?")
    #Читање примљеног податка
    vr=instrument.read()
    #Приказивање резултата
    signal.config(text="Тип сигнала: " + str(vr))
    #Брисање
    instrument.write("*CLS")

    ##Слање упита за вредност фреквенције
    #Слање команде
    instrument.write("FREQuency?")
    #Читање примљеног податка
    citanje=instrument.read()
    #Тражење слова Е у примљеном податку (нпр. +5.00000Е+03)
    ispitivanje=citanje.find('E')

    #Испитивање да ли постоји слово Е у примљеном подакту; -1 - не постоји
    if ispitivanje==-1:
        frek=float(citanje)
        f.config(text="f = " + str(frek) + " Hz")
    else:
        #Дељење примљеног податка на два дела (нпр. +5.00000 и +03)
        pomocna=citanje.split('E')
        frek=float(pomocna[0])*10**float(pomocna[1])
        f.config(text="f = " + str(frek) + " Hz")
    #Брисање
    instrument.write("*CLS")


    ##Слање упита за вредност фреквенције
    #Слање команде
    instrument.write("VOLTage?")
    #Читање примљеног податка
    citanje2=instrument.read()
    #Тражење слова Е у примљеном податку (нпр. +5.00000Е+03)
    ispitivanje2=citanje.find('E')

    #Испитивање да ли постоји слово Е у примљеном подакту; -1 - не постоји
    if ispitivanje2==-1:
        amplituda=float(citanje)
        vpp.config(text="Vpp = " + str(amplituda) + " V")
    else:
        #Дељење примљеног податка на два дела (нпр. +5.00000 и +03)
        pomocna2=citanje2.split('E')
        amplituda=float(pomocna2[0])*10**float(pomocna2[1])
        vpp.config(text="Vpp = " + str(amplituda) + " V")
    #Брисање
    instrument.write("*CLS")

    #Приказивање времена последњег ажурирања
    vreme=datetime.datetime.now().time().strftime('%H:%M:%S')
    obavestenje.config(text="Вредности су ажуриране. " + vreme)
