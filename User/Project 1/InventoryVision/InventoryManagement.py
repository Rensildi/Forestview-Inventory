'''
Detroit-Michigan, September 21st, 2024 - Saturday 05:24 PM
@authors: Group 1 :
Rensildi Kalanxhi, 
Jawad Rashid, 
Abdulla Maruf, 
Ejmen Gerguri, 
Sajidul Haque,
Tucker McGuire
'''

import tkinter as tk
from tkinter import messagebox, Label  # Import necessary components from tkinter
from tkinter.ttk import LabelFrame, Button, Entry, Frame, Scrollbar, Style  # Import themed widgets
from ttkthemes import themed_tk  # Import the themed Tkinter module
from PIL import Image, ImageTk  # Import PIL for image handling

# Function to populate the Listbox with initial items
def populate_list():
    product_list_listbox.delete(0, tk.END)  # Clear the Listbox
    items = [
        "1 | Category | Brand | Product A | 10 | $100 | $120",
        "2 | Category | Brand | Product B | 15 | $80 | $100"
    ]
    for item in items:
        product_list_listbox.insert(tk.END, item)  # Add each item to the Listbox

# Function to select an item from the Listbox and populate the input fields
def select_item(event):
    try:
        clear_input()  # Clear input fields before populating new data
        selected_item = product_list_listbox.get(product_list_listbox.curselection()[0])
        selected_item = selected_item.split(" | ")  # Split the string into components
        # Insert selected item details into respective input fields
        product_id_entry.insert(0, selected_item[0])
        product_category_entry.insert(0, selected_item[1])
        product_brand_entry.insert(0, selected_item[2])
        product_name_entry.insert(0, selected_item[3])
        product_stock_entry.insert(0, selected_item[4])
        cost_price_entry.insert(0, selected_item[5])
        selling_price_entry.insert(0, selected_item[6])
    except IndexError:
        pass  # Handle case where no item is selected

# Function to clear all input fields
def clear_input():
    product_id_entry.delete(0, tk.END)
    product_category_entry.delete(0, tk.END)
    product_brand_entry.delete(0, tk.END)
    product_name_entry.delete(0, tk.END)
    product_stock_entry.delete(0, tk.END)
    cost_price_entry.delete(0, tk.END)
    selling_price_entry.delete(0, tk.END)

# Function to add a new item to the Listbox
def add_item():
    product_id = product_id_entry.get()
    product_category = product_category_entry.get()
    product_brand = product_brand_entry.get()
    product_name = product_name_entry.get()
    product_stock = product_stock_entry.get()
    cost_price = cost_price_entry.get()
    selling_price = selling_price_entry.get()
    
    # Create a formatted string for the Listbox
    new_item = f"{product_id} | {product_category} | {product_brand} | {product_name} | {product_stock} | {cost_price} | {selling_price} "
    
    # Add the new item to the Listbox
    product_list_listbox.insert(tk.END, new_item)
    statusbar_label.config(text="Status: Item added successfully", background="#28a745")  # Update status message
    
    # Clear the input fields after adding the item
    clear_input()

# Function to update the selected item in the Listbox
def update_item():
    try:
        selected_index = product_list_listbox.curselection()[0]  # Get the index of the selected item
        # Retrieve updated values from input fields
        product_id = product_id_entry.get()
        product_category = product_category_entry.get()
        product_brand = product_brand_entry.get()
        product_name = product_name_entry.get()
        product_stock = product_stock_entry.get()
        cost_price = cost_price_entry.get()
        selling_price = selling_price_entry.get()
        
        # Create a formatted string for the updated Listbox item
        updated_item = f"{product_id} | {product_category} | {product_brand} | {product_name} | {product_stock} | {cost_price} | {selling_price} "
        
        # Update the item in the Listbox
        product_list_listbox.delete(selected_index)  # Remove the old item
        product_list_listbox.insert(selected_index, updated_item)  # Insert the updated item
        statusbar_label.config(text="Status: Item updated successfully", background="#28a745")  # Update status message
        
        # Clear the input fields after updating the item
        clear_input()
    except IndexError:
        statusbar_label.config(text="Status: No item selected to update")  # Handle no selection

# Function to remove the selected item from the Listbox
def remove_item():
    try:
        selected_index = product_list_listbox.curselection()[0]  # Get the index of the selected item
        product_list_listbox.delete(selected_index)  # Remove the item from the Listbox
        statusbar_label.config(text="Status: Item removed successfully", background="#28a745")  # Update status message
    except IndexError:
        statusbar_label.config(text="Status: No item selected to remove")  # Handle no selection

