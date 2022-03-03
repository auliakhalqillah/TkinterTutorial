# Import library
import tkinter as tk
from tkinter import messagebox

# Function
def localdb():
    db = {
        'username':['admin'],
        'password':['admin']
        }
    return db

def login():
    username = entryUsername.get()
    password = entryPassword.get()

    # account verification
    db = localdb()
    if( username in db['username']) and (password in db['password']):
        messagebox.showinfo('Info', 'Log in success')
    else:
        messagebox.showwarning('Info', 'Log in failed. Please type Username and Password correctly')
    

# Initial command to call tkinter
window = tk.Tk()
# Create a title for main GUI
window.title('Log In')
# Create a geometry for main GUI
window.geometry('250x120')

# Creating frames.
# Frame 1 for entries
frameEntry = tk.Frame(window, width=240, background='cyan', height=100, highlightbackground='grey', highlightthickness=2)
frameEntry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)
# Frame 2
frameButton = tk.Frame(window, width=240, background='yellow', height=50, highlightbackground='grey', highlightthickness=2) 
frameButton.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)

# Creating Labels
# Username label that parent into frameEntry
labelUsername = tk.Label(frameEntry,text='Username')
labelUsername.grid(row=0,column=0, padx=2, pady=2, sticky=tk.NSEW)

# Password label that parent into frameEntry
labelPassword = tk.Label(frameEntry, text='Password')
labelPassword.grid(row=1,column=0, padx=2, pady=2, sticky=tk.NSEW)

# Creating Entries
entryUsername = tk.Entry(frameEntry, width=27)
entryUsername.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NSEW)

entryPassword = tk.Entry(frameEntry, width=27, show='*')
entryPassword.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NSEW)

# Creating Buttons
# Log in button
buttonLogin = tk.Button(frameButton,text='Log In', width=14, command=login)
buttonLogin.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)

buttonSignup = tk.Button(frameButton,text='Sign Up', width=14)
buttonSignup.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

# To show GUI
window.mainloop()