# 04.05.23 | removed some button icons because they were displayed inproperly in some screen resolutions
           # added 2 themes, removing grey theme

# 01.04.23 | made the app window responsive to various screens
# 28.03.23 | 1) dealt with some syntax errors in renaming; but there are still harmless bugs
#            2) added renaming ability right from textbox     
# some major buxs fixed, the code has become more coherent
# you can switch between windows using frames, this method is smooth.
# class based windows are myth

import tkinter
import re
from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import Menu
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Title Normalizer")
root.resizable(0,0)

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# making the app window close to the centre of the screen
iheight = int(screen_width*0.4)
iwidth = int(screen_height*0.3)

root.geometry(f"+{iheight}+{iwidth}")

def info_popup(event=None):
    top = Toplevel(root)
    top.title("About: Title Normalizer v1.8")
    Label(top, justify = "left", text="Info:\
    \n ✅ Regular Mode: Bu rejimda siz oʻzingiz istagan sarlavha yoki fayl nomidagi ortiqcha probel,\n tagchiziq, chiziqcha yoki nuqtalarni olib tashlashingiz mumkin.\
    \n ✅ Developer Mode: Bu rejimda oʻzingiz istagan sarlavha yoki fayl nomidagi boʻsh joylar oʻrniga\n tagchiziq yoki chiziqcha qoʻyib qoʻyishingiz mumkin.\n\
    \nUmumiy qoidalar:\
    \n • Fayl nomidagi tagchiziq ( _ ), chiziqcha ( - ) va nuqtalarni yoʻqotib, oʻrniga probel qoʻyib qoʻyish uchun «Normalize» tugmasini bosing.\
    \n • Fayl nomidagi probellarni yoʻqotib, oʻrniga tagchiziq qoʻyish uchun «Add ( _ )» tugmasini bosing.\
    \n • Fayl nomidagi probellar oʻrniga chiziqcha qoʻyib qoʻyish uchun «Add ( - )» tugmasini bosing. \
    \n • Fayl menejer orqali kerakli faylni tanlash uchun Fayl menyusidagi «Open» tugmasini bosing.\
    \n • Matn maydonlarini tozalash uchun «Clear» tugmasini bosing.\
    \n • Tayyor boʻlgan matnni buferga koʻchirib olish uchun «Copy» tugmasini bosing.\
    \n • Tanlangan faylni yangi nom bilan saqlash uchun «Rename» tugmasini bosing.\n\
    \n'Bufer'ni chiqarish uchun Win+V tugmalarini birgalikda bosing.\n\
    \nBogʻlanish uchun kontaktlar:\
    \n🔗 Telegram: @Abdulloh_ID\
    \n🔗 Email: outergamer11@gmail.com").pack(padx=(5,0), pady=(5,0))
    Label(top,
        justify = "left",
        text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack(pady=(0,5))

root.bind('<F1>', info_popup)

''' Adding a main frame '''

main_fr = Frame(root, bg='#025a6c')
main_fr.grid(ipady=2)

txt = Text(main_fr, font='Calibri 10', height=5, width=25, wrap=WORD)
txt.focus()
txt.grid(row=0, column=0, pady=5, padx=5)

rslt = Text(main_fr, font=('Calibri 10'), height=5, width=25, wrap=WORD)
rslt.grid(row=1, column=0)

def get_file_name(event=None):
    global file_directory
    global filename
    global file_ext
    global file_path

    file_path = fd.askopenfilename(title="Choose a file to rename")
    file_path_components = file_path.split('/')
    file_directory = "/".join(file_path_components[:-1]) + "/"
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)

    filename = file_name_and_extension[0]
    file_ext = file_name_and_extension[1]

    clear_entry()
    txt.insert("end", filename)
    rslt.delete('1.0', 'end')

root.bind("<Control-o>", get_file_name)

def title_normalizer(event=None):
    global T
    input_txt = txt.get(1.0, "end-1c")
    T = input_txt

    if "_" or "-" or "." or "  " in T:
        T = T.replace("_", " ")
        T = T.replace("-", " ")
        T = T.replace(".", " ")
        T = T.replace("  ", " ")

    rslt.delete('1.0', 'end')
    rslt.insert("end", T)

#txt.bind("<<Paste>>", title_normalizer)

def copy_to_clipboard():
    global F
    final_rslt = rslt.get('1.0', 'end-1c')
    F = final_rslt
    cpy.clipboard_clear()
    cpy.clipboard_append(F)

def clear_entry():
    txt.delete('1.0', 'end')
    rslt.delete('1.0', 'end')
    rslt.config(state="normal")

