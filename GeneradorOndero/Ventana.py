'''
TPFinal MAM
@author: Mnk
'''
from tkinter import *
import Ondas

def validData(a1, a2, a3, a4, a5, a6):
    try:
        amp2 = float(a1)
        sr2 = int(a2)
        freq2 = float(a3)
        fase2 = float(a4)
        tmp2 = int(a5)
        fade2 = float(a6)
        return amp2 > 0
    except ValueError:
        return False

def generar():
    amp = e1.get()
    sr = e2.get()
    freq = e3.get()
    fase = e4.get()
    tmp = e5.get()
    fade = e6.get()
    if (validData(amp, sr, freq, fase, tmp, fade) == True):
        txt.insert(END, "Comenzando el proceso.\n")
        if varsn.get() == 1:
            txt.insert(END, "Generando sinusoide.\n")
            Ondas.SineWave(float(amp), int(sr), float(freq), float(fase), int(tmp), float(fade))
        if varsw.get() == 1:
            txt.insert(END, "Generando diente de sierra.\n")
            Ondas.SawWave(float(amp), int(sr), float(freq), float(fase), int(tmp), float(fade))
        if vartr.get() == 1:
            txt.insert(END, "Generando triangular.\n")
            Ondas.TrngWave(float(amp), int(sr), float(freq), float(fase), int(tmp), float(fade))
        if varsq.get() == 1:
            txt.insert(END, "Generando cuadrada.\n")
            Ondas.SqrWave(float(amp), int(sr), float(freq), float(fase), int(tmp), float(fade))
    else:
        txt.insert(END, "Por favor, revise los datos ingresados.\n")

vnt = Tk()
vnt.title("Generador de Ondas")

varsn = IntVar()
varsw = IntVar()
vartr = IntVar()
varsq = IntVar()

a = Label(vnt, text="Amplitud")
a.grid(row = 1, column = 1, sticky = W)
e1 = Entry(vnt, bd = 5)
e1.grid(row = 1, column = 2, sticky = W)

fs = Label(vnt, text="Sample Rate")
fs.grid(row = 2, column = 1, sticky = W)
e2 = Entry(vnt, bd = 5)
e2.grid(row = 2, column = 2, sticky = W)

fq = Label(vnt, text="Frecuencia")
fq.grid(row = 3, column = 1, sticky = W)
e3 = Entry(vnt, bd = 5)
e3.grid(row = 3, column = 2, sticky = W)

fa = Label(vnt, text="Fase")
fa.grid(row = 4, column = 1, sticky = W)
e4 = Entry(vnt, bd = 5)
e4.grid(row = 4, column = 2, sticky = W)

t = Label(vnt, text="Tiempo (en seg)")
t.grid(row = 5, column = 1, sticky = W)
e5 = Entry(vnt, bd = 5)
e5.grid(row = 5, column = 2, sticky = W)

fd = Label(vnt, text="Fade (I & O)")
fd.grid(row = 6, column = 1, sticky = W)
e6 = Entry(vnt, bd = 5)
e6.grid(row = 6, column = 2, sticky = W)

grt = Button(vnt, text = "Generar", width = 8, height = 3, command = generar)
grt.grid(row = 7, column = 3)

txt = Text(vnt, height = 10, width = 40)
txt.grid(row = 7, column = 2, sticky = E)

chkSine = Checkbutton(vnt, text = "Sinusoide", variable = varsn)
chkSine.grid(row = 1, column = 3, sticky = W)


chkSaw = Checkbutton(vnt, text = "Diente de sierra", variable = varsw)
chkSaw.grid(row = 2, column = 3, sticky = W)

chkTrng = Checkbutton(vnt, text = "Triangular", variable = vartr)
chkTrng.grid(row = 3, column = 3, sticky = W)

chkSqr = Checkbutton(vnt, text = "Cuadrada", variable = varsq)
chkSqr.grid(row = 4, column = 3, sticky = W)

vnt.mainloop()