from  tkinter import*
from tkinter.filedialog import *
from tkinter.messagebox import*
from tkinter.font import Font
from tkinter.scrolledtext import*
import file_menu
import edit_menu
import format_menu
import help_menu

root = Tk()
# Label.config(font = ("Courier", 44))
root.title("My Notepad - Mayank")
root.geometry("600x550+250+250")
root.minsize(width=400, height=400)
text = ScrolledText(root, state='normal', height = 400, width = 400, wrap = 'word', pady = 2, padx = 3, undo = True)
text.pack(fill = Y, expand = 1)
text.focus_set()
menubar = Menu(root)
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)


root.mainloop()
