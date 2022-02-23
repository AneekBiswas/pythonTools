#Veryfing Password for accesing generator
while True:
    qwerty = input('Enter Password:')
    if qwerty == '':
        break
    else:
        print('Inorrect Password')
#import libraries
print('Importing neccassary modules')
from tkinter import *
import random, string
from time import *
try :
    import pyperclip
except: 
    sleep(1)
    print('Import Pyperclip To run Properly')
    print('This Window will close after 5 seconds')
    sleep(5)
    quit()
sleep(1)
print('Import Complete')

#initializing Window
sleep(1)
print('Initializing Window')

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Aneek Biswas's- PASSWORD GENERATOR")

sleep(1)
print('Initialization Complete')

#heading
sleep(1)
print('Creating Heading')

heading =Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
###
Label(root, text = "Aneek Biswas's Password Generator", font ='arial 15 bold').pack(side = BOTTOM)

sleep(1)
print('Haeding Complete')

#select password length
sleep(1)
print('Creating labels')

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len=IntVar()
###Change To alter Length
lenth = Spinbox(root, from_ = 1, to_ = 64 , textvariable = pass_len , width = 15).pack()
sleep(1)
print('Label Creation Complete')

#define function
sleep(1)
print('Defining Functions')

pass_str = StringVar()

def Generator():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
sleep(1)
print('Defining Funcions Complete')

#Add buttons
sleep(1)
print('Adding buttons')

Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

sleep(1)
print('Adding Buttons Complete')

#Function to copy
sleep(1)
print('Adding The Copy Function')

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady = 5)

sleep(1)
print('Function Added')

#creating the loop to make the program run
sleep(1)
print('Completing The Initialization')

root.mainloop()

sleep(1)
print('Task completed.', end=' ')
sleep(1)
print('Thankyou For Using AneekBiswas\'s password generator')