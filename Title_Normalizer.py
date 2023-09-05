# 05.09.23 | Refactored the code.

# 04.09.23 | Added a warning window which pops up while a renaming error happens.

# 02.09.23 | Added removing (.) while renameing in Developer Mode
#          | Refactored the code
#          | Fixed small bugs. 

# 19.05.23 | Fixed some bugs; mainly altering the curser color to complement the themes
# 16.05.23 | Made the app screen bigger for easier usage
#          | Removed manual attribution of button color themes, that was too much hassle
#          | Added 2 styles for buttons and clam theme to the app
#          | Removed some redundant code
# 10.05.23 | Changed the cursor color to white in the black theme
# 04.05.23 | Removed some button icons because they were displayed inproperly in some screen resolutions
#          | Added 2 color themes, removed boring grey theme
# 01.04.23 | Made the app window responsive to various screens
# 28.03.23 | 1) Dealt with some syntax errors in renaming; but there are still harmless bugs
#            2) Added renaming ability right from textbox

import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import Menu
from tkinter import ttk
from tkinter.messagebox import showerror
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Title Normalizer")
root.resizable(0,0)

# getting the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# making the app window close to the centre of the screen
iheight = int(screen_width*0.35)
iwidth = int(screen_height*0.3)

root.geometry(f"+{iheight}+{iwidth}")

style = ttk.Style()             # adding a theme
style.theme_use('clam')

style_grey = ttk.Style()        # adding normal button style
style_grey.configure('Grey.TButton')

style_black = ttk.Style()       # adding black button style
style_black.configure('Black.TButton',
                        background='black',
                        foreground='orange',
                        activebackground='black',
                        activeforeground='black',
                        highlightcolor='black')

def info_popup(event=None):
    top = Toplevel(root)
    top.title("About: Title Normalizer v1.9")
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

txt_box = Text(main_fr, font='Calibri 10', height=5.5, width=28, wrap=WORD)
txt_box.focus()
txt_box.grid(row=0, column=0, pady=5, padx=5)

rslt_box = Text(main_fr, font='Calibri 10', height=5.5, width=28, wrap=WORD)
rslt_box.grid(row=1, column=0)

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

    clear_entries()
    txt_box.insert("end", filename)
    rslt_box.delete('1.0', 'end')

root.bind("<Control-o>", get_file_name)     # adding a shortcut for opening a file

def normalize(event=None):
    global T
    input_txt = txt_box.get(1.0, "end-1c")
    T = input_txt

    if "_" or "-" or "." or "  " in T:
        T = T.replace("_", " ")
        T = T.replace("-", " ")
        T = T.replace(".", " ")
        T = T.replace("  ", " ")

    rslt_box.delete('1.0', 'end')
    rslt_box.insert("end", T)

def copy_to_clipboard():
    global F
    final_rslt = rslt_box.get('1.0', 'end-1c')
    F = final_rslt
    cpy.clipboard_clear()
    cpy.clipboard_append(F)

def clear_entries():
    txt_box.delete('1.0', 'end')
    rslt_box.delete('1.0', 'end')
    txt_box_s.delete('1.0', 'end')
    rslt_box_s.delete('1.0', 'end')

def rename():
    new_filename = rslt_box.get('1.0', 'end-1c')

    try:
        old_file = f"{file_directory}{filename}.{file_ext}"
        new_file = f"{file_directory}{new_filename}.{file_ext}"
        os.rename(old_file, new_file)
    except OSError:
        warning_message = "A filename cannot include these characters : / \\ * ? <> |"
        showerror(title="Renaming Error", message=warning_message)

# adding buttons

clr = ttk.Button(main_fr, text="Clear", width=9, command=clear_entries)
clr.grid(row=0,
        column=1,
        sticky="nw",
        pady=(5,5))

btn = ttk.Button(main_fr, text="Normalize", width=9, command=normalize)
btn.grid(row=0,
        column=1,
        sticky="ws",
        padx=(0,5),
        pady=(0,5))

cpy = ttk.Button(main_fr, text="Copy",  width=9, command=lambda:[copy_to_clipboard(), clear_entries()])
cpy.grid(row=1,
        column=1,
        sticky="n",
        padx=(0,5))

rnm = ttk.Button(main_fr, text="Rename", width=9, command=lambda:[rename(), clear_entries()])
rnm.grid(row=1,
        column=1,
        sticky="sw",
        pady=(5,0))

''' Adding a side frame '''

side_fr = Frame(root, bg='#025a6c')

txt_box_s = Text(side_fr, font='Calibri 10', height=5.5, width=28, wrap=WORD)
txt_box_s.focus()
txt_box_s.grid(row=0, column=0, pady=5, padx=5)

rslt_box_s = Text(side_fr, font=('Calibri 10'), height=5.5, width=28, wrap=WORD)
rslt_box_s.grid(row=1, column=0)

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

    clear_entries()
    txt_box_s.insert("end", filename)
    txt_box.insert("end", filename)
    rslt_box_s.delete('1.0', 'end')

def add_underscore():
    global D
    input_txt = txt_box_s.get(1.0, "end-1c")
    D = input_txt

    if "." in D:
        D = D.replace(".", "")
    if " " in D:
        D = D.replace(" ", "_")
    if "-" in D:
        D = D.replace("-", "_")

    rslt_box_s.delete('1.0', 'end')
    rslt_box_s.insert("end", D)

def add_hypen():
    global D
    input_txt = txt_box_s.get(1.0, "end-1c")
    D = input_txt
    D = D.rstrip(",")

    if "." in D:
        D = D.replace(".", "")
    if " " in D:
        D = D.replace(" ", "-")
    if "_" in D:
        D = D.replace("_", "-")

    rslt_box_s.delete('1.0', 'end')
    rslt_box_s.insert("end", D)
    
