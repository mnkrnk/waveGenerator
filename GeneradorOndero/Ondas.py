'''
TPFinal MAM
@author: Mnk
'''
from pymam import wavwrite
from scipy.signal import tukey
from pylab import figure, ylabel, xlabel, plot, show
import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt

plt.ion()

def SineWave (a, fs, fq, phi, T, w):
#Operaciones previas
    t = np.arange(int(T*fs))/fs
#Genera la onda
    x = a*np.sin((2*np.pi*t-phi)*fq)
#Grafica
    figure(1)
    ylabel("Amplitud")
    xlabel("Tiempo")
    plot(t, x)
    show()
#Exporta el wav, con venatna/filtro
    win = tukey(len(t), w)
    xwin = x * win
    wavwrite("prueba_sine.wav", xwin, fs)
    return x

def SawWave (a, fs, fq, phi, T, w):
    t = np.arange(int(T*fs))/fs
    x = ((2*a)/np.pi)*np.arctan(np.tan((2*np.pi*t-phi)*fq))
    figure(2)
    ylabel("Amplitud")
    xlabel("Tiempo")
    plot(t, x)
    show()
    win = tukey(len(t), w)
    xwin = x * win
    wavwrite("prueba_saw.wav", xwin, fs)
    return x

def TrngWave (a, fs, fq, phi, T, w):
    t = np.arange(int(T*fs))/fs
    x = ((2*a)/np.pi)*np.arcsin(np.sin((2*np.pi*t-phi)*fq))
    figure(3)
    ylabel("Amplitud")
    xlabel("Tiempo")
    plot(t, x)
    show()
    win = tukey(len(t), w)
    xwin = x * win
    wavwrite("prueba_trng.wav", xwin, fs)
    return x

def SqrWave (a, fs, fq, phi, T, w):
    t = np.arange(int(T*fs))/fs
    x = a*np.sin((2*np.pi*t-phi)*fq)
#Empieza la magia
    y = ((x > 0)*2-1)*a
    y[x == 0] = 0
#Termina la magia    
    figure(4)
    ylabel("Amplitud")
    xlabel("Tiempo")
    plot(t, y)
    show()
    win = tukey(len(t), w)
    ywin = y * win
    wavwrite("prueba_sqr.wav", ywin, fs)
    return y