# Function to toggle between dark and light theme
def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        root.set_theme("equilux")  # Dark theme
        statusbar_label.config(fg="#B22222")  # Set status label color for dark mode
    else:
        root.set_theme("breeze")  # Light theme
        statusbar_label.config(fg="#B22222")  # Same color for normal mode
    is_dark_mode = not is_dark_mode  # Toggle the mode

# Function to create and configure the main application window
def create_window():
    global product_list_listbox, product_id_entry, product_category_entry, product_brand_entry, product_name_entry
    global product_stock_entry, cost_price_entry, selling_price_entry, statusbar_label, is_dark_mode, root

    is_dark_mode = False  # Start in normal mode

    root = themed_tk.ThemedTk()  # Create themed Tkinter window
    root.set_theme("breeze")  # Set default normal theme
    root.title("Inventory Vision Pro Management System")  # Set window title
    width = 1080
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)  # Center the window on the screen
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')  # Set window size and position
    root.columnconfigure(0, weight=1)

    # Load and set application icon
    im = Image.open("images//icon.png") # You need to add your file based on where it is located in your own system
    icon = ImageTk.PhotoImage(im)
    root.wm_iconphoto(True, icon)

    # Configure styles for buttons
    style = Style()
    style.configure('TButton', font=('Arial', 12), padding=10)
    style.map('TButton', background=[('active', '#2980b9')])

    # Create a LabelFrame for input fields
    entry_frame = LabelFrame(root, text="Enter Product Details")

    # Create and place input fields with corresponding labels
    product_id_var = tk.StringVar()
    product_id_label = Label(entry_frame, text="Product ID: ")
    product_id_label.grid(row=0, column=0, sticky="w", padx=10)
    product_id_entry = Entry(entry_frame, textvariable=product_id_var)
    product_id_entry.grid(row=0, column=1)

    product_category_var = tk.StringVar()
    product_category_label = Label(entry_frame, text="Product Category: ")
    product_category_label.grid(row=1, column=0, sticky="w", padx=10)
    product_category_entry = Entry(entry_frame, textvariable=product_category_var)
    product_category_entry.grid(row=1, column=1)

    product_brand_var = tk.StringVar()
    product_brand_label = Label(entry_frame, text="Product Brand: ")
    product_brand_label.grid(row=0, column=2, sticky="w", padx=10)
    product_brand_entry = Entry(entry_frame, textvariable=product_brand_var)
    product_brand_entry.grid(row=0, column=3)

    product_name_var = tk.StringVar()
    product_name_label = Label(entry_frame, text="Product Name: ")
    product_name_label.grid(row=1, column=2, sticky="w", padx=10)
    product_name_entry = Entry(entry_frame, textvariable=product_name_var)
    product_name_entry.grid(row=1, column=3)

    product_stock_var = tk.StringVar()
    product_stock_label = Label(entry_frame, text="Product Stock: ")
    product_stock_label.grid(row=0, column=4, sticky="w", padx=10)
    product_stock_entry = Entry(entry_frame, textvariable=product_stock_var)
    product_stock_entry.grid(row=0, column=5)

    cost_price_var = tk.StringVar()
    cost_price_label = Label(entry_frame, text="Cost Price: ")
    cost_price_label.grid(row=1, column=4, sticky="w", padx=10)
    cost_price_entry = Entry(entry_frame, textvariable=cost_price_var)
    cost_price_entry.grid(row=1, column=5)

    selling_price_var = tk.StringVar()
    selling_price_label = Label(entry_frame, text="Selling Price: ")
    selling_price_label.grid(row=2, column=0, sticky="w", padx=10)
    selling_price_entry = Entry(entry_frame, textvariable=selling_price_var)
    selling_price_entry.grid(row=2, column=1)

    # Create a frame for the Listbox and its scrollbar
    listing_frame = Frame(root, borderwidth=1, relief="raised")
    product_list_listbox = tk.Listbox(listing_frame, width=146)  # Create the Listbox
    product_list_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")
    product_list_listbox.bind("<<ListboxSelect>>", select_item)  # Bind selection event

    scroll_bar = Scrollbar(listing_frame)  # Create scrollbar
    scroll_bar.config(command=product_list_listbox.yview)  # Link scrollbar to Listbox
    scroll_bar.grid(row=0, column=1, sticky="ns")  # Place scrollbar
    product_list_listbox.config(yscrollcommand=scroll_bar.set)  # Configure Listbox to use scrollbar

    # Create status bar for feedback messages
    statusbar_label = tk.Label(root, text="Status: ", anchor="w", font=("arial", 10), fg="black", background="#B22222")  # Red color
    statusbar_label.grid(row=3, column=0, sticky="we", padx=10)

    # Create a frame for buttons
    button_frame = Frame(root, borderwidth=2, relief="groove")

    # Create buttons and link them to their respective functions
    add_item_btn = Button(button_frame, text="Add item", command=add_item)
    add_item_btn.grid(row=0, column=0, sticky="we", padx=10, pady=5)

    remove_item_btn = Button(button_frame, text="Remove item", command=remove_item)
    remove_item_btn.grid(row=0, column=1, sticky="we", padx=10, pady=5)

    update_item_btn = Button(button_frame, text="Update item", command=update_item)
    update_item_btn.grid(row=0, column=2, sticky="we", padx=10, pady=5)

    clear_item_btn = Button(button_frame, text="Clear Input", command=clear_input)
    clear_item_btn.grid(row=0, column=3, sticky="we", padx=10, pady=5)

    toggle_theme_btn = Button(button_frame, text="Toggle Dark/Normal Mode", command=toggle_theme)
    toggle_theme_btn.grid(row=0, column=4, sticky="we", padx=10, pady=5)

    # Arrange the frames in the main window
    entry_frame.grid(row=0, column=0, sticky="we", padx=10, pady=5)
    button_frame.grid(row=1, column=0, sticky="we", padx=10, pady=5)
    listing_frame.grid(row=2, column=0, sticky="we", padx=10)

    populate_list()  # Populate the Listbox with initial items

    root.mainloop()  # Start the Tkinter event loop

