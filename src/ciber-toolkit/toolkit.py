# Author : Adrian Toral
# Date   : 11-02-2022
# Code   : Ciber ToolKit Main Menu

from os import system
from my_pickledb import LoadPickleDB, PickleDB

# Global Variables
BLUE = '\33[94m'
RED = '\033[91m'
WHITE = '\33[97m'
CYAN = '\033[36m'
DEFAULT = '\033[0m'
YELLOW = '\33[93m'
MAGENTA = '\033[1;35m'
GREEN = '\033[1;32m'
END = '\033[0m'
BOLD = '\033[1m'
CROSS = '✗'
MARK = '✓'
RIGHT_ARROW = '❯'

TKJSON = LoadPickleDB("data/tools.json")
CONFIRMATION = ["-y", "-yes", "y", "yes", "true"]


class Tool(PickleDB):
    def __init__(self, name: str):
        """
        Class object to convert tool json data into PickleDB object
        This makes data fetching and updating easier and faster

        :param name: Tool name
        """

        super().__init__(f"{name}.json.tmp", **TKJSON.get(name))

        """
        This are some explanation of the variables used in the process
            .tool -> It is the tool name, the key how it will be searched in json
            .path -> It is the tool download and installation path, every time an command is run, it will be executed in this path
            .cmd  -> It is the tool download and installation command, it will be executed once in the tool path
            .run  -> It is the tool initialization command, every time you want to start the tool, this command will be executed
            .requirements -> It is the tool requirements, not installation ones, it will be installed once
        """

        # Tool name
        self.tool = name

        # Download and installation path
        self.path = self.get("path")

        # Initialization command of the tool
        self.run = self.get("run")

        # Tool requirements
        self.requirements = self.get("requirements")

        # Tool downloader and installer command
        if self.exists("git"):
            if not self.exists("fix"):
                self.cmd = "git clone {} . && {}".format(self.get("git"), self.get("install"))
            else:
                self.cmd = "git clone {} . && {} && {}".format(self.get("git"), self.get("fix"), self.get("install"))
        elif self.exists("curl"):
            if not self.exists("fix"):
                self.cmd = "curl {} && {}".format(self.get("curl"), self.get("install"))
            else:
                self.cmd = "curl {} && {} && {}".format(self.get("curl"), self.get("fix"), self.get("install"))
        else:
            self.cmd = "{}".format(self.get("install"))

    def start(self):
        """
        Runs an installed tool by its name
        It will change directory to tool path and try to execute run command
        If failed, it will show an error message

        :return:
        """

        try:
            print(f"{GREEN}[{RIGHT_ARROW}] Running {self.tool} with {self.run}")
            system(f"cd {self.path} && {self.run}")
        except:
            print(f"{RED}[{CROSS}] Error while running {self.tool}. Try again later")

    def install(self, autorun: int = 0):
        """
        Downloads and install to path a tool
        It will download it through git or curl, depending on the tool install method
        It will change directory to tool path, and download it there
        After downloading, it will ask to run tool

        In some cases, a fixer is going to be executed, this makes all tools compatible with your os
        If tool is already downloaded, it will skip it.

        The installation steps are followed in this order:
            |- Directory creation
            |- Clone tool files in directory
            |-- Fix command if posible
            |- Install command
            |- Requirements command
            |- Run command

        :param autorun: Runs tool automatically if True
        :return:
        """

        # Check if json has tool name
        if not TKJSON.exists(self.tool):
            print(f"{RED}[{CROSS}] Invalid tool {self.tool}. Check if it is spelled correctly")
            return -1

        # Downloads and install tool in path if it doesn't exist
        if not self.get("isInstalled"):
            # Creates tool path if it doesn't exist
            print(f"""{GREEN}[{RIGHT_ARROW}] Running installer for {self.tool}""")
            system(f"""if [ ! -d {self.path} ]; then  mkdir -p "{self.path}";  echo "{GREEN}""[{MARK}] {self.path} created. Done"; else echo "{GREEN}""[{MARK}] {self.path} already created. Skipping..."; fi""")

            # Runs tool fixer if exists
            if self.exists("fix"):
                print(f"""{YELLOW}[{RIGHT_ARROW}] Running fixer for {self.tool}{GREEN}""")

            # Downloads and install tool in path
            system(f"cd {self.path} && {self.cmd}")
            print(f"{GREEN}[{MARK}] {self.tool} installed correctly")

            # Installs tool requirements if needed
            if self.get("isRequirements"):
                print(f"""{YELLOW}[{RIGHT_ARROW}] Installing requirements for {self.tool}{GREEN}""")
                system(f"cd {self.path} && {self.requirements}")

            # Create a shortcut for tool
            print(f"{GREEN}[{MARK}] Created shortcut tk-{self.tool}")
            system(f"""touch /bin/tk-{self.tool} ; echo "#!/bin/bash" > /bin/tk-{self.tool}; echo 'cd {self.path} && {self.run} $@' >> /bin/tk-{self.tool}; chmod +x /bin/tk-{self.tool}""")

            # Changes tool json data
            self.set("isInstalled", 1)
            TKJSON.set(self.tool, self.json)

        else:
            print(f"""{GREEN}[{MARK}] {self.tool} is already installed. Skipping...""")

        # Save tools new json
        TKJSON.save.as_json()

        # Ask for running the tool
        run = False
        if not autorun: run = input(f"{YELLOW}[{RIGHT_ARROW}] Do you want to run it (y/n): {DEFAULT}").lower() in CONFIRMATION
        if run or autorun:
            system("clear")
            self.start()
        else:
            print(f"{GREEN}[{RIGHT_ARROW}] Not running {self.tool}. Finishing")


