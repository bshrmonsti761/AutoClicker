import threading
import time
import sys
import os
import pyautogui as k
from customtkinter import *
from PIL import Image
import webbrowser


# Setup
app = CTk()
app.geometry("500x400")
app.title("Autoclicker")        
current_mode = "light"
on_off = "Activate"
running = False
selected_key = "a"
mouse_on = False


# Switch Light/Dark Mode
def mode():
    global current_mode
    if current_mode == "light":
        set_appearance_mode("dark")
        bMode.configure(text="Light Mode", fg_color="#FFFFFF", text_color="#000000", hover_color="#FFFFFF")
        current_mode = "dark"
    else:
        set_appearance_mode("light")
        bMode.configure(text="Dark Mode", fg_color="#000000", text_color="#FFFFFF", hover_color="#000000")
        current_mode = "light"
        

# Possible Keys
key_options = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
    "enter", "space", "tab", "backspace", "esc", "delete", "insert", 
    "shift", "ctrl", "alt", "cmd", "option", "fn", 
    "left", "right", "up", "down", 
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", 
    "home", "end", "pageup", "pagedown", "capslock", "numlock", "scrolllock", 
    "printscreen", "pause", "menu", 
    "volumemute", "volumedown", "volumeup", "playpause", "nexttrack", "prevtrack", 
    "`", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/", "grave", "tilde", 
    "num0", "num1", "num2", "num3", "num4", "num5", "num6", "num7", "num8", "num9", 
    "add", "subtract", "multiply", "divide", "decimal"
]
# Function to get the correct path, whether it's bundled or not
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):  
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def callback(url):
    url="https://github.com/bshrmonsti761/AutoClicker"
    webbrowser.open_new(url)


# Enable mouse click
def mouse_enabled():
    global mouse_on
    mouse_on = True

# Select key
def keys_list(choice):
    global selected_key
    selected_key = choice

# Autoclick function
# While Loop
def autoclick():
    global on_off
    global running
    
    if on_off == "Activate":
        # Timer Countdown
        for i in range(5, -1, -1):
            time.sleep(1)
            print(i)
            lTimer.configure(text=f"Starts in: {i}")
            app.update()
            
            if i == 0:
                lTimer.configure(text="Active")
                app.update()
        
        # Start clicking
        running = True
        button1.configure(text="Stop")
        on_off = "Stop"
        
        while running:
            if mouse_on:
                k.click()
            else:
                k.press(selected_key)
             
    else:
        button1.configure(text="Activate")
        on_off = "Activate"
        running = False
        lTimer.configure(text="Stopped")

# For Loop
e=CTkEntry(app,corner_radius=32,width=156)
def autoclickFor():
    global on_off
    global running
    
    if on_off == "Activate":
        # Timer Countdown
        for i in range(5, -1, -1):
            time.sleep(1)
            print(i)
            lTimer.configure(text=f"Starts in: {i}")
            app.update()
             
            if i == 0:
                lTimer.configure(text="Active")
                app.update()
        
        # Start clicking
        running = True
        button2.configure(text="Stop")  
        on_off = "Stop"
        for i in range(int(e.get())):
            if mouse_on:
                k.click()
            else:
                k.press(selected_key)
        print("The End")
    else:
        button2.configure(text="Activate")
        on_off = "Activate"
        running = False
        lTimer.configure(text="Stopped")
        
# Show tooltip on hover
def show_tooltip(event):
    tooltip.place(x=90, y=150, anchor="center")

def hide_tooltip(event):
    tooltip.place_forget()

# UI Components
bMode = CTkButton(app, text="Appearance Mode", command=mode, corner_radius=32, fg_color="#932108",hover_color="#87210a")
bMode.place(x=485, y=50, anchor="se")

button1 = CTkButton(app, text="Activate Infinite Loop", command=lambda:threading.Thread(target=autoclick).start(), corner_radius=32, fg_color="#932108",hover_color="#87210a")
button1.place(x=250, y=200, anchor="center")
e.place(x=250,y=280,anchor="center")
button2 = CTkButton(app, text="Activate for: ",command=lambda:threading.Thread(target=autoclickFor).start(), corner_radius=32,width=156, fg_color="#932108",hover_color="#87210a")
button2.place(x=250, y=240, anchor="center")
l = CTkButton(app, corner_radius=32, text="Choose Button:", state="readonly", fg_color="#932108",width=156).place(x=250, y=120, anchor="center")

op = CTkOptionMenu(app, corner_radius=32, state="readonly", values=key_options, command=keys_list, fg_color="#932108", button_color="#87210a",width=156)
op.place(x=250, y=160, anchor="center")

cb = CTkCheckBox(app, corner_radius=32, text="Enable Mouse Click", command=mouse_enabled,width=156)
cb.place(x=250, y=80, anchor="center")

# Tooltip and image
tooltip = CTkLabel(app, text="For a safe fail,\nhover the mouse\nto the top left corner\nand\nhold it for a second.\n(x=0, y=0)\nDO NOT ACTIVATE\nMORE THAN ONCE\nAT A TIME FOR\nCRASHING\nAVOIDANCE.",corner_radius=16, fg_color="grey")
tooltip.place_forget()
t=CTkTextbox(app)
image = CTkImage(light_image=Image.open(resource_path("HintLogo.png")), size=(50, 50))
image_label = CTkLabel(app, image=image, text="", cursor="center_ptr")
image_label.place(x=0, y=10)

image_label.bind("<Enter>", show_tooltip)
image_label.bind("<Leave>", hide_tooltip)

# Timer label
lTimer = CTkButton(app, corner_radius=32, text="Starts in: 5", state="readonly", fg_color="#932108",width=156)
lTimer.place(x=250, y=360, anchor="center")
lError=CTkLabel(app,text="Only Whole Numbers Accepted",text_color="#932108").place(x=250, y=320, anchor="center")
link1 = CTkLabel(app, text="My Github", cursor="hand2",text_color="#00a8f3")
link1.place(x=450,y=360,anchor="center")
link1.bind("<Button-1>",command=callback)

# Final app setup
app.resizable(False, True)
app.mainloop()
