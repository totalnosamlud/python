import tkinter as tk



root=tk.Tk()
root.title('Pokušaj sa placeom')
root.geometry('600x400')

btn_image=tk.PhotoImage(file='Python.gif')
button_image=tk.Button(root,text='Tipka sa slikom',
                      image=btn_image,
                      compound=tk.LEFT).place(x=150, y=75)

label=tk.Label(root, text='Neki label')
label.place(x=150,y=120)

root.mainloop()