# Main function to run the application
def main():
    create_window()  # Create and display the window

if __name__ == "__main__":
    main()  # Call the main function to start the program




'''
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import LabelFrame, Label, Button, Entry, Frame, Scrollbar
from ttkthemes import themed_tk
from PIL import Image, ImageTk

# Dummy function to replace database calls
def populate_list():
    product_list_listbox.delete(0, tk.END)
    # You can manually add items here if you want to see something in the listbox
    items = [
        "1 | Category | Brand | Product A | 10 | $100 | $120",
        "2 | Category | Brand | Product B | 15 | $80 | $100"
    ]
    for item in items:
        product_list_listbox.insert(tk.END, item)

# Function to handle item selection (without database functionality)
def select_item(event):
    try:
        clear_input()
        selected_item = product_list_listbox.get(product_list_listbox.curselection()[0])
        selected_item = selected_item.split("  |  ")
        # Insert dummy data into entry fields
        product_id_entry.insert(0, selected_item[1])
        product_category_entry.insert(0, selected_item[2])
        product_brand_entry.insert(0, selected_item[3])
        product_name_entry.insert(0, selected_item[4])
        product_stock_entry.insert(0, selected_item[5])
        cost_price_entry.insert(0, selected_item[6])
        selling_price_entry.insert(0, selected_item[7])
    except IndexError:
        pass

# Function to clear the input fields
def clear_input():
    product_id_entry.delete(0, tk.END)
    product_category_entry.delete(0, tk.END)
    product_brand_entry.delete(0, tk.END)
    product_name_entry.delete(0, tk.END)
    product_stock_entry.delete(0, tk.END)
    cost_price_entry.delete(0, tk.END)
    selling_price_entry.delete(0, tk.END)

# Button frame and functions
def add_item():
    statusbar_label.config(text="Status: Add item clicked", bg='green', fg='white')

def update_item():
    statusbar_label.config(text="Status: Update item clicked", bg='green', fg='white')

def remove_item():
    statusbar_label.config(text="Status: Remove item clicked", bg='green', fg='white')

# Function to create the main GUI window
def create_window():
    global product_list_listbox, product_id_entry, product_category_entry, product_brand_entry, product_name_entry
    global product_stock_entry, cost_price_entry, selling_price_entry, statusbar_label

    # Create main window using themed_tk
    root = themed_tk.ThemedTk()
    root.set_theme("scidpurple")
    root.title("Inventory Vision Pro Management System")
    width = 1080
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.columnconfigure(0, weight=1)

    # Set window icon (optional)
    im = Image.open("C://Users//rkala//OneDrive//Desktop//User//InventoryVision//images//icon.png")
    icon = ImageTk.PhotoImage(im)
    root.wm_iconphoto(True, icon)

    # Entry frame for product details
    entry_frame = LabelFrame(root, text="Enter Product Details")

    # Product ID
    product_id_var = tk.StringVar()
    product_id_label = Label(entry_frame, text="Product ID: ")
    product_id_label.grid(row=0, column=0, sticky="w", padx=10)
    product_id_entry = Entry(entry_frame, textvariable=product_id_var)
    product_id_entry.grid(row=0, column=1)

    # Product Category
    product_category_var = tk.StringVar()
    product_category_label = Label(entry_frame, text="Product Category: ")
    product_category_label.grid(row=1, column=0, sticky="w", padx=10)
    product_category_entry = Entry(entry_frame, textvariable=product_category_var)
    product_category_entry.grid(row=1, column=1)

    # Product Brand
    product_brand_var = tk.StringVar()
    product_brand_label = Label(entry_frame, text="Product Brand: ")
    product_brand_label.grid(row=0, column=2, sticky="w", padx=10)
    product_brand_entry = Entry(entry_frame, textvariable=product_brand_var)
    product_brand_entry.grid(row=0, column=3)

    # Product Name
    product_name_var = tk.StringVar()
    product_name_label = Label(entry_frame, text="Product Name: ")
    product_name_label.grid(row=1, column=2, sticky="w", padx=10)
    product_name_entry = Entry(entry_frame, textvariable=product_name_var)
    product_name_entry.grid(row=1, column=3)

    # Product Stock
    product_stock_var = tk.StringVar()
    product_stock_label = Label(entry_frame, text="Product Stock: ")
    product_stock_label.grid(row=0, column=4, sticky="w", padx=10)
    product_stock_entry = Entry(entry_frame, textvariable=product_stock_var)
    product_stock_entry.grid(row=0, column=5)

    # Cost Price
    cost_price_var = tk.StringVar()
    cost_price_label = Label(entry_frame, text="Cost Price: ")
    cost_price_label.grid(row=1, column=4, sticky="w", padx=10)
    cost_price_entry = Entry(entry_frame, textvariable=cost_price_var)
    cost_price_entry.grid(row=1, column=5)

    # Selling Price
    selling_price_var = tk.StringVar()
    selling_price_label = Label(entry_frame, text="Selling Price: ")
    selling_price_label.grid(row=2, column=0, sticky="w", padx=10)
    selling_price_entry = Entry(entry_frame, textvariable=selling_price_var)  # Define selling_price_entry
    selling_price_entry.grid(row=2, column=1)  # Now this will work


    # Product List frame
    listing_frame = Frame(root, borderwidth=1, relief="raised")
    product_list_listbox = tk.Listbox(listing_frame, width=146)
    product_list_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="we")
    product_list_listbox.bind("<<ListboxSelect>>", select_item)

    # Scrollbar
    scroll_bar = Scrollbar(listing_frame)
    scroll_bar.config(command=product_list_listbox.yview)
    scroll_bar.grid(row=0, column=1, sticky="ns")
    product_list_listbox.config(yscrollcommand=scroll_bar.set)

    # Status bar
    statusbar_label = tk.Label(root, text="Status: ", bg="#ffb5c5", anchor="w", font=("arial", 10))
    statusbar_label.grid(row=3, column=0, sticky="we", padx=10)

    # Button frame and buttons
    button_frame = Frame(root, borderwidth=2, relief="groove")

    add_item_btn = Button(button_frame, text="Add item", command=add_item)
    add_item_btn.grid(row=0, column=0, sticky="we", padx=10, pady=5)

    remove_item_btn = Button(button_frame, text="Remove item", command=remove_item)
    remove_item_btn.grid(row=0, column=1, sticky="we", padx=10, pady=5)

    update_item_btn = Button(button_frame, text="Update item", command=update_item)
    update_item_btn.grid(row=0, column=2, sticky="we", padx=10, pady=5)

    clear_item_btn = Button(button_frame, text="Clear Input", command=clear_input)
    clear_item_btn.grid(row=0, column=3, sticky="we", padx=10, pady=5)

    # Place frames and buttons
    entry_frame.grid(row=0, column=0, sticky="we", padx=10, pady=5)
    button_frame.grid(row=1, column=0, sticky="we", padx=10, pady=5)
    listing_frame.grid(row=2, column=0, sticky="we", padx=10)

    populate_list()

    root.mainloop()

# Main function to run the application
def main():
    create_window()

if __name__ == "__main__":
    main()
'''
