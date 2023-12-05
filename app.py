from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas setup w/ logo image
canvas = Canvas(width=200, height=200)
logo_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_photo)
canvas.pack()



window.mainloop()