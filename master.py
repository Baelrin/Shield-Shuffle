import tkinter

from tkinter import messagebox
from random import randint

root = tkinter.Tk()
root.title('Shield-Shuffle')  # Sets window title.
root.iconbitmap('gui/shield-shuffle.ico')  # Sets window icon.
root.geometry('500x300')  # Sets window size.

def new_rand():
    """Generates a new random password and displays it in the GUI."""
    try:
        pw_entry.delete(0, tkinter.END)  # Clears the password field.
        pw_length = int(my_entry.get())  # Retrieves desired password length.
        if pw_length < 1 or pw_length > 300:
            raise ValueError("Number of characters is incorrect. Should be 1 — 300 chars.")
        my_password = ''.join(chr(randint(33, 126)) for _ in range(pw_length))  # Generates password.
        pw_entry.insert(0, my_password)  # Displays generated password.
    except ValueError:  # Handles invalid input for password length.
        messagebox.showinfo("What are you doing?", 'ONLY DIGITS')
    except Exception as e:  # Handles unexpected errors.
        messagebox.showinfo("Unexpected Error", f'An unexpected error occurred: {str(e)}')

def clipper():
    """Copies the generated password to clipboard if not empty, shows a messagebox otherwise."""
    if pw_entry.get() == '':
        messagebox.showinfo("I hate you", "Password field is empty like your head!")
    else:
        root.clipboard_clear()  # Clears clipboard.
        root.clipboard_append(pw_entry.get())  # Copies the password to clipboard.
        messagebox.showinfo(
            "Well...", "Password copied to clipboard, don't forget to send it to hacker!")

# Creates a label frame to ask for desired password length.
label_frame = tkinter.LabelFrame(root, text="How Many Characters? (1 — 300)")
label_frame.pack(pady=20)  # Adds padding to place the frame.

# Creates an entry widget for inputting desired password length.
my_entry = tkinter.Entry(label_frame, font=('Helvetica', 24))
my_entry.pack(pady=20, padx=20)  # Adds padding to place the entry box.

# Creates an entry widget to display the generated password.
pw_entry = tkinter.Entry(root, font=('Helvetica', 24), bd=0, bg="systembuttonface")
pw_entry.insert(0, '')  # Ensures the password field is empty at the start.
pw_entry.pack(pady=20)  # Adds padding to place the password display box.

# Creates a frame to hold buttons.
my_frame = tkinter.Frame(root)
my_frame.pack(pady=20)  # Adds padding to place the frame.

# Creates a button to generate a new random password.
my_button = tkinter.Button(
    my_frame, text='Generate Strong Password', command=new_rand)
my_button.grid(row=0, column=0, padx=10)  # Places the button in the grid layout with padding.

# Creates a button to copy the generated password to clipboard.
clip_button = tkinter.Button(
    my_frame, text='Copy to Clipboard', command=clipper)
clip_button.grid(row=0, column=1, padx=10)  # Places the button next to the generate button with padding.

try:
    root.mainloop()  # Enters the tkinter main event loop.
except Exception as e:  # Handles unexpected errors during execution.
    messagebox.showinfo("Unexpected Error",
                        f'An unexpected error occurred: {str(e)}')