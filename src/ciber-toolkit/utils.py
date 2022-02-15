# Colors and emojis
BLUE = "\33[94m"
RED = "\033[91m"
WHITE = "\33[97m"
CYAN = "\033[36m"
DEFAULT = "\033[0m"
YELLOW = "\33[93m"
ORANGE = "\e[38;5;166m"
MAGENTA = "\033[1;35m"
GREEN = "\033[1;32m"
END = "\033[0m"
BOLD = "\033[1m"
CROSS = "✗"
MARK = "✓"
RIGHT_ARROW = "❯"
INTERROGATION = "ʔ"

# Validation arrays
CONFIRMATION = ["-y", "-yes", "y", "yes", "true"]
EXIT = ["exit", "break", "stop", "10", "false"]
CLEAN = ["clear", "clean", "c", ""]
PASS = ["back", "pass", "skip", "99"]

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
    {WHITE}|          [02] {YELLOW}Phishing{WHITE}                  |       [07] {YELLOW}Others{WHITE}                       |
    {WHITE}|                                         |                                         |
    {WHITE}|          [03] {YELLOW}Wifi Attacks{WHITE}              |       [08] {YELLOW}Custom tools{RED} [Under Dev.]{WHITE}    |
    {WHITE}|                                         |                                         |
    {WHITE}|          [04] {YELLOW}Passwords Attacks{WHITE}         |       [09] {YELLOW}About{WHITE}                        |
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