def rename():
    final_rslt = rslt.get('1.0', 'end-1c')
    F = final_rslt
    if ":" or "/" or "\\" or "*" or "?" or "<" or ">" or "\"" or "|" in F: # add prohibited symbols here
        W = "The new filename includes characters that are not allowed in naming a file! ( : / \\ * ? <> |)"
        rslt.delete('1.0', 'end')
        rslt.insert("end", W)
        rslt.config(state="disabled")
    else:
        pass

    old_file = f"{file_directory}" + f"{filename}.{file_ext}"
    new_file_1 = f"{file_directory}" + f"{F}.{file_ext}"
    os.rename(old_file, new_file_1)
    clear_entry()

# color themes

def ocean_bg(event=None):
    main_fr.configure(bg='#025a6c')
    txt.config(bg="white", fg="black")
    rslt.config(bg="white", fg="black")
    side_fr.configure(bg='#025a6c')
    txt1.config(bg="white", fg="black")
    rslt1.config(bg="white", fg="black")

def hunter_green_bg(event=None):
    main_fr.configure(bg='#355E3B')
    side_fr.configure(bg='#355E3B')
    txt.config(bg="white", fg="black")
    rslt.config(bg="white", fg="black")
    txt1.config(bg="white", fg="black")
    rslt1.config(bg="white", fg="black")

def navy_bg(event=None):
    main_fr.configure(bg='#2C3E50')
    side_fr.configure(bg='#2C3E50')
    txt.config(bg="white", fg="black")
    rslt.config(bg="white", fg="black")
    txt1.config(bg="white", fg="black")
    rslt1.config(bg="white", fg="black")

def black_bg(event=None):
    main_fr.configure(bg='black')
    side_fr.configure(bg='black')
    txt.config(bg="#121212", fg="white")
    rslt.config(bg="#121212", fg="white")
    txt1.config(bg="#121212", fg="white")
    rslt1.config(bg="#121212", fg="white")

f2 = Button()
root.bind('<F2>', hunter_green_bg)

f3 = Button()
root.bind('<F3>', ocean_bg)

f4 = Button()
root.bind('<F4>', black_bg)

f4 = Button()
root.bind('<F4>', navy_bg)

# button colors

def norm_btn(event=None):
    btn.configure(bg="#d72631", fg="#fcf5e5")

def clear_btn(event=None):
    clr.configure(bg="#d72631", fg="#fcf5e5")

def copy_btn(event=None):
    cpy.configure(bg="#d72631", fg="#fcf5e5")

def rnm_btn(event=None):
    rnm.configure(bg="#d72631", fg="#fcf5e5")

def grey_btn(event=None):
    btn.configure(bg="#f0f0f0", fg="black")
    clr.configure(bg="#f0f0f0", fg="black")
    cpy.configure(bg="#f0f0f0", fg="black")
    rnm.configure(bg="#f0f0f0", fg="black")

# buttons and their bindings

clr = Button(main_fr, text="Clear", width=9, command=clear_entry)
clr.grid(row=0,
        column=1,
        sticky="nw",
        pady=(5,5))

clr.bind("<Enter>", clear_btn)
clr.bind("<Leave>", grey_btn)

btn = Button(main_fr, text="Normalize", width=9, command=title_normalizer)
btn.grid(row=0,
        column=1,
        sticky="ws",
        padx=(0,5),
        pady=(0,5))

btn.bind("<Enter>", norm_btn)
btn.bind("<Leave>", grey_btn)

cpy = Button(main_fr, text="Copy",  width=9, command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1,
        column=1,
        sticky="n",
        padx=(0,5))

cpy.bind("<Enter>", copy_btn)
cpy.bind("<Leave>", grey_btn)

rnm = Button(main_fr, text="Rename", width=9, command=lambda:[rename(), clear_entry()])
rnm.grid(row=1,
        column=1,
        sticky="sw",
        pady=(5,0))

rnm.bind("<Enter>", rnm_btn)
rnm.bind("<Leave>", grey_btn)

''' Adding a side frame '''

side_fr = Frame(root, bg='#025a6c')

txt1 = Text(side_fr, font='Calibri 10', height=5, width=25, wrap=WORD)
txt1.focus()
txt1.grid(row=0, column=0, pady=5, padx=5)

rslt1 = Text(side_fr, font=('Calibri 10'), height=5, width=25, wrap=WORD)
rslt1.grid(row=1, column=0)

def get_file_name(event=None):
    global file_directory
    global filename
    global file_ext
    global file_path

    file_path = fd.askopenfilename()
    file_path_components = file_path.split('/')
    file_directory = "/".join(file_path_components[:-1]) + "/"
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)

    filename = file_name_and_extension[0]
    file_ext = file_name_and_extension[1]

    clear_entry1()
    txt1.insert("end", filename)
    txt.insert("end", filename)
    rslt1.delete('1.0', 'end')

