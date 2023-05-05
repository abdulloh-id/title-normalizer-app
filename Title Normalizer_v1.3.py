import tkinter
import re
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os 
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

oyna = Tk()
oyna.title("Title Normalizer")
oyna.geometry('400x300')

window_width = 350
window_height = 275

# get the screen dimension
screen_width = oyna.winfo_screenwidth()
screen_height = oyna.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

win_size_width = int(screen_width/50) #responsive window width
win_size_height = int(screen_height/110) #responsive window height

# set the position of the window to the center of the screen
oyna.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

oyna.attributes('-topmost', 1)    
oyna.resizable(False, False)            
oyna['background'] = '#316879' # teal 

txt = Text(oyna, width=f"{win_size_width}", height=f"{win_size_height}", font='Calibri 10',  wrap=WORD)
txt.focus()
txt.grid(row=0, column=0, pady=5, padx=5)

rslt = Text(oyna, width=f"{win_size_width}", height=f"{win_size_height}", font=('Calibri 10'),  wrap=WORD)
rslt.grid(row=1, column=0)

def get_file_name():
    file_path = fd.askopenfilename()
    file_path_components = file_path.split('/')
    file_name_and_extension = file_path_components[-1].rsplit('.', 1)
    filename = file_name_and_extension[0]
    
    txt.delete('1.0', 'end')
    txt.insert("end", filename)

def underscore_remover():
    input_txt = txt.get(1.0, "end-1c")
    title_split_txt = re.split("_", input_txt)
    join_txt = ' '.join(title_split_txt)

    re_title = join_txt.replace(".", " ")
    re_title_join = ''.join(re_title)

    split_txt = re_title_join.split()
    pre_final_txt = ' '.join(split_txt)
    S = pre_final_txt.split()

    S = ' '.join(S)

    rslt.delete('1.0', 'end')
    rslt.insert("end", S)

def add_underscore():
    input_txt = txt.get(1.0, "end-1c")
    S = input_txt
    if " " in S:
        S = S.replace(" ", "_")

    rslt.delete('1.0', 'end')
    rslt.insert("end", S)

def copy_to_clipboard():
    final_rslt = rslt.get('1.0', 'end-1c')
    cpy.clipboard_clear()
    cpy.clipboard_append(final_rslt)

def clear_entry():
    txt.delete('1.0', 'end')
    rslt.delete('1.0', 'end')

def info_popup(event=None):
    top = Toplevel(oyna)
    top.geometry('700x500')
    top.title("About: Title Normalizer v1.3")
    Label(top, justify = "left", text="\nInfo:\
    \n✅ Bu programma orasida tagchiziq yoki nuqta bilan ajratilgan sarlavhalarni toʻgʻrilab yozib beradi.\
    \n✅ Bu ilovadan sarlavhalarni oson yozishda ham foydalanishingiz mumkin. \n\
    \nIlovadan foydalanish yoʻriqnomasi:\
    \n 1-usul: Oʻzingiz istagan sarlavhani buferga koʻchirib oling va uni birinchi matn maydoniga kiriting.\
    \n 2-usul: Fayl menejer orqali kerakli faylni tanlang, buning uchun «Choose file» tugmasini bosing.\
    \n • Fayl nomini toʻgʻrilash uchun «Normalize» tugmasini bosing.\
    \n • Matn maydonini tozalash uchun «Clear» tugmasini bosing.\
    \n • Tayyor boʻlgan matnni buferga ko'chirib olish uchun «Copy» tugmasini bosing. \n\
    \n'Bufer'ni chiqarish uchun Win+V tugmalarini birgalikda bosing.\n\
    \nBogʻlanish uchun kontaktlar:\
    \n🔗 Telegram: @Abdulloh_ID\
    \n🔗 Email: outergamer11@gmail.com").pack()
    Label(top, justify = "left", text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack()

oyna.bind('<F1>', info_popup)

# themes

def grey_bg(event=None):
    oyna.configure(bg='grey') 

def teal_bg(event=None):
    oyna.configure(bg='#316879')

f2 = Button()
oyna.bind('<F2>', grey_bg)

f3 = Button()
oyna.bind('<F3>', teal_bg)

# button colors

def norm_btn(event=None):
    btn.configure(bg="#d72631", fg="#fcf5e5")

def clear_btn(event=None):
    clr.configure(bg="#d72631", fg="#fcf5e5")

def copy_btn(event=None):
    cpy.configure(bg="#d72631", fg="#fcf5e5")

def fch_btn(event=None):
    fch.configure(bg="#d72631", fg="#fcf5e5")

def grey_btn(event=None):
    btn.configure(bg="#f0f0f0", fg="black")
    fch.configure(bg="#f0f0f0", fg="black")
    clr.configure(bg="#f0f0f0", fg="black")
    cpy.configure(bg="#f0f0f0", fg="black")

clr = Button(oyna, text="Clear", width=2, command=clear_entry)
clr.grid(row=0, column=1, sticky="new", padx=(0,5), pady=5)

clr.bind("<Enter>", clear_btn)
clr.bind("<Leave>", grey_btn)

fch = Button(oyna, width=10, height=1, text="Choose file", command=get_file_name)
fch.grid(row=0, column=1, sticky="s", padx=(0,5), pady=(0,5))

fch.bind("<Enter>", fch_btn)
fch.bind("<Leave>", grey_btn)

btn = Button(oyna, width=10, height=1, text="Normalize", command=underscore_remover)
btn.grid(row=1, column=1, sticky="n", padx=(0,5), pady=(0,5))

btn.bind("<Enter>", norm_btn)
btn.bind("<Leave>", grey_btn)

cpy = Button(oyna, text="Copy", width=2, command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=1, sticky="sew", padx=(0,5))

cpy.bind("<Enter>", copy_btn)
cpy.bind("<Leave>", grey_btn)

oyna.mainloop()

# burnt sienna #c66b3d
# navy #1e3d59