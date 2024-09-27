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
# Open Screen
from tkinter import *                           # Importing all the functions, classes, and constants from the tkinter library for GUI
from tkinter.ttk import Progressbar, Style      # Imports Progressbar widget from the ttk module in tkinter (Create progress bars 'loading bars')
import sys                                      # Provides access to system-specific parameters and functions
import os                                       # Allows Interaction with the oparting system such as file handling.
import time                                     # Provides time-related functions (for sleeping, delays)

root = Tk()                                     # Creates the main window for the application known as the 'root'. This is where all the buttons and labesl will be placed

# Creating image 
image = PhotoImage(file='images/open_screen.png') # You need to add your file based on where it is located in your own system

# Size of the window (image)
height = 600
width = 800

# Calculating the position of the window on the screen, to center it horizontally and vertically
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)

# Get dimensions of the screen to position the window in the center of the screen
# Dividing these dimensions by 2 and substracting half the width and height of the window
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Removing the window frame and title bar from the root window.
# To appear the window as a floating window without any borders or decorations.
root.overrideredirect(1)

# Using '-topmost' Tkinter attribute to control the stackign order of windows.
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')

# Background image
bg_label = Label(root, image=image)
bg_label.image = image # Store a reference to the image to preven it from being garabge-collected
bg_label.place(x=0, y=0)

#welcome_label = Label(text='Welcome to Inventory Vision Pro', bg='black', font=("arial", 15, "bold"), fg='white')
#welcome_label.place(x=100, y=20)

created_by_label = Label(text='Created by Group 1', bg='black', font=("arial", 20, "bold"), fg='white')
created_by_label.place(x=250, y=100)

# Progress label
progress_label = Label(root, text="Please Wait...", font=('arial', 20, 'bold'), fg='white', bg='black')
progress_label.place(x=270, y=510)

# Define a custom style for the progress bar
style = Style()
style.theme_use('alt') # 'clam', 'alt', 'default', or 'classic' (options)
style.configure("custom.Horizontal.TProgressbar",
                troughcolor='#2e2e2e',  # Background (trough) color of progress bar
                background='#f4f4f4',   # Foreground (progress fill) color
                thickness=20)           # Thickness of the progress bar

# Apply the cusotm style to the progress bar
progress = Progressbar(root, style="custom.Horizontal.TProgressbar", orient=HORIZONTAL, length=650, mode="determinate")
progress.place(x=80, y=555)

# Exit Button
exit_btn = Button(
    text='x',                                   # The text displayed on the button
    bg='red',                                   # Background color of the button
    command=lambda: exit_window(),              # Command to execute when the button is clicked
    bd=0,                                       # Border width of the button
    font=("arial", 16, "bold"),                 # Font type and size for the button text
    activebackground='#fd6a36',                 # Backgroudn color when the button is clicked
    fg='white'                                  # Foreground (text) color of the button
)
exit_btn.place(x=769, y=0)                      # Postition of the button

# Function to handel window exit
def exit_window():
    sys.exit(root.destroy())                    # Close the application and exit the program
    
# Function to launch the main application
def top():
    root.withdraw()                             # Hide the current window
    os.system("python InventoryManagement.py") # Launch the Inventory Vision app # You need to add your file based on where it is located in your own system
    root.destroy()                              # Destroy the current window

# Initialize a global variable for progress tracking
i = 0

# Function to simluate the loading process
def loadsystem():
    global i                                        # Use the globar variable 'i'
    if i <= 100:                                    # Continue until 'i' reached 100
        if i == 90:                                 # If 'i' is 90, introduce a delat to simluate loading
            time.sleep(2)
        txt = 'Please Wait...  ' + (str(i)+'%')     # Update the label text with current progress
        progress_label.config(text=txt)             # Update the progress label
        progress_label.after(10, loadsystem)        # Schedule the next update after 10 milliseconds
        progress['value'] = i                       # Update the progress bar value
        i += 1                                      # Increment the progress counter
    else:
        top()                                       # Call the function to launch the main application

# Start the laoding process
loadsystem()

# Start the Tkinter even loop
root.mainloop()

