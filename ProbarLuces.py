import RPi.GPIO as GPIO
import sys
from time import sleep
from Tkinter import *
root = Tk()

root.title("Encender Luces")
root.geometry("300x360")
root.resizable(0,0)

def EncenderLuz(pin):
    #pin=26
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    state = GPIO.input(pin)

    if(state is 0):
        #print('Apagar')
        GPIO.output(pin,True)
    else:
        #print('Encender')
        GPIO.output(pin,False)


w = Label(root, text="Cambio de Estilo", bg="blue", fg="white", height=6)
w.pack(fill=X)
w.bind("<Button>",lambda event: EncenderLuz(pin=26))

w = Label(root, text="Verde", bg="green", fg="white", height=6)
w.pack(fill=X)
w.bind("<Button>",lambda event: EncenderLuz(pin=19))

w = Label(root, text="Naranja", bg="orange", fg="black", height=6)
w.pack(fill=X)
w.bind("<Button>",lambda event: EncenderLuz(pin=13))

w = Label(root, text="Maquina Mala", bg="red", fg="white", height=6)
w.pack(fill=X)
w.bind("<Button>",lambda event: EncenderLuz(pin=6))


mainloop()
