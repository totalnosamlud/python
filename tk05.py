import tkinter as tk



root=tk.Tk()
root.title('Pokušaj sa grid-om')



root.columnconfigure(0,weight=1,minsize=75)
root.columnconfigure(1,weight=1,minsize=190)

root.rowconfigure(0,weight=1,minsize=75)
root.rowconfigure(1,weight=1,minsize=90)

frame0=tk.Frame(root,
                relief=tk.RAISED,
                borderwidth=1)

frame0.grid(row=0,column=0,padx=15,pady=15)
label0=tk.Label(frame0, text='L0F0')
label0.pack(padx=55,pady=15)

root.mainloop()