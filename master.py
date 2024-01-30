import tkinter

from tkinter import messagebox
from random import randint

root = tkinter.Tk()
root.title('Shield-Shuffle')
root.iconbitmap('gui/shield-shuffle.ico')
root.geometry('500x300')


def new_rand():
    pw_entry.delete(0, tkinter.END)
    pw_length = my_entry.get()
    if not pw_length.isdigit() or int(pw_length) < 1 or int(pw_length) > 40:
        messagebox.showinfo(
            "What are you doing?", "Number of characters is incorrect. Should be 1 — 40 chars and ONLY digits.")
        return
    my_password = ''

    for x in range(int(pw_length)):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)


def clipper():
    if pw_entry.get() == '':
        messagebox.showinfo("I hate you", "Password field is empty like your head!")
    else:
        root.clipboard_clear()
        root.clipboard_append(pw_entry.get())
        messagebox.showinfo(
            "Well...", "Password copied to clipboard, don't forget to send to hacker!")


label_frame = tkinter.LabelFrame(root, text="How Many Characters? (1 — 40)")
label_frame.pack(pady=20)

my_entry = tkinter.Entry(label_frame, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)

pw_entry = tkinter.Entry(root, text='', font=(
    'Helvetica', 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame = tkinter.Frame(root)
my_frame.pack(pady=20)

my_button = tkinter.Button(
    my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = tkinter.Button(
    my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
