import tkinter as tk
from tkinter import PhotoImage
from pynput import keyboard, mouse
import threading
from PIL import Image, ImageTk


# ------------------------------------------------------------------------------------------------------

# Create the root window and set its size
root = tk.Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position of the window
width = -849  # x-coordinate (left side of the screen)
height = screen_height - 425  # y-coordinate (bottom of the screen)

# Set the size and position of the window
root.geometry(f"857x364+{width}+{height}")

root.overrideredirect(True)  # Remove the window border
root.attributes('-topmost', True)  # Always on top

# ------------------------------------------------------------------------------------------------------

# Moves the window to where clicked
click_x = 0
click_y = 0

def on_click(x, y, button, pressed):
    global click_x, click_y
    if pressed and x < 8:
        click_x = x
        click_y = y
        root.geometry(f"857x364+{11}+{y-182}")

# ------------------------------------------------------------------------------------------------------

# Mouse listener
def on_move(x, y):
    global width, click_x, click_y

    if click_x is None or click_y is None:
        return

    while  x < 8 and width < 8 and click_y-182< y < click_y+182:
        width += 7
        root.geometry(f"857x364+{width}+{click_y-182}")

    if  x < 8 and width > 10 and click_y-182< y < click_y+182:
        return

    while width > -849:
        width -= 7
        root.geometry(f"857x364+{width}+{click_y-182}")

# ------------------------------------------------------------------------------------------------------

# Load the image with PIL
background_image_pil = Image.open("images/857x364_keyboard.png")

# Convert the PIL image to a Tkinter-compatible photo image
background_image = ImageTk.PhotoImage(background_image_pil)

# Set the image in the root window
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the pressed key image and add it to the window
pressed_image_label = tk.Label(root)

# ------------------------------------------------------------------------------------------------------

# Dictionary mapping keys to coordinates
key_coordinates = {
    keyboard.Key.esc : (7, 9),
    keyboard.Key.f1 : (119, 9),
    keyboard.Key.f2 : (176, 9),
    keyboard.Key.f3 : (232, 9),
    keyboard.Key.f4 : (288, 9),
    keyboard.Key.f5 : (373, 9),
    keyboard.Key.f6 : (429, 9),
    keyboard.Key.f7 : (486, 9),
    keyboard.Key.f8 : (542, 9),
    keyboard.Key.f9 : (627, 9),
    keyboard.Key.f10 : (683, 9),
    keyboard.Key.f11 : (739, 9),
    keyboard.Key.f12 : (796, 9),
    '`' : (6, 79), '~' : (6, 79),
    '1' : (63, 79), '!' : (63, 79),
    '2' : (119, 79), '@' : (119, 79),
    '3' : (176, 79), '#' : (176, 79),
    '4' : (232, 79), '$' : (232, 79),
    '5' : (288, 79), '%' : (288, 79),
    '6' : (345, 79), '^' : (345, 79),
    '7' : (401, 79), '&' : (401, 79),
    '8' : (457, 79), '*' : (457, 79),
    '9' : (514, 79), '(' : (514, 79),
    '0' : (570, 79), ')' : (570, 79),
    '-' : (627, 79), '_' : (627, 79),
    '=' : (683, 79), '+' : (683, 79),
    keyboard.Key.backspace : (739, 79),
    keyboard.Key.tab : (6, 135),
    'q' : (91, 135), 'Q' : (91, 135),
    'w' : (147, 135), 'W' : (147, 135),
    'e' : (204, 135), 'E' : (204, 135),
    'r' : (260, 135), 'R' : (260, 135),
    't' : (316, 135), 'T' : (316, 135),
    'y' : (373, 135), 'Y' : (373, 135),
    'u' : (429, 135), 'U' : (429, 135),
    'i' : (486, 135), 'I' : (486, 135),
    'o' : (542, 135), 'O' : (542, 135),
    'p' : (598, 135), 'P' : (598, 135),
    '[' : (655, 135), '{' : (655, 135),
    ']' : (711, 135), '}' : (711, 135),
    '\\' : (768, 135), '|' : (768, 135),
    keyboard.Key.caps_lock : (6, 191),
    'a' : (105, 191), 'A' : (105, 191),
    's' : (161, 191), 'S' : (161, 191),
    'd' : (218, 191), 'D' : (218, 191),
    'f' : (274, 191), 'F' : (274, 191),
    'g' : (330, 191), 'G' : (330, 191),
    'h' : (387, 191), 'H' : (387, 191),
    'j' : (443, 191), 'J' : (443, 191),
    'k' : (500, 191), 'K' : (500, 191),
    'l' : (556, 191), 'L' : (556, 191),
    ';' : (612, 191), ':' : (612, 191),
    "'" : (669, 191), '"' : (669, 191),
    keyboard.Key.enter : (725, 191),
    keyboard.Key.shift : (6, 247),
    'z' : (133, 247), 'Z' : (133, 247),
    'x' : (190, 247), 'X' : (190, 247),
    'c' : (246, 247), 'C' : (246, 247),
    'v' : (302, 247), 'V' : (302, 247),
    'b' : (359, 247), 'B' : (359, 247),
    'n' : (415, 247), 'N' : (415, 247),
    'm' : (472, 247), 'M' : (472, 247),
    ',' : (528, 247), '<' : (528, 247),
    '.' : (584, 247), '>' : (584, 247),
    '/' : (641, 247), '?' : (641, 247),
    keyboard.Key.shift_r : (697, 247),
    keyboard.Key.ctrl_l : (6, 303),
    keyboard.Key.cmd : (77, 303),
    keyboard.Key.alt_l : (147, 303),
    keyboard.Key.space : (218, 303),
    keyboard.Key.alt_gr : (570, 303),
    keyboard.Key.ctrl_r : (782, 303)
}