if __name__ == '__main__':
    """
    Shows toolkit main menu interface while its running
    Options variable contains all the available tags
    """

    running = True
    options = {
        str(i + 1): j
        for i, j in enumerate(
            TKJSON.get("__menu__").keys()
        )
    }

    while running:
        # Banner
        system("clear")
        print(
            f"""{RED}
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
        )

        selection = input(f"{RED}ToolKit {RIGHT_ARROW}{DEFAULT}")

        if selection == "10": running = False

        elif selection == "9":
            print(
                """
                ╔──────────────────────────────────────────────────╗
                |               Author: Adrián Toral               |
                |           Ciber ToolKit Copyright 2022           |
                | Github: https://github.com/tory1103/cibertoolkit |
                |                      v1.0.0                      |
                |                                                  |
                ┖──────────────────────────────────────────────────┙
                            """
            )
            system("sleep 2")

        elif selection == "8":
            print("CUSTOM")
            system("sleep 2")

        elif selection in options:
            system("clear")
            print(f"========={GREEN}Tool{DEFAULT}==================================={GREEN}Information{DEFAULT}================================")
            tag_tools_info = list(TKJSON.get("__menu__").get(options.get(selection)).items())
            for index, tool in enumerate(tag_tools_info):
                print(f"{'0' + str(index) if index < 10 else index}) {MAGENTA if 'CLI' in TKJSON.get(tool[0]).get('tags') else CYAN if 'CLI-BOTH' in TKJSON.get(tool[0]).get('tags') else BLUE}{tool[0]}{DEFAULT} {tool[1]}")
            print(f"99) {YELLOW}Back{DEFAULT}")
            print(f"\n{MAGENTA}[*] CLI")
            print(f"{BLUE}[*] CLI-GUI")
            print(f"{CYAN}[*] CLI / CLI-GUI")

            selection = input(f"{RED}ToolKit {RIGHT_ARROW}{DEFAULT}").split()
            confirmation = selection[-1]
            selection = int(selection[0])

            if selection <= len(tag_tools_info):
                Tool(tag_tools_info[selection][0]).install(1 if confirmation.lower() in CONFIRMATION else 0)
        else:
            try:
                system(f"""bash -c "{selection}" """)
            except:
                print(f"{RED}[{CROSS}] Command returned error. Try again")
