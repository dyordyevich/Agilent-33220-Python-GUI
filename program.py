#-*- coding:utf-8 -*-
## Модули
#Модул за графички кориснички интерфејс
from Tkinter import *
#Модул за комуникацију са уређајем
import visa
#Модул
import sys
#Додатни модули
import poruka
import veza
import trenutneVrednosti
import promenaSignala
import promenaVrednosti

#Тк функција за отварање помоћног прозора
def noviProzor():
    oprogramu = Toplevel(root)
    oprogramu.title("Телекомуникациона мерења")
    oprogramu.resizable(width=False, height=False)
    sirina=150
    visina=150
    w = oprogramu.winfo_screenwidth()/2-sirina/2
    h = oprogramu.winfo_screenheight()/2-visina/2
    oprogramu.geometry("%dx%d" % (sirina,visina))
    oprogramu.geometry("+%d+%d" % (w, h))

    verzija=Label(oprogramu,text="Верзија: 1.0")
    verzija.place(x=40,y=50)

#Исписивање почетне поруке
poruka.pocetnaPoruka()

#Успостављање везе са уређајем
rm=visa.ResourceManager('C:\\Program Files (x86)\\IVI Foundation\\VISA\\WinNT\\agvisa\\agbin\\visa32.dll')
uredjaj1adrese=["TCPIP0::169.254.2.20::inst0::INSTR","GPIB0::10::INSTR"]

#Исписивање обавештајне поруке
poruka.pronalazenjeUredjaja()

#tipUredjaja=None

brojac=0
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
        poruka.nijePovezan()
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
        poruka.nijePovezan()
        brojac=0

if brojac==0:
    print u"Уређај није повезан."
    quit()



##Прављење главног прозора
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

##Прављење менија
meni = Menu(root)

datoteka = Menu(meni, tearoff=0)
datoteka.add_command(label="Изађи", command=lambda: veza.egzit(root,instrument))
meni.add_cascade(label="Програм", menu=datoteka)

pomoc = Menu(meni, tearoff=0)
pomoc.add_command(label="О програму", command=noviProzor)
meni.add_cascade(label="Помоћ", menu=pomoc)
##......

## Приказивање менија
root.config(menu=meni)
##......

##Прављење оквира
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

########1. ОКВИР########
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

########2. ОКВИР########
###Тренутне вредности###

##Текст
naslov=Label(okvir2,text="Тренутне вредности", foreground="#283593")
naslov.place(x=80,y=5)
##......

##Вредности
signal=Label(okvir2,text="Тип сигнала:")
signal.place(x=5,y=35)

f=Label(okvir2,text="f =")
f.place(x=5,y=55)

vpp=Label(okvir2,text="Vpp =")
vpp.place(x=5,y=75)

##......

##Текст
obavestenje2=Label(okvir2,text=" ")
obavestenje2.place(x=5,y=105)
##......

##Дугме
azuriraj=Button(okvir2,text="Ажурирај",command=lambda: trenutneVrednosti.azuriranje(instrument,signal,f,obavestenje2,vpp))
azuriraj.place(x=200,y=102)
##......

#######################################################################################################################################

########3. ОКВИР########
###Промена типа сигнала###

##Текст
naslov=Label(okvir3,text="Промена типа сигнала", foreground="#283593")
naslov.place(x=60,y=5)
##......

##Падајући мени
var=StringVar(okvir3)
var.set("-")
tipovi=[u"синусоидални","правоугаони","троугаони", "импулсни","шум"]
odabir=OptionMenu(okvir3, var, *tipovi)
odabir.place(x=5,y=40)
##......

##Текст
info=Label(okvir3,text=" ")
info.place(x=5,y=90)
##......

##Текст
obavestenje3=Label(okvir3,text=" ")
obavestenje3.place(x=5,y=110)
##......

##Дугме
primeni=Button(okvir3,text="Примени", command=lambda: promenaSignala.set(instrument,obavestenje3,var))
primeni.place(x=155,y=41)
##......

#######################################################################################################################################

########4. ОКВИР########
###Промена вредности###

##Текст
naslov=Label(okvir4,text="Промена параметара", foreground="#283593")
naslov.place(x=75,y=5)
##......

##Текст
naslov=Label(okvir4,text="Фреквенција:")
naslov.place(x=5,y=35)
##......

##Текст
naslov=Label(okvir4,text="Амплитуда:")
naslov.place(x=5,y=67)
##......

##Поље
polje1=Entry(okvir4, width=8)
polje1.place(x=85,y=38)
##......

##Поље
polje2=Entry(okvir4, width=8)
polje2.place(x=85,y=70)
##......

##Падајући мени
var1=StringVar(okvir4)
var1.set("-")
tipovi1=["Hz","kHz","MHz"]
odabir1=OptionMenu(okvir4, var1, *tipovi1)
odabir1.place(x=137,y=35)
##......

##Падајући мени
var2=StringVar(okvir4)
var2.set("-")
tipovi2=["mV","V"]
odabir2=OptionMenu(okvir4, var2, *tipovi2)
odabir2.place(x=137,y=67)
##......

##Текст
obavestenje4=Label(okvir4,text=" ")
obavestenje4.place(x=5,y=110)
##......

##Дугме
primeniF=Button(okvir4,text="Примени", command=lambda: promenaVrednosti.set_frekvencija(instrument,polje1,obavestenje4,var1))
primeniF.place(x=205,y=37)
##......

##Дугме
primeniV=Button(okvir4,text="Примени", command=lambda: promenaVrednosti.set_napon(instrument,polje2,obavestenje4,var2))
primeniV.place(x=205,y=69)
##......

#######################################################################################################################################

root.mainloop()
