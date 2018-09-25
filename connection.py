#-*- coding:utf-8 -*-
import visa
import sys
from Tkinter import *
import poruka

def zatvaranje(instrument):
    instrument.close()

def egzit(root,instrument):
    instrument.close()
    root.destroy()
