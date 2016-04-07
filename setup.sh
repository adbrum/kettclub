# Usage: source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Cloning repo...${reset}"
git clone https://github.com/adbrum/kettclub.git kettclub

echo "${green}>>> Enter in kettclub directory.${reset}"
cd kettclub

echo "${green}>>> Creating virtualenv...${reset}"
python -m venv .kett
echo "${green}>>> venv is created.${reset}"

sleep 2
echo "${green}>>> activate the venv.${reset}"
source .kett/bin/activate

echo "${green}>>> Short the prompt path.${reset}"
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\e[00m$ "
sleep 2

echo "${green}>>> Creating .env${reset}"
cp contrib/env-sample .env

echo "${green}>>> Load data...${reset}"
make

echo "${green}>>> Done.${reset}"