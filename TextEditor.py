#Importing
from tkinter import *
from tkinter import filedialog
from os import path
#GUI
root = Tk()
root.title('Text Editor')
root.geometry('500x500')



filename = NONE

#Functions
def cut_fun(*args):
    text_entry_box.event_generate("<<Cut>>")

def copy_fun(*args):
    text_entry_box.event_generate("<<Copy>>")

def paste_fun(*args):
    text_entry_box.event_generate("<<Paste>>")


def settitle(*args):
    if filename != NONE:
        fname_var.set(filename)
    else:
        if filename == NONE:
            fname_var.set("Untitled")


def new_file(*args):
    text_entry_box.delete("1.0",END)
    filename = None
    settitle()
    fname_var.set("Untitled")
    status_var.set("New File Created")
    


def open_file(*args):
    global filename
    try:
        filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
        if filename != NONE:
            infile = open(filename,"r")
            text_entry_box.delete("1.0",END)
            for line in infile:
                text_entry_box.insert(END,line)
            infile.close()
            status_var.set("Opened Successfully")
            raw_fname = path.basename(filename)
            fname, deleted = raw_fname.split('.')
            deleted = ''
            fname_var.set(fname)
    except Exception as e:
        pass


def save_fun(*args):
    try:
        if filename != NONE:
            data = text_entry_box.get("1.0",END)
            outfile = open(filename,"w")
            outfile.write(data)
            outfile.close()
            raw_fname = path.basename(filename)
            fname, deleted = raw_fname.split('.')
            deleted = ''
            status_var.set("Saved Successfully")
            fname_var.set(fname)
        else:
            if filename == NONE:
                saveas_fun()
    except Exception as e:
        pass


def saveas_fun(*args):
    try:
        untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",
                                                    filetypes = (("Text Files","*.txt"), ("All Files","*.*"), ("Python Files","*.py")))
        data =text_entry_box.get("1.0",END)
        outfile = open(untitledfile,"w")
        outfile.write(data)
        outfile.close()
        filename = untitledfile
        raw_fname = path.basename(filename)
        fname, deleted = raw_fname.split('.')
        deleted = ''
        settitle()
        status_var.set("Saved Successfully")
        fname_var.set(fname)
    except Exception as e:
        pass




#Widgets
fname_var = StringVar()
fname_var.set(NONE)

status_var = StringVar()

settitle()

file_name_lbl = Label(root, textvariable=fname_var, font=('bold'))
file_name_lbl.pack(side=TOP)

statusbar = Label(root,textvariable=status_var,font=("arial",15),bd=2,relief=GROOVE)
statusbar.pack(side=BOTTOM,fill=BOTH)
statusbar.config(borderwidth=0)


text_entry_scroll = Scrollbar(root)
text_entry_scroll.pack(side=RIGHT, fill=Y)

text_entry_box = Text(root, font=('arial', 22), yscrollcommand=text_entry_scroll.set)
text_entry_box.pack(fill=BOTH, expand=1)
text_entry_box.config(borderwidth=0)
text_entry_box.bind('<Control-s>', save_fun)
text_entry_box.bind('<Control-c>', copy_fun)
text_entry_box.bind('<Control-p>', paste_fun)
text_entry_box.bind('<Control-x>', cut_fun)
text_entry_box.bind('<Control-o>', open_file)
text_entry_box.bind('<Control-n>', new_file)


text_entry_scroll.config(borderwidth=0, command=text_entry_box.yview)


new_btn = Button(root, text='New', width=8, height=1, command=new_file)
new_btn.place(x=0, y=0)
new_btn.config(borderwidth=0)

open_btn = Button(root, text='Open', width=8, height=1, command=open_file)
open_btn.place(x=65, y=0)
open_btn.config(borderwidth=0)

save_btn = Button(root, text='Save', width=8, height=1, command=save_fun)
save_btn.place(x=130, y=0)
save_btn.config(borderwidth=0)


root.mainloop()