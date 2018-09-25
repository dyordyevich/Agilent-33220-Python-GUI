#-*- coding:utf-8 -*-
## Modules
#Module for GUI
from Tkinter import *
#Module for communication with device
import visa
#Module sys
import sys
#Date and time module
import datetime

def updatingValues(instrument,signal,f,note,vpp):

    ##Sending query for function type
    #Sending command
    instrument.write("FUNCtion?")
    #Reading received data
    vr=instrument.read()
    #Showing the result
    signal.config(text="Type of signal: " + str(vr))
    #Errasing
    instrument.write("*CLS")

    ##Sending query for frequency value
    #Sending command
    instrument.write("FREQuency?")
    #Reading received data
    readingValue=instrument.read()
    #Looking for letter E in received data (example +5.00000Е+03)
    checking=readingValue.find('E')

    # -1 - letter E doesn't exist
    if checking==-1:
        frek=float(readingValue)
        f.config(text="f = " + str(frek) + " Hz")
    else:
        #Splitting data in two peaces(example +5.00000 and +03)
        helpVar=readingValue.split('E')
        frek=float(helpVar[0])*10**float(helpVar[1])
        f.config(text="f = " + str(frek) + " Hz")
    #Errasing
    instrument.write("*CLS")


    ##Sending query for voltage value
    #Sending command
    instrument.write("VOLTage?")
    #Reading received data
    readingValue2=instrument.read()
    #Looking for letter E in received data (example +5.00000Е+03)
    checking2=readingValue.find('E')

    # -1 - letter E doesn't exist
    if checking2==-1:
        amplituda=float(readingValue)
        vpp.config(text="Vpp = " + str(amplituda) + " V")
    else:
        #Splitting data in two peaces(example +5.00000 and +03)
        helpVar2=readingValue2.split('E')
        amplituda=float(helpVar2[0])*10**float(helpVar2[1])
        vpp.config(text="Vpp = " + str(amplituda) + " V")
    #Errasing
    instrument.write("*CLS")

    #Showing time of last update
    onlyTime=datetime.datetime.now().time().strftime('%H:%M:%S')
    note.config(text="Values are updated. " + onlyTime)
