# Visual Keyboard
This is a simple visual keyboard that can be used to check what keys are being pressed.

## Description

So my keyboard and system keyboard layout are not same, because I dont have money to buy a new keyboard. So I write this
code to check what key is being pressed. This code will show a visual keyboard and highlight the key that is being pressed.

It will show you exactly what key is being pressed(Like if you press ~ it will show ~ on the screen not ` and ~).
It will be hide in left corner and when mouse is on that location it will shift to right to see all of it.

You can change its location by just clicking your mouse to left corner of your screen.

I guess it can be usefull for 10 finger typing practice. Idk just do whatever you want with it.

## How to use

### For non-developers
If you are not developer and just want to download the exe + images file you can check the release section.

Just run the exe file and you are good to go. 

There is no window corner so you can't close the window by clicking on it.
You can close it through task manager.

### For developers
You will need Pillow, Pynput and Python 3.12 to run this code. You can install libraries by running this command:
1. **Clone the Repository**

   First, you need to create a local copy of this repository. Open a terminal and run the following command:

   ```bash
   git clone https://github.com/LucaLightW/Visual-Keyboard.git
   cd where\ever\it\is\Visual-Keyboard
    ```

2. **Create new virtual environment**
    ```bash
    python -m venv name_of_your_virtual_environment
    ```
   
3. **Activate the virtual environment**
    ```bash
   activate name_of_your_virtual_environment
    ```
   
4. **Install the Required Libraries**
    ```bash
    pip install Pillow pynput
    ```

5. **Run the Code**
    ```bash
    python main.py
    ```
   or just double click on the main.py file and run the code on your IDE.


You may change anything you would like, in the code. I tried to add many comments as possible to make it easy to understand.
And if you have any question you can ask me on my discord: lucalight_w

## Known issues and bugs
They all just visual bugs so it will not affect the functionality of the code.

So when it first opened if you move your mouse over it, it will not shift to right. You have to click on somewhere on left corner(idk why there is such problem sorry).

When you clicked somewhere different and moved the window, it will do some little 'flick' for a frame.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Idk if this is needed
Image for keyboard (also [edit.png](edit.png) file is same): [upload.wikimedia.org/...](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/ANSI_US_QWERTY_%28Windows%29.svg/1280px-ANSI_US_QWERTY_%28Windows%29.svg.png)

I did this with Copilot -our lord and saviour- from Github. 

And this is my first project. soooo... yeah.

