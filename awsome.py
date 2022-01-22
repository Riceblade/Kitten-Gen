import ctypes
import colorama
import time
import pyfiglet
import random
from colorama import Fore, Back, Style
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("Kitten Gen")
print(f"{Fore.BLUE}")

trolldeo = pyfiglet.figlet_format("Kitten Gen")
print(trolldeo)
print("for frozie")
print("")
time.sleep(0.5)
print("Follow instructions\n")
time.sleep(0.2)
print(f"{Fore.BLUE}")


def choose_word():
    list_of_words = []
    with open('kitten.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_word = random.choice(list_of_words)
    print(f"{uname}'s Kitten's Tag: ", chosen_word)
    print("==========================")
    time.sleep(2)


def choose_gen():
    time.sleep(2)
    list_of_words = []
    with open('gender.txt') as f:
        line = f.readline().strip()
        while line:
            list_of_words.append(line)
            line = f.readline().strip()
    chosen_gen = random.choice(list_of_words)
    print(f"{uname}'s Kitten's Gender: ", chosen_gen)
    print("==========================")


uname = input('Hello, Who are you picking a kitten for?: ')
print(" ")
choose_word()
print(f"{uname}'s Kitten's Age:", random.randint(8, 15))
print("==========================")
choose_gen()
print(" ")
