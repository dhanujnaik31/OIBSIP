import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        length = int(length_entry.get())
        letters_required = letters_var.get()
        symbols_required = symbols_var.get()
        digits_required = digits_var.get()
    except:
        messagebox.showerror(message="Please key in the required inputs")
        return

    character_string = ""
    if letters_required == 1:
        character_string += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if symbols_required == 1:
        character_string += "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    if digits_required == 1:
        character_string += "0123456789"

    if len(character_string) == 0:
        messagebox.showerror(message="Please select at least one character type")
        return

    password = []
    if letters_required == 1:
        password += random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", random.randint(1, length))
    if symbols_required == 1:
        password += random.sample("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~", random.randint(1, length))
    if digits_required == 1:
        password += random.sample("0123456789", random.randint(1, length))

    for _ in range(length - len(password)):
        password.append(random.choice(character_string))

    random.shuffle(password)
    password = ''.join(password)

    password_strength = "Weak"
    password_color = "red"
    if length >= 12 and letters_required == 1 and symbols_required == 1 and digits_required == 1:
        password_strength = "Strong"
        password_color = "green"
    elif length >= 8 and (letters_required == 1 or symbols_required == 1 or digits_required == 1):
        password_strength = "Medium"
        password_color = "blue"

    password_v = StringVar()
    password = "Generated password: " + str(password) + "\nPassword Strength: " + password_strength
    password_v.set(password)


    password_label = Label(password_gen, textvariable=password_v, font=('Arial', 12), fg=password_color)
    password_label.place(x=10, y=200, height=100, width=320)

character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

password_gen = Tk()
password_gen.geometry("450x300")
password_gen.title("Password Generator")

title_label = Label(password_gen, text="Password Generator", font=('Arial', 14,))
title_label.pack()

length_label = Label(password_gen, text="Enter length of password: ", font=('Arial', 14),anchor="center")
length_label.place(x=20, y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=250, y=30)

letters_var = IntVar()
letters_label = Label(password_gen, text="Require letters?", font=('Arial', 14),anchor="center")
letters_label.place(x=20, y=60)
letters_checkbox = Checkbutton(password_gen, variable=letters_var, font=('Arial', 14))
letters_checkbox.place(x=200, y=60)

symbols_var = IntVar()
symbols_label = Label(password_gen, text="Require symbols?", font=('Arial', 14),anchor="center")
symbols_label.place(x=20, y=90)
symbols_checkbox = Checkbutton(password_gen, variable=symbols_var, font=('Arial', 14))
symbols_checkbox.place(x=200, y=90)

digits_var = IntVar()
digits_label = Label(password_gen, text="Require digits?", font=('Arial', 14),anchor="center")
digits_label.place(x=20, y=120)
digits_checkbox = Checkbutton(password_gen, variable=digits_var, font=('Arial', 14))
digits_checkbox.place(x=200, y=120)

password_button = Button(password_gen, text="Generate Password", command=generate_password,background="grey")
password_button.place(x=200, y=160)

password_gen.mainloop()
