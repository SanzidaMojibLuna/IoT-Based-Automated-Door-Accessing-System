import os
import tkinter  
import tkinter.filedialog
import shutil
import integrated
import random
import time
from tkinter.font import Font
from tkinter import *
from tkinter import messagebox


top = Tk()
root = tkinter.Tk()

C = Canvas(top, bg="blue", height=500, width=800)
filename = PhotoImage(file = "background.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

top.title("SMART HOME SECURITY SYSTEM")



def settings():
    tp = Toplevel()
    C = Canvas(tp, bg="pink", height=500, width=800)
    filename = PhotoImage(file="background.png")
    background_label = Label(tp, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tp.title("SMART HOME SECURITY SYSTEM")

    b1 = Button(tp, text="  ADD PHOTO", bg="pink", fg="purple", anchor='w', relief=RAISED, height=1, width=15,command=save_photo)
    b1_window = C.create_window(330, 115, anchor='nw', window=b1)
    b1.config(font=('helvetica', 15, 'bold'))

    #b2 = Button(tp, text="RENAME PHOTO", bg="pink", fg="purple", anchor='w', relief=RAISED,
             #   height=1, width=15)
    #b2_window = C.create_window(330, 145, anchor='nw', window=b2)
    #b2.config(font=('helvetica', 15, 'bold'))
    
    b3 = Button(tp, text="REMOVE PHOTO", bg="pink", fg="purple", anchor='w', relief=RAISED,
                height=1, width=15,command=remove_photo)
    b3_window = C.create_window(330, 175, anchor='nw', window=b3)
    b3.config(font=('helvetica', 15, 'bold'))


    tp.mainloop()


def face_recognize():
    exec(integrated.sonar_range())
    
def save_photo():
    f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='/home',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('jpg images', '.jpg'),
                   ('jpeg images', '.jpeg')]
        )
 
    shutil.move(f, "/home/pi/Desktop/final/images")
    
def remove_photo():
    f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='/home/pi/Desktop/final/images',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('jpg images', '.jpg'),
                   ('jpeg images', '.jpeg')]
        )
 
    os.remove(f)
    


def open_window():
    tp=Toplevel()
    C = Canvas(tp, bg="pink", height=500, width=800)
    filename = PhotoImage(file="background.png")
    background_label = Label(tp, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    tp.title("SMART HOME SECURITY SYSTEM")

    one = Label(tp, text="ABOUT", bg="purple", fg="white", anchor='w')
    one_window = C.create_window(95, 20, anchor='nw', window=one)
    one.config(font=("Bold", 20))



    S = Scrollbar(one)
    T = Text(one, height=25, width=80,bg="pink",fg="purple")
    T.config(font=("Bold", 10))
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """A report by World Health Organization(WHO)and International Agency for Prevention of Blindness(IAPB) stated that there are approximately285 million peoples around the world who are
visuay impaired.Among these individuals, thereare 39 million who are totally blind.Africa and
other developing countries represent 90 percent ofthis statistics. According to WHO and IPAB, the
number of blind people will increase worldwide toreach the double by 2020.
It is difficult for blind people to move or livewithout help. There have been several systems
designed to support visually-impaired people andto improve the quality of their lives. Unfortunately,
most of these systems are limited in their capabilities.Almost 90 percent blind people have to depend
on others to ensure their safety.So, here we have thought about a project that will
give comfort to the blind people so that they don’tneed others to ensure their safety.Here our device
will be attached to the door and it will contain somefeatures to ensure safety.Through our system users
can detect people who came to their home andif they know the people then they can commandthe door to open through android device.The doorwill open automatically after command so that
blind people dont need to move.This device canalso detect suspicious activity and will give alertin any kind of danger situation. Our device willcollect data from the surrounding environment (viaeither laser scanner, cameras sensors, or sonar)
and transmitted to the user either via tactile, audioformat or both. Hardware and software both part
will be integrated in our device.There are many devices integrated for blind peoplebut mostly are for their walking,reading purposes
but we mainly focus on their security purpose sothat they can stay safe by themselves."""
    T.insert(END, quote)

    tp.mainloop()


one=Label(top,text="SMART HOME SECURITY SYSTEM",bg="purple",fg="white",anchor='w')
one_window=C.create_window(80,5,anchor='nw',window=one)
one.config(font=("Bold",30))


b1=Button(top,text="        START",bg="pink",fg="purple",anchor='w', relief=RAISED, height =1, width =15,command=face_recognize)
b1_window=C.create_window(330,115,anchor='nw',window=b1)
b1.config(font=('helvetica',15, 'bold'))


b2=Button(top,text="        ABOUT",bg="pink",fg="purple",anchor='w', relief=RAISED,command=open_window, height =1, width =15)
b2_window=C.create_window(330,185,anchor='nw',window=b2)
b2.config(font=('helvetica', 15, 'bold'))


b3=Button(top,text=" VIDEO TUTORIAL",bg="pink",fg="purple",anchor='w', relief=RAISED, height =1, width =15)
b3_window=C.create_window(330,255,anchor='nw',window=b3)
b3.config(font=('helvetica', 15, 'bold'))


b4=Button(top,text="      SETTINGS",bg="pink",fg="purple",anchor='w', relief=RAISED, height =1, width =15,command=settings)
b4_window=C.create_window(330,325,anchor='nw',window=b4)
b4.config(font=('helvetica', 15, 'bold'))

top.mainloop()