def add_underscore():
    global D
    input_txt = txt1.get(1.0, "end-1c")
    D = input_txt
    if " " in D:
        D = D.replace(" ", "_")
    if "-" in D:
        D = D.replace("-", "_")
    else:
        pass

    rslt1.delete('1.0', 'end')
    rslt1.insert("end", D)

def add_hypen():
    global D
    input_txt = txt1.get(1.0, "end-1c")
    D = input_txt
    if " " in D:
        D = D.replace(" ", "-")
    if "_" in D:
        D = D.replace("_", "-")
    else:
        pass

    rslt1.delete('1.0', 'end')
    rslt1.insert("end", D)

def copy_to_clipboard1():
    final_rslt1 = rslt1.get('1.0', 'end-1c')
    cpy1.clipboard_clear()
    cpy1.clipboard_append(final_rslt)

def clear_entry1():
    txt1.delete('1.0', 'end')
    rslt1.config(state="normal")
    rslt1.delete('1.0', 'end')
    
def rename1():
    final_rslt1 = rslt1.get('1.0', 'end-1c')
    D = final_rslt1
    if ":" or "/" or "\\" or "*" or "?" or "<" or ">" or "\"" or "|" in D: # add prohibited symbols here
        W = "The new filename includes characters that are not allowed in naming a file! ( : / \\ * ? <> |)"
        rslt1.delete('1.0', 'end')
        rslt1.insert("end", W)
        rslt1.config(state="disabled")
    else:
        pass
    old_file = f"{file_directory}" + f"{filename}.{file_ext}"
    new_file_2 = f"{file_directory}" + f"{D}.{file_ext}"
    os.rename(old_file, new_file_2)

# button colors

def clear_btn(event=None):
    clr1.configure(bg="#d72631", fg="#fcf5e5")

def und_btn(event=None):
    und1.configure(bg="#d72631", fg="#fcf5e5")

def hyp_btn(event=None):
    hyp1.configure(bg="#d72631", fg="#fcf5e5")

def rnm_btn(event=None):
    rnm1.configure(bg="#d72631", fg="#fcf5e5")

def grey_btn(event=None):
    clr1.configure(bg="#f0f0f0", fg="black")
    und1.configure(bg="#f0f0f0", fg="black")
    hyp1.configure(bg="#f0f0f0", fg="black")
    rnm1.configure(bg="#f0f0f0", fg="black")

# buttons and their bindings

clr1 = Button(side_fr, text="Clear", width=8, command=clear_entry1)
clr1.grid(row=0,
        column=1,
        sticky="nw",
        padx=(0,5),
        pady=(5,5))

clr1.bind("<Enter>", clear_btn)
clr1.bind("<Leave>", grey_btn)

und1 = Button(side_fr, text="Add ( _ )", command=add_underscore)
und1.grid(row=0,
        column=1,
        sticky="wse",
        padx=(0,5),
        pady=(0,5))

und1.bind("<Enter>", und_btn)
und1.bind("<Leave>", grey_btn)

hyp1 = Button(side_fr, text="Add ( - )", command=lambda:[add_hypen()])
hyp1.grid(row=1,
        column=1,
        sticky="new",
        padx=(0,5))

hyp1.bind("<Enter>", hyp_btn)
hyp1.bind("<Leave>", grey_btn)

side_fr.bind('<Control-C>', copy_to_clipboard1)

rnm1 = Button(side_fr, text="Rename", width=8, command=lambda:[rename1(), clear_entry1()])
rnm1.grid(row=1,
        column=1,
        sticky="ws",
        padx=(0,5),
        pady=(5,0))

rnm1.bind("<Enter>", rnm_btn)
rnm1.bind("<Leave>", grey_btn)

def to_side_frame(event=None):
    main_fr.grid_forget()
    side_fr.grid(ipady=2)

def to_main_frame(event=None):
    side_fr.grid_forget()
    main_fr.grid(ipady=2)

# Adding menubar to an app

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)     # ajralib chiqishni oldini olish
filemenu.add_command(label="Open...", command=get_file_name)
filemenu.add_command(label="Info", command=info_popup)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

modemenu = Menu(menubar, tearoff=0)
modemenu.add_command(label="Regular Mode", command=to_main_frame)
modemenu.add_command(label="Developer Mode", command=to_side_frame)

thememenu = Menu(menubar, tearoff=0)
thememenu.add_command(label="Ocean", command=ocean_bg)
thememenu.add_command(label="Hunter Green", command=hunter_green_bg)
thememenu.add_command(label="Navy Blue", command=navy_bg)
thememenu.add_command(label="Black", command=black_bg)

# Adding the File menu to the menubar
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Mode", menu=modemenu)
menubar.add_cascade(label="Theme", menu=thememenu)    # sharshara usulini qo'shish, bu muhim!

root.mainloop()
