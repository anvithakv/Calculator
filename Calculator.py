from tkinter import *

# ---------------- WINDOW ---------------- #
root = Tk()
root.title("Real Calculator")
root.geometry("360x540")
root.configure(bg="#202124")
root.resizable(False, False)

# ---------------- DISPLAY ---------------- #
expression = ""

entry = Entry(
    root,
    font=("Arial", 28),
    bg="#202124",
    fg="white",
    bd=0,
    justify=RIGHT
)

entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=25, sticky="nsew")

# ---------------- FUNCTIONS ---------------- #

def press(num):
    global expression
    expression += str(num)
    entry.delete(0, END)
    entry.insert(END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, END)
    entry.insert(END, expression)

# ---------------- BUTTON STYLE ---------------- #

btn_font = ("Arial", 18, "bold")

# ---------------- BUTTONS ---------------- #

buttons = [
    ('C', 1, 0, "#5f6368"),
    ('⌫', 1, 1, "#5f6368"),
    ('%', 1, 2, "#5f6368"),
    ('/', 1, 3, "#ff9500"),

    ('7', 2, 0, "#3c4043"),
    ('8', 2, 1, "#3c4043"),
    ('9', 2, 2, "#3c4043"),
    ('×', 2, 3, "#ff9500"),

    ('4', 3, 0, "#3c4043"),
    ('5', 3, 1, "#3c4043"),
    ('6', 3, 2, "#3c4043"),
    ('-', 3, 3, "#ff9500"),

    ('1', 4, 0, "#3c4043"),
    ('2', 4, 1, "#3c4043"),
    ('3', 4, 2, "#3c4043"),
    ('+', 4, 3, "#ff9500"),

    ('0', 5, 0, "#3c4043"),
    ('.', 5, 1, "#3c4043"),
    ('=', 5, 2, "#34a853"),
]

# ---------------- CREATE BUTTONS ---------------- #

for (text, row, col, color) in buttons:

    if text == "=":
        cmd = equal

    elif text == "C":
        cmd = clear

    elif text == "⌫":
        cmd = backspace

    elif text == "×":
        cmd = lambda x="*": press(x)

    else:
        cmd = lambda x=text: press(x)

    Button(
        root,
        text=text,
        command=cmd,
        font=btn_font,
        bg=color,
        fg="white",
        activebackground=color,
        activeforeground="white",
        bd=0,
        width=5,
        height=2
    ).grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

# Make buttons expand evenly
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# ---------------- RUN ---------------- #
root.mainloop()