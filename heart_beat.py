from Tkinter import *
import time
window = Tk()
window.title("Heart Beat Sensor")
window.iconbitmap(default = 'transparent.ico')
label1 = Label(window,text='Dinosaurs',font=('Verdana',50))
#label1.grid(row=1,column=1)
label1.pack()
heart = PhotoImage(file='big_heart.gif')
label2 = Label(window,image=heart)
#label2.grid(row=1,column=2)
label2.pack()
import serial
data = serial.Serial('com3',9600)
time.sleep(2)
def show(event):  #binded
    time.sleep(2)
    label1.configure(text = data.readline())
    
    
def show2():
    time.sleep(2)
    label1.configure(text = data.readline())


button1 = Button(window,text = "Check",command=show2,bg = '#2ff5dc',fg='blue')
button1.grid(row=3,column=3,columnspan=2)
button1.pack()
window.bind('<Return>',show) #binding the show function with the 'Enter' key.
  
window.mainloop()
