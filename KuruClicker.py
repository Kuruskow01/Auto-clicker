import time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
import threading
import colorama
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from colorama import Fore, Back, Style, init
from time import sleep
import sys
from os import system

system("python icon.ico")
system('cls')
start_click = input(f"{Fore.BLUE}what put for start/stop click ?\n              ")
system('cls')
close_click = input(f"{Fore.BLUE}what put for close clicker ?\n                ")
system('cls')


colorama.init()
sys.stderr.write(colorama.Fore.RED + """
 ██ ▄█▀ █    ██  ██▀███   █    ██     ▄████▄   ██▓     ██▓ ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██▄█▒  ██  ▓██▒▓██ ▒ ██▒ ██  ▓██▒   ▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒▓██  ▒██░   ▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ▓▓█  ░██░   ▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒▒▒█████▓    ▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒    ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒ ▒░░░▒░ ░ ░   ░▒ ░ ▒░░░▒░ ░ ░      ░  ▒   ░ ░ ▒  ░ ▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░ ░░ ░  ░░░ ░ ░   ░░   ░  ░░░ ░ ░    ░          ░ ░    ▒ ░░        ░ ░░ ░    ░     ░░   ░ 
░  ░      ░        ░        ░        ░ ░          ░  ░ ░  ░ ░      ░  ░      ░  ░   ░     
                                     ░                    ░                               
\n""")

sys.stderr.write(colorama.Fore.BLUE + f'Press "{start_click}" for starting/stoping a auto-clickers \nPress "{close_click}" for close a auto-clickers')

delay = 0.08
button = Button.left
start_stop_key = KeyCode(char=f'{start_click}')
exit_key = KeyCode(char=f'{close_click}')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()