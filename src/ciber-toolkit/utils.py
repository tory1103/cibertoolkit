# Colors and emojis
DEFAULT = "\033[0m"
BOLD = "\033[1m"
DISABLE = '\033[02m'
UNDERLINE = '\033[04m'
REVERSE = '\033[07m'
STRIKETHROUGH = '\033[09m'
INVISIBLE = '\033[08m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'
WHITE = "\33[97m"

print(BLUE, "hola", DARKGREY, "adios")

BACKGROUND_BLACK = '\033[40m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_ORANGE = '\033[43m'
BACKGROUND_BLUE = '\033[44m'
BACKGROUND_PURPLE = '\033[45m'
BACKGROUND_CYAN = '\033[46m'
BACKGROUND_LIGHTGREY = '\033[47m'

CROSS = "✗"
MARK = "✓"
RIGHT_ARROW = "❯"
INTERROGATION = "ʔ"

# Validation arrays
CONFIRMATION = ["-y", "-yes", "y", "yes", "true"]
EXIT = ["exit", "break", "stop", "10", "false"]
CLEAN = ["clear", "clean", "c", ""]
PASS = ["b", "back", "pass", "skip", "99"]

# Banners
MAIN_BANNER = f"""
{RED}
            __  ____  ____     ___  ____         ______  __  _     
           /  ]l    j|    \   /  _]|    \       |      T|  l/ ]    
          /  /  |  T |  o  ) /  [_ |  D  )_____ |      ||  ' /     
         /  /   |  | |     TY    _]|    /|     |l_j  l_j|    \     
        /   \_  |  | |  O  ||   [_ |    \l_____j  |  |  |     Y    
        \     | j  l |     ||     T|  .  Y        |  |  |  .  |    
         \____j|____jl_____jl_____jl__j\_j        l__j  l__j\_j    
                                               By: Adrian Toral     

    {WHITE}╔───────────────────────────────────────────────────────────────────────────────────╗
    {WHITE}|                                        MENU                                       |
    {WHITE}|───────────────────────────────────────────────────────────────────────────────────|
    {WHITE}|                                         |                                         |
    {WHITE}|          [01] {YELLOW}Spoofing{WHITE}                  |       [06] {YELLOW}Information Gathering{WHITE}        |
    {WHITE}|                                         |                                         |
    {WHITE}|          [02] {YELLOW}Phishing{WHITE}                  |       [07] {YELLOW}Forensic{WHITE}                     |
    {WHITE}|                                         |                                         |
    {WHITE}|          [03] {YELLOW}Wifi Attacks{WHITE}              |       [08] {YELLOW}Others{WHITE}                       |
    {WHITE}|                                         |                                         |
    {WHITE}|          [04] {YELLOW}Cryptography{WHITE}              |       [09] {YELLOW}About{WHITE}                        |
    {WHITE}|                                         |                                         |
    {WHITE}|          [05] {YELLOW}Web Attacks{WHITE}               |       [10] {YELLOW}Exit{WHITE}                         |
    {WHITE}┖───────────────────────────────────────────────────────────────────────────────────┙
    {DEFAULT}"""
ABOUT_BANNER = f"""
{GREEN}
                ╔──────────────────────────────────────────────────╗
                |               Author: Adrián Toral               |
                |           Ciber ToolKit Copyright 2022           |
                | Github: https://github.com/tory1103/cibertoolkit |
                |                      v1.0.0                      |
                |                                                  |
                ┖──────────────────────────────────────────────────┙
"""
CUSTOM_BANNER = f"""{YELLOW}[*] Custom under development. Try again later...{DEFAULT}"""
TOOL_TAG_BANNER = f"""========={GREEN}Tool{DEFAULT}==================================={GREEN}Information{DEFAULT}================================"""
