import tkinter as tk

def click():
    label.config(text='Izmjenjeni text\nu tri\nreda',
                font=('Helvetica, 18'),fg='red')



root=tk.Tk()
root.title('Treća sreća')
root.geometry('600x400')


label=tk.Label(root, text='Poruka\nu dva reda',
               font=('Segoe UI',16))
label.pack(padx=30,pady=40)

button_click=tk.Button(root,text="Klikni me!", command=click()).pack(padx=10,pady=10)

image_in_label=tk.PhotoImage(file='python-logo.png').subsample(7)
label_image=tk.Label(root,text='Tekst nekakvi',
                     font=('Segoe UI', 20),
                     compound=tk.CENTER,
                     image=image_in_label)

label_image.pack(padx=5,pady=5)

root.mainloop()