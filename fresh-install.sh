# Colors
red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'
cross='✗'
mark='✓'
right_arrow='❯'

# Installation directory
workdir="/usr/bin/cibertk"

# Check root
if [[ "$(id -u)" != "0" ]]; then
  echo "$red""[$cross] This script needs root access. Try running 'sudo $SHELL install.sh'"
  exit
fi

# Banner
clear
echo -e "$yellow _________ ._____.                        _______________  __.                               "
echo -e "$yellow \_   ___ \|__\_ |__   ___________        \__    ___/    |/ _|                               "
echo -e "$yellow /    \  \/|  || __ \_/ __ \_  __ \  ______ |    |  |      <                                 "
echo -e "$yellow \     \___|  || \_\ \  ___/|  | \/ /_____/ |    |  |    |  \                                "
echo -e "$yellow  \______  /__||___  /\___  >__|            |____|  |____|__ \                               "
echo -e "$yellow         \/        \/     \/                                \/                               "
echo -e "$yellow ___________                     .__              .___                 __         .__  .__   "
echo -e "$yellow \_   _____/______   ____   _____|  |__           |   | ____   _______/  |______  |  | |  |  "
echo -e "$yellow  |    __) \_  __ \_/ __ \ /  ___/  |  \   ______ |   |/    \ /  ___/\   __\__  \ |  | |  |  "
echo -e "$yellow  |     \   |  | \/\  ___/ \___ \|   Y  \ /_____/ |   |   |  \\___ \  |  |  / __ \|  |_|  |__"
echo -e "$yellow  \___  /   |__|    \___  >____  >___|  /         |___|___|  /____  > |__| (____  /____/____/"
echo -e "$yellow      \/                \/     \/     \/                   \/     \/            \/           "
echo -e "$orange                         Ciber-ToolKit Installer                                             "
echo -e "$orange                                                                                             "
echo -e "$orange                          Author : Adrian Toral                                              "
echo -e "$default"

$SHELL uninstall.sh
$SHELL install.sh $@
