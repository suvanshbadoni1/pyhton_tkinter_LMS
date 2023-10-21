import tkinter as tk
from tkinter import messagebox

# Define common font and color settings
font = ("Arial", 16)
bg_color = "lightblue"
button_bg_color = "lightgray"
button_fg_color = "black"

# Function to simulate a login (placeholder functionality)
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace with your actual authentication logic here
    if username == "admin" and password == "password":
        # Successful login, open the main menu
        open_main_menu()
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Function to open a section (placeholder functionality)
def open_section(section_title):
    section_window = tk.Tk()
    section_window.title(section_title)

    # Create the section GUI
    section_label = tk.Label(section_window, text=section_title, font=("Arial", 24))
    section_label.pack()

    # Placeholder: Add buttons, labels, and input fields for the section
    add_button = tk.Button(section_window, text="Add", font=font, bg=button_bg_color, fg=button_fg_color)
    add_button.pack()
    delete_button = tk.Button(section_window, text="Delete", font=font, bg=button_bg_color, fg=button_fg_color)
    delete_button.pack()
    # Add more buttons and widgets as needed

    section_window.mainloop()

# Function to open the main menu
def open_main_menu():
    login_window.destroy()

    main_menu = tk.Tk()
    main_menu.title("Library Management System - Main Menu")
    main_menu.geometry("800x600")  # Set window size
    main_menu.configure(bg=bg_color)  # Set background color

    sections = ["Book Management", "Member Management", "Librarian Management", "Category Management"]

    # Buttons to open different sections of the application
    for section_title in sections:
        section_button = tk.Button(main_menu, text=section_title, command=lambda title=section_title: open_section(title), font=font, bg=button_bg_color, fg=button_fg_color)
        section_button.pack()

    main_menu.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Library Management System - Login")
login_window.geometry("800x600")  # Set window size
login_window.configure(bg=bg_color)  # Set background color

# Labels
username_label = tk.Label(login_window, text="Username:", font=font, bg=bg_color)
username_label.pack()
password_label = tk.Label(login_window, text="Password:", font=font, bg=bg_color)
password_label.pack()

# Entry fields
username_entry = tk.Entry(login_window, font=font)
username_entry.pack()
password_entry = tk.Entry(login_window, show="*", font=font)  # Show asterisks for password input
password_entry.pack()

# Login button
login_button = tk.Button(login_window, text="Login", command=login, font=font, bg=button_bg_color, fg=button_fg_color)
login_button.pack()

login_window.mainloop()
