import random
from tkinter import *
import time

correct_numbers = [1,3,5,13,16,23]
def Lotto_No():
    try:
        inp_num1 = int(txtInput1.get())
        inp_num2 = int(txtInput2.get())
        inp_num3 = int(txtInput3.get())
        inp_num4 = int(txtInput4.get())
        inp_num5 = int(txtInput5.get())
        inp_num6 = int(txtInput6.get())
        inp_numlist = [inp_num1, inp_num2, inp_num3, inp_num4, inp_num5, inp_num6]
        inp_numlist.sort()        
        if inp_numlist == correct_numbers:
            x = correct_numbers[0]
            q = correct_numbers[1]
            w = correct_numbers[2]
            e = correct_numbers[3]
            r = correct_numbers[4]
            t = correct_numbers[5]
            num1.set(x)
            num2.set(q)
            num3.set(w)
            num4.set(e)
            num5.set(r)
            num6.set(t)
            return
        else:
            random_numbers = random.sample(range(1, 41), 6)
            random_numbers.sort()
            
            x = random_numbers[0]
            q = random_numbers[1]
            w = random_numbers[2]
            e = random_numbers[3]
            r = random_numbers[4]
            t = random_numbers[5]
            num1.set(x)
            num2.set(q)
            num3.set(w)
            num4.set(e)
            num5.set(r)
            num6.set(t)
            return
    except Exception as e:
        print(e)


    
def retrieve_numbers():
    try:
        num1 = int(txtInput1.get())
        num2 = int(txtInput2.get())
        num3 = int(txtInput3.get())
        num4 = int(txtInput4.get())
        num5 = int(txtInput5.get())
        num6 = int(txtInput6.get())
        num7 = int(txtOutput1.get())
        num8 = int(txtOutput2.get())
        num9 = int(txtOutput3.get())
        num10 = int(txtOutput4.get())
        num11 = int(txtOutput5.get())
        num12 = int(txtOutput6.get())
        numlist = [num1, num2, num3, num4, num5, num6]
        randlist = [num7, num8, num9, num10, num11, num12]
        numlist.sort()
        randlist.sort()

    except Exception as e:
        print(e)

def output_message():
    try:
        num1 = int(txtInput1.get())
        num2 = int(txtInput2.get())
        num3 = int(txtInput3.get())
        num4 = int(txtInput4.get())
        num5 = int(txtInput5.get())
        num6 = int(txtInput6.get())
        num7 = int(txtOutput1.get())
        num8 = int(txtOutput2.get())
        num9 = int(txtOutput3.get())
        num10 = int(txtOutput4.get())
        num11 = int(txtOutput5.get())
        num12 = int(txtOutput6.get())
        numlist = [num1, num2, num3, num4, num5, num6]
        randlist = [num7, num8, num9, num10, num11, num12]
        numlist.sort()
        randlist.sort()
        print(numlist)
        print(randlist)
        if correct_numbers == numlist:
            message= "Correct!"
            message_text.set(message)
        elif numlist == randlist:
            message = "Correct!! Amazing, you managed to guess the correct answer. "
            message_text.set(message)
        else: 
            message = ["Incorrect! Try again!","Bad luck! Try again!", "Incorrect!", "Incorrect!", "You are just guessing aren't you?"]
            message_text.set(random.choice(message))
    except Exception as e:
        print(e)
        message = "Check that you have entered all fields correctly"
        message_text.set(message)



Lottery = Tk()
Lottery.geometry('800x460')
Lottery.resizable(0, 0)
frame = Frame(Lottery)
frame.pack()

Lottery.title('Room Escape Lottery machine')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()
message_text = StringVar()

var = StringVar()
var.set("Choose 6 numbers between 1-40.")
frame1 = Frame(Lottery)
frame1.pack(side=TOP)

label = Label(frame1, textvariable=var, font
=("Arial", 28), width=44)
label.pack(side=TOP)

label2 = Label(frame1, textvariable="", width=24)
label2.pack(side=TOP)
label2 = Label(frame1, textvariable="", width=24)
label2.pack(side=TOP)


frame1.pack(side=TOP)
txtInput1 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput1.pack(side=LEFT)
txtInput2 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput2.pack(side=LEFT)
txtInput3 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput3.pack(side=LEFT)
txtInput4 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput4.pack(side=LEFT)
txtInput5 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput5.pack(side=LEFT)
txtInput6 = Entry(frame1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtInput6.pack(side=LEFT)

#BUTTON
frame3 = Frame(Lottery)
frame3.pack(side=TOP)
button1 = Button(frame3, padx=8, width=20, pady=8, bd=8, font=("Arial", 26), text="Draw lottery numbers", bg="black", fg="white", command=lambda:[Lotto_No(), retrieve_numbers(), output_message()])
button1.pack(side=TOP)

frame2 = Frame(Lottery)
frame2.pack(side=TOP)
txtOutput1 = Entry(frame2, textvariable=num1, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput1.pack(side=LEFT)
txtOutput2 = Entry(frame2, textvariable=num2, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput2.pack(side=LEFT)
txtOutput3 = Entry(frame2, textvariable=num3, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput3.pack(side=LEFT)
txtOutput4 = Entry(frame2, textvariable=num4, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput4.pack(side=LEFT)
txtOutput5 = Entry(frame2, textvariable=num5, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput5.pack(side=LEFT)
txtOutput6 = Entry(frame2, textvariable=num6, state = DISABLED, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtOutput6.pack(side=LEFT)

frame4 = Frame(Lottery)
frame4.pack(side=BOTTOM)
button2 = Entry(frame4, bd=0, textvariable=message_text, insertwidth=50,state = DISABLED,  font=("Arial", 15), justify='center', width=100)

button2.pack(side=TOP)

Lottery.mainloop()