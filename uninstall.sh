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
echo -e "$yellow _________ ._____.                        _______________  __.                  "
echo -e "$yellow \_   ___ \|__\_ |__   ___________        \__    ___/    |/ _|                  "
echo -e "$yellow /    \  \/|  || __ \_/ __ \_  __ \  ______ |    |  |      <                    "
echo -e "$yellow \     \___|  || \_\ \  ___/|  | \/ /_____/ |    |  |    |  \                   "
echo -e "$yellow  \______  /__||___  /\___  >__|            |____|  |____|__ \                  "
echo -e "$yellow         \/        \/     \/                                \/                  "
echo -e "$yellow  ____ ___      .__                 __         .__  .__                         "
echo -e "$yellow |    |   \____ |__| ____   _______/  |______  |  | |  |   ___________          "
echo -e "$yellow |    |   /    \|  |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \         "
echo -e "$yellow |    |  /   |  \  |   |  \\___ \  |  |  / __ \|  |_|  |_\  ___/|  | \/         "
echo -e "$yellow |______/|___|  /__|___|  /____  > |__| (____  /____/____/\___  >__| /\  /\  /\ "
echo -e "$yellow              \/        \/     \/            \/               \/     \/  \/  \/ "
echo -e "$orange                         Ciber-ToolKit Installer                                "
echo -e "$orange                                                                                "
echo -e "$orange                          Author : Adrian Toral                                 "
echo -e "$default"

# Requirements uninstall
python3 -m pip uninstall -r "$(pwd)/requirements.txt" -y

if [[ -d $workdir ]]; then
  # Shortcuts remove
  for tag in $(ls $workdir/tools); do
    for tool in $(ls $workdir/tools/$tag); do
      rm "/bin/tk-$tool"
    done
  done

  # Shortcut remove
  rm "/bin/toolkit"
  rm "/bin/toolkit-freshinstall"
  rm "/bin/toolkit-uninstall"

  # Main folder remove
  rm -rf $workdir
fi

# Removing saved json
rm "$(pwd)/src/ciber-toolkit/data/tools.json"
mv "$(pwd)/src/ciber-toolkit/data/backup.json" "$(pwd)/src/ciber-toolkit/data/tools.json"

echo -e "$green"
echo -e "╔───────────────────────╗"
echo -e "|[$mark] Uninstall complete.|"
echo -e "┖───────────────────────┙"
