from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Notepad 1.0 - by Ryumasu')
root.geometry('800x450')

main_menu = Menu(root)

# Functions
def notepad_exit():
    root.destroy()

def notepad_open_file():
    file_path = filedialog.askopenfilename(title='Choose File', filetypes=(('Text Documents (*.txt)', '*txt'), ('All Files', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())

def notepad_save_file():
    file_path = filedialog.asksaveasfilename(title='Choose File',filetypes=(('Text Documents (*.txt)', '*txt'), ('All Files', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()

def text_select_all():
    text_field.tag_add(SEL, "1.0", END)

def text_delete_all():
    text_field.delete('1.0', END)

# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open...", command=notepad_open_file)
file_menu.add_command(label="Save As", command=notepad_save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=notepad_exit)

# Edit
edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete", command=text_delete_all)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=text_select_all)

# Style
style_menu = Menu(main_menu, tearoff=0)

root.config(menu=file_menu)
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='Style', menu=style_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_field = Text(f_text, bg="white", fg="black", padx=5, pady=5, wrap=WORD, insertbackground='black', selectbackground="#989898")
text_field.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()
