# Author  : Adrian Toral
# Date    : 11-02-2022
# Code    : Ciber ToolKit Main Menu
# Version : Alpha

from os import system
from my_pickledb import LoadPickleDB, PickleDB
from utils import *

# Global Variables
TOOLKIT_TOOLS = LoadPickleDB("data/tools.json")
SYSTEM_CLEAR = lambda: system("clear")


class Tool(PickleDB):
    def __init__(self, name: str):
        """
        Class object to convert tool json data into PickleDB object
        This makes data fetching and updating easier and faster

        This are some explanation of the variables used in the process
            .tool -> It is the tool name, the key how it will be searched in json
            .path -> It is the tool download and installation path, every time an command is run, it will be executed in this path
            .cmd  -> It is the tool download and installation command, it will be executed once in the tool path
            .run  -> It is the tool initialization command, every time you want to start the tool, this command will be executed
            .requirements -> It is the tool requirements, not installation ones, it will be installed once

        :param name: Tool name
        """

        super().__init__(f"""{name}.json.tmp""", **TOOLKIT_TOOLS.get(name))

        # Tool name
        self.tool = name

        # GitHub repository to download or cURL url
        self.git = self.get("git") if self.exists("git") else self.get("curl") if self.exists("curl") else None

        # Download and installation path
        self.path = self.get("path")

        # Initialization command of the tool
        self.run = self.get("run")

        # Installation command
        self.installation = self.get("install")

        # Fix command
        self.fix = self.get("fix")

        # Tool requirements
        self.requirements = self.get("requirements")

        # Tool downloader and installer command
        if self.exists("git"):
            if not self.exists("fix"): self.cmd = f"""git clone {self.git} . && {self.installation}"""
            else: self.cmd = f"""git clone {self.git} . && {self.fix} && {self.installation}"""

        elif self.exists("curl"):
            if not self.exists("fix"): self.cmd = f"""curl {self.git} && {self.installation}"""
            else: self.cmd = f"""curl {self.git} . && {self.fix} && {self.installation}"""

        elif self.exists("wget"):
            if not self.exists("fix"): self.cmd = f"""wget {self.git} && {self.installation}"""
            else: self.cmd = f"""wget {self.git} . && {self.fix} && {self.installation}"""

        else: self.cmd = f"""{self.installation}"""

    def start(self):
        """
        Runs an installed tool by its name
        It will change directory to tool path and try to execute run command
        If failed, it will show an error message

        :return:
        """

        try:
            print(f"""{YELLOW}[{RIGHT_ARROW}] Running {self.tool} with {self.run}""")
            print(f"""{GREEN}[{MARK}] Response returned : {system(f"cd {self.path} && {self.run}")} status""")

        except: print(f"""{RED}[{CROSS}] Error while running {self.tool}. Try again later""")

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

        :param autorun: Runs tool automatically after installation if True
        :return:
        """

        # Downloads and install tool in path if it doesn't exist
        if not self.get("isInstalled"):
            print(f"""{YELLOW}[{INTERROGATION}] Running installer for {self.tool}""")

            # Creates tool path if it doesn't exist
            print(f"""{YELLOW}[{INTERROGATION}] Creating path for {self.tool}""")
            system(f"""if [ ! -d {self.path} ]; then  mkdir -p "{self.path}";  echo "{GREEN}""[{MARK}] {self.path} created. Done"; else echo "{ORANGE}""[{CROSS}] {self.path} already created. Skipping..."; fi""")

            # Runs tool fixer if exists
            if self.exists("fix"):
                print(f"""{YELLOW}[{INTERROGATION}] Running fixer for {self.tool}{GREEN}""")

            # Downloads and install tool in path
            system(f"""cd {self.path} && {self.cmd}""")
            print(f"""{GREEN}[{MARK}] {self.tool} installed correctly""")

            # Installs tool requirements if needed
            if self.get("isRequirements"):
                print(f"""{YELLOW}[{INTERROGATION}] Installing requirements for {self.tool}{GREEN}""")
                system(f"""cd {self.path} && {self.requirements}""")

            # Create a shortcut for tool
            print(f"""{GREEN}[{MARK}] Created shortcut tk-{self.tool.lower()}""")
            system(f"""touch /bin/tk-{self.tool.lower()} ; echo "#!/bin/bash" > /bin/tk-{self.tool.lower()}; echo 'cd {self.path} && {self.run} $@' >> /bin/tk-{self.tool.lower()}; chmod +x /bin/tk-{self.tool.lower()}""")

            # Changes tool json data
            self.set("isInstalled", 1)
            TOOLKIT_TOOLS.set(self.tool, self.json)

        else: print(f"""{ORANGE}[{CROSS}] {self.tool} is already installed. Skipping...""")

        # Save tools new json
        TOOLKIT_TOOLS.save.as_json()

        # Ask for running the tool
        run = False
        if not autorun: run = input(f"""{YELLOW}[{RIGHT_ARROW}] Do you want to run it (y/n): {DEFAULT}""").lower() in CONFIRMATION
        if run or autorun:
            SYSTEM_CLEAR()
            self.start()

        else: print(f"""{RED}[{CROSS}] Not running {self.tool}. Finishing""")


if __name__ == '__main__':
    """
    Shows toolkit main menu interface while its running
    Options variable contains all the available tags
    """

    isRunning = True
    categories = {
        str(i + 1): j
        for i, j in enumerate(
            TOOLKIT_TOOLS.get("__menu__").keys()
        )
    }

    SYSTEM_CLEAR()
    print(MAIN_BANNER)
    while isRunning:
        execute_on_bash = False

        command_to_execute = input(f"""{RED}ToolKit {RIGHT_ARROW}{DEFAULT} """).lower()

        if command_to_execute in CLEAN: SYSTEM_CLEAR(); print(MAIN_BANNER)

        elif command_to_execute in EXIT: isRunning = False

        elif command_to_execute in ["about", "help", "9"]: print(ABOUT_BANNER)

        elif command_to_execute in categories:
            SYSTEM_CLEAR()
            print(TOOL_TAG_BANNER)

            tool_and_info = list(
                TOOLKIT_TOOLS.get("__menu__").get(
                    categories.get(command_to_execute)
                ).items()
            )

            tool_keys = list(
                TOOLKIT_TOOLS.get("__menu__").get(
                    categories.get(command_to_execute)
                ).keys()
            )

            for tool_index, tool_data in enumerate(tool_and_info):
                """
                This are the iterated tool variables, some explanation of it are:
                    tool_name -> Regular name of the tool
                    tool_description -> Regular description of the tool
                    tool_index -> The position of the tool in the saved json
                    tool_tags -> A list with all tool tags
                    tool_colortype -> Color to know if the tool is CLI only, CLI and CLI-GUI or CLI-GUI
                    tool_to_execute -> Tool name or index to execute
                    tool_argv -> Tool execution arguments
                """
                tool_name = tool_data[0]
                tool_description = tool_data[1]
                tool_index = "0" + str(tool_index) if tool_index < 10 else tool_index
                tool_tags = TOOLKIT_TOOLS.get(tool_name).get("tags")
                tool_status =TOOLKIT_TOOLS.get(tool_name).get("isWorking")

                if "CLI" in tool_tags: tool_colortype = PURPLE
                elif "CLI-BOTH" in tool_tags: tool_colortype = CYAN
                elif "KALI" in tool_tags: tool_colortype = DARKGREY
                else: tool_colortype = BLUE

                if tool_status == "W": tool_status = f"""{GREEN}Working"""
                elif tool_status == "M": tool_status = f"""{YELLOW}Maintenance"""
                elif tool_status == "N": tool_status = f"""{RED}Not Working"""

                print(f"""{YELLOW}{tool_index}) {tool_colortype}{tool_name} {DEFAULT}{tool_description} {tool_status}""")

            print(f"""{YELLOW}99) Back{DEFAULT}""")
            print()
            print(f"""{YELLOW}[*] {PURPLE}CLI""")
            print(f"""{YELLOW}[*] {BLUE}CLI-GUI""")
            print(f"""{YELLOW}[*] {CYAN}CLI / CLI-GUI""")
            print(f"""{YELLOW}[*] {DARKGREY}KALI / DOCKER""")

            tool_to_execute_raw = input(f"""{RED}ToolKit {RIGHT_ARROW}{DEFAULT} """)
            tool_to_execute = tool_to_execute_raw.split()[0]
            tool_argv = tool_to_execute_raw.split()[1:]

            try:
                if tool_to_execute in CLEAN or tool_to_execute in PASS: SYSTEM_CLEAR(); print(MAIN_BANNER)

                elif tool_to_execute in EXIT: isRunning = False

                elif tool_to_execute in tool_keys: Tool(tool_to_execute).install(any(x in CONFIRMATION for x in tool_argv))

                elif int(tool_to_execute) <= len(tool_and_info): Tool(tool_and_info[int(tool_to_execute)][0]).install(any(x in CONFIRMATION for x in tool_argv))

                else:
                    command_to_execute = tool_to_execute_raw
                    execute_on_bash = True

            except:
                command_to_execute = tool_to_execute_raw
                execute_on_bash = True

        else: execute_on_bash = True

        if execute_on_bash:
            try:
                SYSTEM_CLEAR()

                print(f"""{GREEN}[{MARK}] Executed '{command_to_execute}' successfully""")
                print(f"""{GREEN}[{MARK}] Response returned : {system(f'''bash -c "{command_to_execute}" ''')} status""")

            except: print(f"""{RED}[{CROSS}] Command '{command_to_execute}' returned error. Try again later""")
