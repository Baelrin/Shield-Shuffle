import tkinter
import string
from tkinter import messagebox
from random import randint

root = tkinter.Tk()
root.title('Shield-Shuffle')  # Sets window title.
root.iconbitmap('gui/shield-shuffle.ico')  # Sets window icon.
root.geometry('500x500')  # Sets window size.

# Create a BooleanVar variable to store the state of the checkbox
sensitive_chars_var = tkinter.BooleanVar()

# Create a container for the checkbox
checkbox_container = tkinter.Frame(root)
checkbox_container.grid(row=0, column=0, padx=20, pady=20)

# Create a checkbox in the user interface
# Checkbox text: "Exclude sensitive characters"
# Link the checkbox to the variable sensitive_chars_var
sensitive_chars_checkbox = tkinter.Checkbutton(
    checkbox_container, text="Exclude sensitive characters", variable=sensitive_chars_var)
sensitive_chars_checkbox.pack()

# Create a container for the buttons
buttons_container = tkinter.Frame(root)
buttons_container.grid(row=1, column=0, padx=20, pady=20)


def new_rand():
    """Generates a new random password and displays it in the GUI."""
    try:
        pw_entry.delete(0, tkinter.END)  # Clears the password field.
        pw_length = int(my_entry.get())  # Retrieves desired password length.
        if pw_length < 1 or pw_length > 300:
            raise ValueError(
                "Number of characters is incorrect. Should be 1 — 300 chars and ONLY DIGITS.")
        if sensitive_chars_var.get():
            # Exclude sensitive characters
            my_password = ''.join(chr(randint(33, 126)) for _ in range(
                pw_length) if chr(randint(33, 126)) not in string.punctuation)
        else:
            # Include all characters
            my_password = ''.join(chr(randint(33, 126))
                                  for _ in range(pw_length))
        pw_entry.insert(0, my_password)  # Displays generated password.
    except ValueError:  # Handles invalid input for password length.
        messagebox.showinfo("What are you doing?",
                            'Should be 1 — 300 chars and ONLY DIGITS.')
    except Exception as e:  # Handles unexpected errors.
        messagebox.showinfo("Unexpected Error",
                            f'An unexpected error occurred: {str(e)}')


# Create a button to generate a new random password
generate_button = tkinter.Button(
    buttons_container, text='Generate Strong Password', command=new_rand)
generate_button.grid(row=0, column=0, padx=10)


def clipper():
    """Copies the generated password to clipboard if not empty, shows a messagebox otherwise."""
    if pw_entry.get() == '':
        messagebox.showinfo(
            "I hate you", "Password field is empty!")
    else:
        root.clipboard_clear()  # Clears clipboard.
        # Copies the password to clipboard.
        root.clipboard_append(pw_entry.get())
        messagebox.showinfo(
            "Well...", "Password copied to clipboard, don't forget to send it to hacker!")


# Create a button to copy the generated password to clipboard
copy_button = tkinter.Button(
    buttons_container, text='Copy to Clipboard', command=clipper)
copy_button.grid(row=0, column=1, padx=10)

# Creates a label frame to ask for desired password length.
label_frame = tkinter.LabelFrame(root, text="How Many Characters? (1 — 300)")
label_frame.grid(row=2, column=0, padx=20, pady=20)

# Creates an entry widget for inputting desired password length.
my_entry = tkinter.Entry(label_frame, font=('Helvetica', 24))
my_entry.grid(row=0, column=0, padx=20, pady=20)

# Creates an entry widget to display the generated password.
pw_entry = tkinter.Entry(root, font=('Helvetica', 24),
                         bd=0, bg="systembuttonface")
pw_entry.insert(0, '')  # Ensures the password field is empty at the start.
pw_entry.grid(row=3, column=0, padx=20, pady=20)

try:
    root.mainloop()  # Enters the tkinter main event loop.
except Exception as e:  # Handles unexpected errors during execution.
    messagebox.showinfo("Unexpected Error",
                        f'An unexpected error occurred: {str(e)}')
