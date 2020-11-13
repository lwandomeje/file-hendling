from tkinter import *
from tkinter import  filedialog

show=Tk()

show.title("Student: Lwando Meje")
show.geometry("800x490")
show.configure(background="lightGray")

def creat_file():
    open_file= filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def append_file():
    a = filedialog.askopenfile(mode="a")
    if a is not None:
        return
    text = entry.get(1.0,"end-1c") + "\n"
    content = a.write(text)
    entry.insert(INSERT,content)




def clear_file():
    entry.delete(1.0,END)



def display_file():
    file = filedialog.askopenfile(mode="r")
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)



entry=Text(show,height=18,width=58,wrap=WORD)
entry.place(x=100,y=10)


creat_button=Button(show,bg="Aqua",text="Create" ,command=creat_file)
creat_button.place(x=50,y=350)

clear_button=Button(show,bg="Aqua",text="Append Data",command=append_file)
clear_button.place(x=160,y=350)

display_button=Button(show,bg= "Aqua",text="Display",command=display_file)
display_button.place(x=290,y=350)


clear_button=Button(show,bg= "orange",text="clear",command=clear_file)
clear_button.place(x=500,y=450)

exit_button = Button(show,bg= "red", text="click to exit",command=show.destroy)
exit_button.place(x=590,y=450)

show.mainloop()
