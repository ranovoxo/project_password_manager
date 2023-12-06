from tkinter import *
from tkinter import messagebox as mb
from random import choice, randint, shuffle
import pyperclip3

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Remove passwords already in input field
    password_input.delete(0,END) 
    pwd_list = []

    pwd_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    pwd_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    pwd_list = pwd_letters + pwd_list + pwd_numbers

    shuffle(pwd_list)
    password = "".join(pwd_list)
    password_input.insert(0, password)
    pyperclip3.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    f = open("data.txt", "a")
    website = website_input.get()
    email = email_input.get()
    pwd = password_input.get()
    
    data = website + " | " + email + " | " + pwd + "\n"

    result = mb.askyesno(title=website, 
                      message=f"""Here are the details you entered: 
                      Email: {email}
                      Password: {pwd}
                      Is it ok to save?""")
    if result == True:
        website_input.delete(0, END) 
        password_input.delete(0,END)
        f.write(data)
        f.close()
    elif result == False:
        pass

def check_fields():
    if len(website_input.get()) == 0:
        mb.showwarning(title="Empty Field", message="Please dont leave Website field empty")
    elif len(email_input.get()) == 0:
         mb.showwarning(title="Empty Field", message="Please dont leave Email field empty")
    elif(len(password_input.get()) == 0):
         mb.showwarning(title="Empty Field", message="Please dont leave Password field empty")
    else:
        save_to_file()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

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
website_input.focus()

# email field setup
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
email_input = Entry(width=35)
email_input.grid(column=1, row=3, columnspan=2)
email_input.insert(0, "testertest@gmail.com")

# password field setup
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
password_input = Entry(width=18)
password_input.grid(column=1, row=4)
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=4)
password_button.config(command=generate_password)

# submit button field
submit_info_button = Button(text="Add", width=34)
submit_info_button.grid(column=1, row=5, columnspan=2)
submit_info_button.config(command=check_fields)




window.mainloop()