
from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator


def translate_it():
        translator = Translator()
        output = translator.translate(text=original_txt.get(1.0,END), dest=translated_combo.get())
        translated_txt.delete(1.0, END)
        translated_txt.insert(END, output.text)


def clear():
    original_txt.delete(1.0,END)
    translated_txt.delete(1.0, END)


languages = googletrans.LANGUAGES
lang_list = list(languages.values())


root = Tk()
root.title("Translator")
root.geometry("800x600")
root.resizable(False, False)
icon_image = PhotoImage(file="translator.png")
root.iconphoto(False,icon_image)

original_txt = Text(root, width=36, height=20, borderwidth=5, relief=RIDGE, bg="#ebf7f7")
original_txt.place(x=10, y=100)

translated_txt = Text(root, width=36, height=20, borderwidth=5, relief=RIDGE, bg="#ebf7f7")
translated_txt.place(x=410, y=100)

translate_button = Button(root, text="Translate", relief=RIDGE, borderwidth=3,
                          font=('verdana', 10, 'bold'),
                          command=translate_it)
translate_button.place(x=160, y=460)

clear_button = Button(root, text="Clear", relief=RIDGE, borderwidth=3,
                      font=('verdana', 10, 'bold'),
                      command=clear)
clear_button.place(x=580, y=460)

original_combo = ttk.Combobox(root,width=38,font=('verdana', 10, 'bold'), values=lang_list)
original_combo.place(x=12, y=80)
original_combo.current(21)

translated_combo = ttk.Combobox(root,width=38,font=('verdana', 10, 'bold'), values=lang_list)
translated_combo.place(x=411, y=80)
translated_combo.set("Select language")

root.mainloop()