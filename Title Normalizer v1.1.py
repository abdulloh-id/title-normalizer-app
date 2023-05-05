import tkinter
import re
from tkinter import *
from ctypes import windll
import math

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
center_x = int(screen_width/2)
center_y = int(screen_height/2)

win_size_width = int(screen_width/50)
win_size_height = int(screen_height/110)

# set the position of the window to the center of the screen
oyna.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

oyna.attributes('-topmost', 1)    
oyna.resizable(False, False)            
oyna['background'] = '#025a6c'

txt = Text(oyna, width=f"{win_size_width}", height=f"{win_size_height}", font='Calibri 10',  wrap=WORD)
txt.focus()
txt.grid(row=0, column=0, pady=5, padx=5)

rslt = Text(oyna, width=f"{win_size_width}", height=f"{win_size_height}", font=('Calibri 10'),  wrap=WORD)
rslt.grid(row=1, column=0)

def underscore_remover():
	input_txt = txt.get(1.0, "end-1c")
	title_txt = re.split("_", input_txt)
	join_txt = ' '.join(title_txt)

	print(join_txt)

	re_title = join_txt.replace(".", " ")
	re_title_join = ''.join(re_title)

	print(re_title_join)

	split_txt = re_title_join.split()
	final_txt = ' '.join(split_txt)

	rslt.delete('1.0', 'end')
	rslt.insert("end", final_txt)

def copy_to_clipboard():
    final_rslt = rslt.get('1.0', 'end-1c')
    cpy.clipboard_clear()
    cpy.clipboard_append(final_rslt)

def clear_entry():
    txt.delete('1.0', 'end')
    rslt.delete('1.0', 'end')

def info_popup(event=0):
    top = Toplevel(oyna)
    top.geometry('500x300')
    top.title("About: Title Normalizer v1.1")
    Label(top, text="\n ©️ This program is made by Abdulloh Abdusamadov.\n").pack()

oyna.bind('<F1>', info_popup)

btn = Button(oyna, width=10, height=1, text="Normalize", command=underscore_remover)
btn.grid(row=0, column=1, sticky="s", padx=(0,5))

clr = Button(oyna, text="Clear", width=2, command=clear_entry)
clr.grid(row=0, column=1, sticky="new", padx=(0,5), pady=5)

cpy = Button(oyna, text="Copy", width=2, command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=1, sticky="sew", padx=(0,5))

oyna.mainloop()