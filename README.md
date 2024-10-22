
# AUTOCLICKER
Autoclicker is a simple and customizable auto-clicker tool built using Python and customtkinter. It allows the user to automate mouse clicks or key presses for a selected key. The tool provides a user-friendly interface to configure settings like button choice, mouse click enabling, and switching between light and dark modes.
##

## Features

- **Key Automation**: Allows automating key presses for various keys like alphabets, function keys, and special keys.
- **Mouse Click Automation**: Option to automate mouse clicks.
- **Customizable Timer**: Displays a countdown timer before activation.
- **Light/Dark Mode**: Toggle between light and dark themes for the UI.
- **Tooltips**: Hover over the icon to see a tooltip for additional safety instructions.
- **Fail-Safe**: Hovering the mouse to the top-left corner (x=0, y=0) provides an easy fail-safe.

## Screenshot

![image alt](https://github.com/bshrmonsti761/AutoClicker/blob/main/AutoClickerGUI.png?raw=true)


## Installation 
**Prerequisites** 
- Python 3.x is required.
- The following Python libraries must be installed:
  - customtkinter
  - pyautogui
  - Pillow (for image handling)
    
```bash
  pip install customtkinter pyautogui Pillow
```
**Run from Source:**
    
1. Clone the repository
```bash
git clone https://github.com/bshrmonsti761/AutoClicker
cd Autoclicker
```
2. Run the Python script:
```bash
python AutoClicker.py
```
3. Run Executable
    
    To run a standalone executable using PyInstaller,
    you can download the executable file instead    of building it yourself.
    
**Download the Executable**

1. Download the executable "AutoClicker.exe", found in the releases.

2. Once the download is complete,locate the .exe file
on your computer.

3. Run the executable by double-clicking on the file.
## Usage

- **Choose Button**: Use the dropdown menu to select which key to automate.
- **Enable Mouse Click**: Check the box if you want to automate mouse clicks instead of key presses.
- **Activate/Stop**: Press the Activate button to start the automation, and Stop to end it.
- **Appearance Mode**: Use the Appearance Mode button to switch between light and dark themes.
**Fail-Safe**

If you want to stop the auto-clicker manualhttps://github.com/bshrmonsti761/AutoClicker/blob/main/AutoClickerGUI.png?raw=truely, simply move your mouse cursor to the top-left corner (x=0, y=0) of the screen and hold it for a second or longer, which will stop the process for safety.


## Contributing

Contributions are always welcome!

If you'd like to contribute to this project, 
feel free to fork the repository and submit a pull request.



## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
