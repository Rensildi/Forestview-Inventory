'''
Detroit-Michigan, September 21st, 2024 - Saturday 12:01 PM
@authors: Group 1 :
Rensildi Kalanxhi, 
Jawad Rashid, 
Abdulla Maruf, 
Ejmen Gerguri, 
Sajidul Haque,
Tucker McGuire
'''

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar, Style
import time
from database import add_product, get_all_products, update_product, delete_product, create_table

'''
This function centers a given Tkinter window on the screen
based on the window’s width and height.
'''
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width // 2) - (width // 2)
    y_coordinate = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

'''
This function refreshes the product list in the Treeview widget
by clearing the current content and re-fetching all products from the database.
'''
def refresh_product_list():
    product_list.delete(*product_list.get_children())  # Clear the Treeview
    products = get_all_products()
    for product in products:
        product_list.insert('', 'end', values=product)

'''
This function adds a new product to the database.
It fetches the user input, validates it, and then inserts
the new product into the database before refreshing the list.
'''
def add_product_to_db():
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    if name and quantity and price:
        add_product(name, int(quantity), float(price))
        refresh_product_list()
        clear_input_fields()
    else:
        messagebox.showwarning("Input Error", "All fields are required")

'''
This function updates an existing product in the database.
It gets the selected product from the Treeview, updates the database
with the new values, and refreshes the list.
'''
def update_product_in_db():
    selected_item = product_list.selection()
    if selected_item:
        product = product_list.item(selected_item)['values']
        product_id = product[0]
        name = name_entry.get()
        quantity = quantity_entry.get()
        price = price_entry.get()

        if name and quantity and price:
            update_product(product_id, name, int(quantity), float(price))
            refresh_product_list()
            clear_input_fields()
        else:
            messagebox.showwarning("Input Error", "All fields are required")
    else:
        messagebox.showwarning("Selection Error", "No product selected")

'''
This function deletes a selected product from the database.
It retrieves the selected product, removes it from the database,
and then refreshes the product list.
'''
def delete_product_from_db():
    selected_item = product_list.selection()
    if selected_item:
        product = product_list.item(selected_item)['values']
        product_id = product[0]
        delete_product(product_id)
        refresh_product_list()
        clear_input_fields()
    else:
        messagebox.showwarning("Selection Error", "No product selected")

'''
This function clears the input fields in the form
by setting the text entries for name, quantity, and price to empty.
'''
def clear_input_fields():
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

'''
This function toggles between light and dark modes for the application.
It changes the theme of the ttk widgets and adjusts the background color of the root window.
'''
def toggle_theme():
    if root.tk.call("ttk::style", "theme", "use") == "clam":  # Light mode
        root.tk.call("ttk::style", "theme", "use", "alt")  # Switch to dark
        root.configure(bg='#2e2e2e')
    else:  # Dark mode
        root.tk.call("ttk::style", "theme", "use", "clam")  # Switch to light
        root.configure(bg='#f0f0f0')

'''
This function creates a loading screen with a progress bar. 
It shows a splash screen and, after loading, it closes the splash screen and 
reveals the main window.
'''
def open_menu_screen():
    menu_root = tk.Toplevel()
    menu_root.title("Loading Screen")
    
    # Set size and center the window
    width, height = 800, 600
    center_window(menu_root, width, height)
    
    menu_root.overrideredirect(1)  # No window frame
    menu_root.wm_attributes('-topmost', True)

    image = tk.PhotoImage(file='C:/Users/rkala/Downloads/IMS_CSC 4110/IMS_CSC 4110/images/open_screen.png')  # Set your image path
    bg_label = tk.Label(menu_root, image=image)
    bg_label.image = image  # Prevent garbage collection
    bg_label.place(x=0, y=0)

    created_by_label = tk.Label(menu_root, text="Created by Group 1", bg='black', font=("arial", 20, "bold"),
                                fg='white')
    created_by_label.place(x=250, y=100)

    progress_label = tk.Label(menu_root, text="Please Wait...", font=('arial', 20, 'bold'), fg='white', bg='black')
    progress_label.place(x=270, y=510)

    style = Style()
    style.theme_use('alt')
    style.configure("custom.Horizontal.TProgressbar", troughcolor='#2e2e2e', background='#f4f4f4', thickness=20)

    progress = Progressbar(menu_root, style="custom.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=650,
                           mode="determinate")
    progress.place(x=80, y=555)

    # Function to update progress bar and close menu
    def load_app():
        for i in range(101):
            time.sleep(0.03)
            progress['value'] = i
            progress_label.config(text=f'Please Wait... {i}%')
            menu_root.update_idletasks()
        menu_root.destroy()  # Close menu screen when complete
        root.deiconify()  # Show the main window

    load_app()

# Create the database and the products table if they don't exist
create_table()

'''
The main window initialization and setup for the Inventory Management System.
The window is centered, configured for responsive layout, and set with default
themes and widgets such as input fields, buttons, and a Treeview for displaying products.
'''
root = tk.Tk()
root.title("Inventory Management System")

# Center the main window before withdrawing
center_window(root, 800, 600)

root.withdraw()  # Hide the main window until the menu screen is done

# Set up ttk themes
style = ttk.Style(root)
root.tk.call("ttk::style", "theme", "use", "clam")  # Set default to light

# Make the window responsive
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Product Input Frame
input_frame = ttk.Frame(root, padding="10 10 10 10")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

input_frame.grid_columnconfigure(1, weight=1)  # Make the input fields expand

name_label = ttk.Label(input_frame, text="Product Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

quantity_label = ttk.Label(input_frame, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
quantity_entry = ttk.Entry(input_frame)
quantity_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

price_label = ttk.Label(input_frame, text="Price:")
price_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
price_entry = ttk.Entry(input_frame)
price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Buttons Frame
buttons_frame = ttk.Frame(root, padding="10 10 10 10")
buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

buttons_frame.grid_columnconfigure(3, weight=1)  # Ensure buttons expand

add_button = ttk.Button(buttons_frame, text="Add Product", command=add_product_to_db)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = ttk.Button(buttons_frame, text="Update Product", command=update_product_in_db)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = ttk.Button(buttons_frame, text="Delete Product", command=delete_product_from_db)
delete_button.grid(row=0, column=2, padx=5, pady=5)

toggle_button = ttk.Button(buttons_frame, text="Toggle Light/Dark Mode", command=toggle_theme)
toggle_button.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

# Product List (Treeview)
columns = ('id', 'name', 'quantity', 'price')
product_list = ttk.Treeview(root, columns=columns, show='headings')
product_list.heading('id', text='ID')
product_list.heading('name', text='Product Name')
product_list.heading('quantity', text='Quantity')
product_list.heading('price', text='Price')

product_list.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Make product list expand to fit available space
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Initial load of products into the Treeview
refresh_product_list()

# Open the menu screen
open_menu_screen()

# Start the Tkinter event loop
root.mainloop()
