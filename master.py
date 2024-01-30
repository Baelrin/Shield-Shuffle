import tkinter

from tkinter import messagebox
from random import randint

root = tkinter.Tk()
root.title('Shield-Shuffle')
root.iconbitmap('gui/shield-shuffle.ico')
root.geometry('500x300')

def new_rand():
    """Generates a new random password"""
    try:
        pw_entry.delete(0, tkinter.END)
        pw_length = int(my_entry.get())
        if pw_length < 1 or pw_length > 300:
            raise ValueError("Number of characters is incorrect. Should be 1 — 300 chars.")
        my_password = ''.join(chr(randint(33, 126)) for _ in range(pw_length))
        pw_entry.insert(0, my_password)
    except ValueError:
        messagebox.showinfo("What are you doing?", 'ONLY DIGITS')
    except Exception as e:
        messagebox.showinfo("Unexpected Error", f'An unexpected error occurred: {str(e)}')

def clipper():
    if pw_entry.get() == '':
        messagebox.showinfo("I hate you", "Password field is empty like your head!")
    else:
        root.clipboard_clear()
        root.clipboard_append(pw_entry.get())
        messagebox.showinfo(
            "Well...", "Password copied to clipboard, don't forget to send to hacker!")


label_frame = tkinter.LabelFrame(root, text="How Many Characters? (1 — 300)")
label_frame.pack(pady=20)

my_entry = tkinter.Entry(label_frame, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)

pw_entry = tkinter.Entry(root, font=('Helvetica', 24), bd=0, bg="systembuttonface")
pw_entry.insert(0, '')
pw_entry.pack(pady=20)

my_frame = tkinter.Frame(root)
my_frame.pack(pady=20)

my_button = tkinter.Button(
    my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = tkinter.Button(
    my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

try:
    root.mainloop()
except Exception as e:
    messagebox.showinfo("Unexpected Error",
                        f'An unexpected error occurred: {str(e)}')
