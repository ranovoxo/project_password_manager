from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas setup w/ logo image
canvas = Canvas(width=200, height=200)
logo_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(row=1, column=1)

# website field setup
website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
website_input = Entry(width=35)
website_input.grid(row=2, column=1, columnspan=2)

# email field setup
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)

# password field setup
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
password_input = Entry(width=18)
password_input.grid(column=1, row=4)
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=4)
password_button.config(command=generate_password)

# submit button field
submit_info_button = Button(text="Add", width=36)
submit_info_button.grid(column=1, row=5, columnspan=2)




window.mainloop()