# In windows file names cannot contain the following characters
def sanitize_key_id(key_id):
    # Mapping of special keys to strings that are allowed in file names
    special_key_mapping = {
        '\\': 'backslash',
        '|': 'pipe',
        '<': 'less_than',
        '>': 'greater_than',
        ':': 'colon',
        '"': 'double_quote',
        '/': 'forward_slash',
        '?': 'question_mark',
        '*': 'asterisk',
    }

    # Replace each special key with its corresponding string
    for key, replacement in special_key_mapping.items():
        key_id = key_id.replace(key, replacement)


    return key_id

# Dictionary mapping shifted keys to non-shifted keys
shifted_key_mapping = {
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5',
    '^': '6',
    '&': '7',
    '*': '8',
    '(': '9',
    ')': '0',
    '_': '-',
    '+': '=',
    '{': '[',
    '}': ']',
    '|': '\\',
    ':': ';',
    '"': "'",
    '<': ',',
    '>': '.',
    '?': '/',
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z',
    # Add more shifted keys and their non-shifted counterparts here
}

shifted_key_mapping_backwards = {
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '-': '_',
    '=': '+',
    '[': '{',
    ']': '}',
    '\\': '|',
    ';': ':',
    "'": '"',
    ',': '<',
    '.': '>',
    '/': '?',
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z',
    # Add more shifted keys and their non-shifted counterparts here
}

# List to store the labels for the pressed key images
pressed_image_labels = []
# Dictionary to keep track of which label is associated with each key press
key_to_label = {}

# ------------------------------------------------------------------------------------------------------

# It gets pressed key and displays the image of the key
def on_press(key):
    # Make the key as str
    try:
        key_id = key.char
    except AttributeError:
        key_id = key

    sanitized_key_id = sanitize_key_id(str(key_id))

    # If the key is already pressed, ignore this event
    if key_id in key_to_label:
        return
    # Get the image for the pressed key
    try:
        pressed_image = PhotoImage(file=f"images/{sanitized_key_id}_pressed.png")
    except tk.TclError: # If the image does not exist, ignore this event
        return
    # Check if the image is already at pressed_image_labels
    available_label = None
    for label in pressed_image_labels:
        if not label.winfo_ismapped():
            available_label = label
            break
    # If there is no label available, create a new one
    if available_label is None:
        available_label = tk.Label(root)
        pressed_image_labels.append(available_label)

    # Set the image for the label
    available_label.config(image=pressed_image)
    available_label.image = pressed_image

    # Get the coordinates for the image
    x, y = key_coordinates.get(key_id , (0, 0))
    available_label.place(x=x, y=y)

    # Add the label to the dictionary
    key_to_label[key_id] = available_label

# It gets released key and removes the image of the key
def on_release(key):
    # Make the key as str
    try:
        key_id = key.char
    except AttributeError:
        key_id = key

    sanitized_key_id = sanitize_key_id(str(key_id))

    # Try to remove the image for the shifted version of the key
    shifted_key = None
    for k, v in shifted_key_mapping_backwards.items():
        if k == sanitized_key_id:
            shifted_key = v
            break
    if shifted_key is None:
        for k, v in shifted_key_mapping.items():
            if k == sanitized_key_id:
                shifted_key = v
                break
    if shifted_key is not None:
        label = key_to_label.get(str(shifted_key))
        if label is not None:
            label.config(image='')
            label.place_forget()
            del key_to_label[shifted_key]

    # Try to remove the image for the key
    label = key_to_label.get(key_id)
    if label is not None:
        label.config(image='')
        label.place_forget()
        del key_to_label[key_id]

# ------------------------------------------------------------------------------------------------------

# Assign the listeners
keyboard_listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click)

# Start the listeners
keyboard_thread = threading.Thread(target=keyboard_listener.start)
keyboard_thread.start()
mouse_thread = threading.Thread(target=mouse_listener.start)
mouse_thread.start()

# ------------------------------------------------------------------------------------------------------

# Tkinter thingy
root.mainloop()
