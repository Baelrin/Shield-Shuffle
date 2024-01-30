from tkinter import * #TODO Заменить wildcard импорт на нормальный
from random import randint

root = Tk()
root.title('Shield-Shuffle')
root.iconbitmap('gui/shield-shuffle.ico')
root.geometry('500x300')

def new_rand(): #TODO Ограничить количество генерации до 40 символов
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password = ''
    
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
        
    pw_entry.insert(0, my_password)


def clipper(): #TODO Сообщение об успешном копировании
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

label_frame = LabelFrame(root, text="How Many Characters? (1 — 40)")
label_frame.pack(pady=20)

my_entry = Entry(label_frame, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=('Helvetica', 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)


my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()