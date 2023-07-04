import tkinter as tk

def click():
    print('Tipka "Klikni me!" je pritisnut')

root=tk.Tk()
root.title('Drugi GUI')
root.geometry('600x400')


button=tk.Button(root, text='TIPKA')




button.pack()

button_click=tk.Button(root, text='Klikni me!', command=click).pack(padx=10,pady=10)
btn_image=tk.PhotoImage(file='python.gif')
button_image=tk.Button(root,text='Tipka sa slikom',
                       image=btn_image,
                       compound=tk.TOP,
                       relief=tk.RAISED, #GROOVE,
                       command=click,
                       state=tk.ACTIVE
                       ).pack(padx=10,pady=10)


root.mainloop()