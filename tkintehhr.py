# from tkinter import  Tk, Label,Checkbutton
# main = Tk()
# main.title("AlbinaLera.COM")
# main.geometry("250x200")
# Label(main, text='male'). grid(row=0,column=1)
# Label(main, text='female'). grid(row=1,column=1)
# e1= Checkbutton(main)
# e2=Checkbutton(main)
# e1.grid(row=0)
# e2.grid(row=1)
# main.mainloop()

# from tkinter import  Tk, Label, Radiobutton
# main = Tk()
# main.title("AlbinaLera.COM")
# main.geometry("250x200")
# Label(main, text='Gfg'). grid(row=0,column=1)
# Label(main, text='MIT'). grid(row=1,column=1)
# e1= Radiobutton(main)
# e2= Radiobutton(main)
# e1.grid(row=0)
# e2.grid(row=1)
# main.mainloop()

# from tkinter import  Tk, Label, Listbox , StringVar
# main = Tk()
# main.title("AlbinaLera.COM")
# main.geometry("250x200")
# listbox = Listbox()
# items = StringVar()
# items.set(
#     "Python "
#     "C "
#     "C++ "
#     "Java "
# )
# listbox = Listbox(listvariable=items)
# listbox.pack()
# main.mainloop() 


from tkinter import Tk, Listbox, Scrollbar, RIGHT, Y, END, LEFT, BOTH

main= Tk()
scrollbar = Scrollbar(main)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(main, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))
   
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

main.mainloop()

