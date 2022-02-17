# Colors scheme
red="\e[1;31m"
default="\e[0m"
yellow="\e[0;33m"
orange="\e[38;5;166m"
green="\033[92m"
cross="✗"
mark="✓"
right_arrow="❯"
interrogation="ʔ"

# Variables
url=$1
workdir=$(pwd)

clear
echo -e "$yellow  ██████╗ █████╗ ████████╗██████╗ ██╗  ██╗██╗███████╗██╗  ██╗  $green  ██╗   ██╗ ██████╗ "
echo -e "$yellow ██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║  ██║██║██╔════╝██║  ██║  $green  ██║   ██║██╔═████╗"
echo -e "$yellow ██║     ███████║   ██║   ██████╔╝███████║██║███████╗███████║  $green  ██║   ██║██║██╔██║"
echo -e "$yellow ██║     ██╔══██║   ██║   ██╔═══╝ ██╔══██║██║╚════██║██╔══██║  $green  ╚██╗ ██╔╝████╔╝██║"
echo -e "$yellow ╚██████╗██║  ██║   ██║   ██║     ██║  ██║██║███████║██║  ██║  $green   ╚████╔╝ ╚██████╔╝"
echo -e "$yellow  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝  $green    ╚═══╝   ╚═════╝ "
echo -e "$orange                                           Ciber-ToolKit Builtin                   "
echo -e "$orange                                                                                   "
echo -e "$orange                                           Author : Adrian Toral                   "
echo -e "$default"

if [[ ! $url ]]; then
  echo -e "$yellow""[$interrogation]""$green"" No URL selected, type an URL (example.com)  : ""$default"
  read -r url
fi

wget -r $url
if [[ $? -ne 0 ]]; then
  echo "$red""[$cross] Invalid URL. Try again later"
  exit 1
fi

ngrok http file://$workdir/$url >/dev/null

# link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o -e "https://a02d-81-35-144-195.ngrok.io")
# echo "$green""[$mark]"" Share this link : ""$orange""$link"

