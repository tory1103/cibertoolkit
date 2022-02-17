source config.sh

# Update directory
workdir="$(pwd)/src/ciber-toolkit"

# Update files
fileupdate=$(echo "$1" | tr '[:upper:]' '[:lower:]')
if [[ -z $fileupdate ]]; then
  fileupdate="all"
fi

# Banner
clear
echo -e "$yellow _________ ._____.                        _______________  __. "
echo -e "$yellow \_   ___ \|__\_ |__   ___________        \__    ___/    |/ _| "
echo -e "$yellow /    \  \/|  || __ \_/ __ \_  __ \  ______ |    |  |      <   "
echo -e "$yellow \     \___|  || \_\ \  ___/|  | \/ /_____/ |    |  |    |  \  "
echo -e "$yellow  \______  /__||___  /\___  >__|            |____|  |____|__ \ "
echo -e "$yellow         \/        \/     \/                                \/ "
echo -e "$yellow  ____ ___            .___       __                            "
echo -e "$yellow |    |   \______   __| _/____ _/  |_  ___________             "
echo -e "$yellow |    |   /\____ \ / __ |\__  \\   __\/ __ \_  __ \            "
echo -e "$yellow |    |  / |  |_> > /_/ | / __ \|  | \  ___/|  | \/            "
echo -e "$yellow |______/  |   __/\____ |(____  /__|  \___  >__| /\  /\  /\    "
echo -e "$yellow           |__|        \/     \/          \/     \/  \/  \/    "
echo -e "$orange                          Ciber-ToolKit Updater                "
echo -e "$orange                                                               "
echo -e "$orange                          Author : Adrian Toral                "
echo -e "$default"

if [[ $fileupdate == "all" || $fileupdate == "toolkit" ]]; then
  rm "$workdir/toolkit.py"
  wget https://raw.githubusercontent.com/tory1103/cibertoolkit/master/src/ciber-toolkit/toolkit.py -O $workdir/toolkit.py
fi

if [[ $fileupdate == "all" || $fileupdate == "utils" ]]; then
  rm "$workdir/utils.py"
  wget https://raw.githubusercontent.com/tory1103/cibertoolkit/master/src/ciber-toolkit/utils.py -O $workdir/utils.py
fi

if [[ $fileupdate == "all" || $fileupdate == "tools" ]]; then
  rm "$workdir/data/*.json"
  wget https://raw.githubusercontent.com/tory1103/cibertoolkit/master/src/ciber-toolkit/data/tools.json -O $workdir/data/tools.json
  cp "$workdir/data/tools.json" "$workdir/data/backup.json"
fi

echo -e "$green"
echo -e "╔─────────────────────╗"
echo -e "|[$mark] Update complete.|"
echo -e "┖─────────────────────┙"
