import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
window=tk.Tk()
window.title("Notepad")
window.geometry("600x600")
#window.resizable(0,0)

#define fonts and colours

text_color = "#fffacd"
menu_color = "#dbd9db"
window_color = "#6c809a"
window.configure(bg = window_color)

#define functions


def openfile():
    file_path = askopenfilename(filetypes = [("text files", "*.txt"), ("all files", "*.*")])
    if not file_path:
        return
    input_text.delete("1.0", tk.END)
    with open(file_path, "r") as f:
        fontStyleVar.set(f.readline().strip())
        fontSizeVar.set(f.readline().strip())
        fontFamilyVar.set(f.readline().strip())
        changefont(1)
        text = f.read()
        input_text.insert("1.0", text)
    
def savefile():
    file_path = asksaveasfilename(defaultextension = "txt", filetypes = [("text files", "*.txt"), ("all files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as write_file:
        text = input_text.get("1.0","end")
        write_file.write(fontStyleVar.get() + "\n")
        write_file.write(str(fontSizeVar.get())+"\n")
        write_file.write(fontFamilyVar.get()+"\n")
        write_file.write(text)
    
def changefont(event):
    #change the font based on font drop down options
    if fontStyleVar.get() == "Normal":
        my_font = (fontFamilyVar.get(), fontSizeVar.get())
    else:
        my_font = (fontFamilyVar.get(), fontSizeVar.get(), fontStyleVar.get())
    input_text.config(font = my_font, fg = fontColorVar.get())
"""
def changecolor(event):
    if fontColorVar.get() == "Black":
        my_font = (fontColorVar.get()
"""
def newfile():
    answer = messagebox.askyesno("New Note", "Do you want open a new note?")
    if answer == 1:
        input_text.delete("1.0","end")

def closeapp():
    answer = messagebox.askyesno("Close file","Are you sure you would like to close this file?")
    if answer == 1:
        window.destroy()

def style():
    fontStyleVar = StringVar()
    fontStyleVar.set("Normal")
    my_font = (fontFamilyVar.get(), fontSizeVar.get())
#define layout and frame

menu_frame = tk.Frame(window, bg = menu_color)
text_frame = tk.Frame(window, bg = text_color)
menu_frame.pack(padx = 5, pady = 5)
text_frame.pack(padx = 5, pady = 5)
new_btn = tk.Button(menu_frame, text = "New", command = newfile).grid(row = 0, column = 0, padx = 5, pady = 5)
open_btn = tk.Button(menu_frame, text = "Open", command = openfile ).grid(row = 0, column=1, padx = 5, pady = 5)
save_btn = tk.Button(menu_frame, text = "Save as", command = savefile).grid(row = 0, column = 2, padx = 5, pady = 5)
close_btn = tk.Button(menu_frame, text = "Close", command = closeapp).grid(row = 0, column = 3, padx =5, pady=5)
#bold_btn = tk.Button(menu_frame, text = "Bold", command = style).grid(row = 0, column = 7,padx =5, pady=5)
fontFamilyVar = StringVar()
font_family = ['Verdana',
               'Calibri',
               'Arial',
               'Times New Roman',
               'Cambria']
fontFamilyVar.set("Verdana")
fontfamily = tk.OptionMenu(menu_frame, fontFamilyVar, *font_family, command = changefont)
fontfamily.grid(row = 0, column = 4, padx = 5, pady = 5)
fontSizeVar = IntVar()
font_size = [8,10,12,14,16,18,20,24,26,32,64]
fontSizeVar.set(8)
fontsize = tk.OptionMenu(menu_frame, fontSizeVar, *font_size, command = changefont).grid(row = 0, column = 5)
fontStyleVar = StringVar()
font_style = ["Normal","bold", 	"italic", "underline"]
fontStyleVar.set("Normal")
fontstyle = tk.OptionMenu(menu_frame, fontStyleVar, *font_style, command = changefont).grid(row=0, column =6)
my_font = (fontFamilyVar.get(), fontSizeVar.get())

fontColorVar = StringVar()

font_Color = ['Black',
              'Red',
              'Blue',
              'Green',
              'Yellow']
              
fontColor = tk.OptionMenu(menu_frame, fontColorVar, *font_Color, command = changefont)
fontColor.grid(row = 0, column = 7, padx = 5, pady = 5)

input_text = scrolledtext.ScrolledText(text_frame, width = 1000, height = 100, bg = text_color, font = my_font)
input_text.pack()
window.mainloop()  
