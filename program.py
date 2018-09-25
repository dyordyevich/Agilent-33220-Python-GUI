#-*- coding:utf-8 -*-
## Modules
#Module for GUI
from Tkinter import *
#Module fot communication with device
import visa
#Module sys
import sys
#Extra modules
import message
import connection
import currentValues
import changingSignal
import changingValues

#Тк function for opening the second (help) window
def noviProzor():
    oprogramu = Toplevel(root)
    oprogramu.title("Telecommunication measurements")
    oprogramu.resizable(width=False, height=False)
    sirina=150
    visina=150
    w = oprogramu.winfo_screenwidth()/2-sirina/2
    h = oprogramu.winfo_screenheight()/2-visina/2
    oprogramu.geometry("%dx%d" % (sirina,visina))
    oprogramu.geometry("+%d+%d" % (w, h))

    verzija=Label(oprogramu,text="Version: 1.0")
    verzija.place(x=40,y=50)

#Showing message
message.welcome()

#Connection with device
rm=visa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
uredjaj1adrese=["TCPIP0::169.254.2.20::inst0::INSTR","GPIB0::10::INSTR"] # <- here you should add addresses of device

#Showing message
message.findingDevices()

#tipUredjaja=None

brojac=0 #brojac=counter
if brojac==0:
    print ">>> LAN"
    try:
        instrument=rm.open_resource(uredjaj1adrese[0])
        instrument.write("*IDN?")
        tipUredjaja=instrument.read()
        model=tipUredjaja.split(',')
        instrument.write("*CLS")
        brojac=1
        interfejs="LAN"
    except:
        message.notConnected()
        brojac=0

if brojac==0:
    print ">>> GPIB"
    try:
        instrument=rm.open_resource(uredjaj1adrese[1])
        instrument.write("*IDN?")
        tipUredjaja=instrument.read()
        model=tipUredjaja.split(',')
        instrument.write("*CLS")
        brojac=1
        interfejs="GPIB"
    except:
        message.notConnected()
        brojac=0

if brojac==0:
    print u"Уређај није повезан."
    quit()



##Creating main window
root=Tk()
sirina=540
visina=270
w = root.winfo_screenwidth()/2-sirina/2
h = root.winfo_screenheight()/2-visina/2
root.geometry("%dx%d" % (sirina,visina))
root.geometry("+%d+%d" % (w, h))
root.title("Телекомуникациона мерења")
root.resizable(width=False, height=False)
##......

##Creating menu
meni = Menu(root)

datoteka = Menu(meni, tearoff=0)
datoteka.add_command(label="Изађи", command=lambda: connection.egzit(root,instrument))
meni.add_cascade(label="Програм", menu=datoteka)

pomoc = Menu(meni, tearoff=0)
pomoc.add_command(label="О програму", command=noviProzor)
meni.add_cascade(label="Помоћ", menu=pomoc)
##......

## Showing menu
root.config(menu=meni)
##......

##Making frames (okvir)
okvir1=Frame(root,width=270, height=135, borderwidth=1, relief=SUNKEN)
okvir2=Frame(root,width=270, height=135,borderwidth=1, relief=SUNKEN)
okvir3=Frame(root,width=270, height=135,borderwidth=1, relief=SUNKEN)
okvir4=Frame(root,width=270, height=135,borderwidth=1, relief=SUNKEN)
okvir1.grid(row=0, column=0)
okvir2.grid(row=0, column=1)
okvir3.grid(row=1, column=0)
okvir4.grid(row=1, column=1)
##......

#######################################################################################################################################

########1. FRAME########
###Опште информације###

naslov=Label(okvir1,text="Телекомуникациона мерења", foreground="#283593")
naslov.place(x=45,y=5)

profesor=Label(okvir1,text="Професор: др Ненад Јевтић")
profesor.place(x=5,y=35)

student=Label(okvir1,text="Студент: Никола Ђорђевић ТС130211")
student.place(x=5,y=55)

linija=Label(okvir1,text="-------")
linija.place(x=5,y=75)


oUredjaju=Label(okvir1,text=model[0]+" "+model[1]+" >>> "+interfejs)
oUredjaju.place(x=5,y=90)

#######################################################################################################################################

########2. FRAME########
###Current values###

##Text
naslov=Label(okvir2,text="Current values", foreground="#283593")
naslov.place(x=80,y=5)
##......

##Values
signal=Label(okvir2,text="Type of signal:")
signal.place(x=5,y=35)

f=Label(okvir2,text="f =")
f.place(x=5,y=55)

vpp=Label(okvir2,text="Vpp =")
vpp.place(x=5,y=75)

##......

##Text
obavestenje2=Label(okvir2,text=" ")
obavestenje2.place(x=5,y=105)
##......

##Button
azuriraj=Button(okvir2,text="Ажурирај",command=lambda: currentValues.updatingValues(instrument,signal,f,obavestenje2,vpp))
azuriraj.place(x=200,y=102)
##......

#######################################################################################################################################

########3. FRAME########
###Changing type of signal###

##Тext
naslov=Label(okvir3,text="Промена типа сигнала", foreground="#283593")
naslov.place(x=60,y=5)
##......

##List meny
var=StringVar(okvir3)
var.set("-")
tipovi=[u"синусоидални","правоугаони","троугаони", "импулсни","шум"]
odabir=OptionMenu(okvir3, var, *tipovi)
odabir.place(x=5,y=40)
##......

##Text
info=Label(okvir3,text=" ")
info.place(x=5,y=90)
##......

##Text
obavestenje3=Label(okvir3,text=" ")
obavestenje3.place(x=5,y=110)
##......

##Button
primeni=Button(okvir3,text="Примени", command=lambda: changingSignal.set(instrument,obavestenje3,var))
primeni.place(x=155,y=41)
##......

#######################################################################################################################################

########4. FRAME########
###Промена вредности###

##Text
naslov=Label(okvir4,text="Промена параметара", foreground="#283593")
naslov.place(x=75,y=5)
##......

##Text
naslov=Label(okvir4,text="Фреквенција:")
naslov.place(x=5,y=35)
##......

##Text
naslov=Label(okvir4,text="Амплитуда:")
naslov.place(x=5,y=67)
##......

##Entry
polje1=Entry(okvir4, width=8)
polje1.place(x=85,y=38)
##......

##Entry
polje2=Entry(okvir4, width=8)
polje2.place(x=85,y=70)
##......

##List meny
var1=StringVar(okvir4)
var1.set("-")
tipovi1=["Hz","kHz","MHz"]
odabir1=OptionMenu(okvir4, var1, *tipovi1)
odabir1.place(x=137,y=35)
##......

##List meny
var2=StringVar(okvir4)
var2.set("-")
tipovi2=["mV","V"]
odabir2=OptionMenu(okvir4, var2, *tipovi2)
odabir2.place(x=137,y=67)
##......

##Text
obavestenje4=Label(okvir4,text=" ")
obavestenje4.place(x=5,y=110)
##......

##Button
primeniF=Button(okvir4,text="Примени", command=lambda: changingValues.set_frekvencija(instrument,polje1,obavestenje4,var1))
primeniF.place(x=205,y=37)
##......

##Button
primeniV=Button(okvir4,text="Примени", command=lambda: changingValues.set_napon(instrument,polje2,obavestenje4,var2))
primeniV.place(x=205,y=69)
##......

#######################################################################################################################################

root.mainloop()