def rename_s():
    new_filename_s = rslt_box_s.get('1.0', 'end-1c')

    try:
        old_file = f"{file_directory}{filename}.{file_ext}"
        new_file = f"{file_directory}{new_filename_s}.{file_ext}"
        os.rename(old_file, new_file)
    except OSError:
        warning_message = "A filename cannot include these characters : / \\ * ? <> |"
        showerror(title="Renaming Error", message=warning_message)

# buttons and their bindings

clr_s = ttk.Button(side_fr, text="Clear", width=8, command=clear_entries())
clr_s.grid(row=0,
        column=1,
        sticky="nw",
        padx=(0,5),
        pady=(5,5))

und_s = ttk.Button(side_fr, text="Add ( _ )", width=8, command=add_underscore)
und_s.grid(row=0,
        column=1,
        sticky="wse",
        padx=(0,5),
        pady=(0,5))

hyp_s = ttk.Button(side_fr, text="Add ( - )", width=8, command=lambda:[add_hypen()])
hyp_s.grid(row=1,
        column=1,
        sticky="new",
        padx=(0,5))

rnm_s = ttk.Button(side_fr, text="Rename", width=8, command=lambda:[rename_s(), clear_entries()])
rnm_s.grid(row=1,
        column=1,
        sticky="ws",
        padx=(0,5),
        pady=(5,0))

def to_side_frame(event=None):
    main_fr.grid_forget()
    side_fr.grid(ipady=2)

def to_main_frame(event=None):
    side_fr.grid_forget()
    main_fr.grid(ipady=2)

# adding color themes

def ocean_bg(event=None):
    main_fr.config(bg='#025a6c')
    txt_box.config(bg="white", fg="black")
    rslt_box.config(bg="white", fg="black")
    txt_box.config(insertbackground="black")
    rslt_box.config(insertbackground="black")

    side_fr.config(bg='#025a6c')
    txt_box_s.config(bg="white", fg="black")
    rslt_box_s.config(bg="white", fg="black")
    txt_box_s.config(insertbackground="black")
    rslt_box_s.config(insertbackground="black")

    clr['style'] = 'Grey.TButton'
    btn['style'] = 'Grey.TButton'
    cpy['style'] = 'Grey.TButton'
    rnm['style'] = 'Grey.TButton'
    
    clr_s['style'] = 'Grey.TButton'
    und_s['style'] = 'Grey.TButton'
    hyp_s['style'] = 'Grey.TButton'
    rnm_s['style'] = 'Grey.TButton'

def hunter_green_bg(event=None):
    main_fr.config(bg='#355E3B')
    txt_box.config(bg="white", fg="black")
    rslt_box.config(bg="white", fg="black")
    txt_box.config(insertbackground="black")
    rslt_box.config(insertbackground="black")
    
    side_fr.config(bg='#355E3B')
    txt_box_s.config(bg="white", fg="black")
    rslt_box_s.config(bg="white", fg="black")
    txt_box_s.config(insertbackground="black")
    rslt_box_s.config(insertbackground="black")

    clr['style'] = 'Grey.TButton'
    btn['style'] = 'Grey.TButton'
    cpy['style'] = 'Grey.TButton'
    rnm['style'] = 'Grey.TButton'

    clr_s['style'] = 'Grey.TButton'
    und_s['style'] = 'Grey.TButton'
    hyp_s['style'] = 'Grey.TButton'
    rnm_s['style'] = 'Grey.TButton'

def navy_bg(event=None):
    main_fr.config(bg='#2C3E50')
    txt_box.config(bg="white", fg="black")
    rslt_box.config(bg="white", fg="black")
    txt_box.config(insertbackground="black")
    rslt_box.config(insertbackground="black")
    
    side_fr.config(bg='#2C3E50')
    txt_box_s.config(bg="white", fg="black")
    rslt_box_s.config(bg="white", fg="black")
    txt_box_s.config(insertbackground="black")
    rslt_box_s.config(insertbackground="black")

    clr['style'] = 'Grey.TButton'
    btn['style'] = 'Grey.TButton'
    cpy['style'] = 'Grey.TButton'
    rnm['style'] = 'Grey.TButton'

    clr_s['style'] = 'Grey.TButton'
    und_s['style'] = 'Grey.TButton'
    hyp_s['style'] = 'Grey.TButton'
    rnm_s['style'] = 'Grey.TButton'

def black_bg(event=None):
    main_fr.config(bg='black')
    txt_box.config(bg="#121212", fg="white")
    rslt_box.config(bg="#121212", fg="white")
    txt_box.config(insertbackground="white")
    rslt_box.config(insertbackground="white")
    
    side_fr.config(bg='black')
    txt_box_s.config(bg="#121212", fg="white")
    rslt_box_s.config(bg="#121212", fg="white")
    txt_box_s.config(insertbackground="white")
    rslt_box_s.config(insertbackground="white")
    
    clr['style'] = 'Black.TButton'
    btn['style'] = 'Black.TButton'
    cpy['style'] = 'Black.TButton'
    rnm['style'] = 'Black.TButton'

    clr_s['style'] = 'Black.TButton'
    hyp_s['style'] = 'Black.TButton'
    und_s['style'] = 'Black.TButton'
    rnm_s['style'] = 'Black.TButton'

f2 = Button()
root.bind('<F2>', hunter_green_bg)

f3 = Button()
root.bind('<F3>', ocean_bg)

f4 = Button()
root.bind('<F4>', black_bg)

f4 = Button()
root.bind('<F4>', navy_bg)

# adding menubar to the app

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
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
menubar.add_cascade(label="Theme", menu=thememenu)

root.mainloop()
