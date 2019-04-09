echo "This script will create virtual environment,"
echo "make migrations, and if you want start server."
read -p "Click ""ENTER"" continue."
echo "Installing virtual environment..."
sudo apt install virtualenv
echo "---------------------------------------------------"
echo "Creating virtual environment in current directory"
echo "---------------------------------------------------"
virtualenv -p python3 skyvenv
# pip install -r requirements.txt
sky-venv/bin/pip install -r requirements.txt
source ./skyvenv/bin/activate
echo "---------------------------------------------------"
echo "Installation completed"
echo "---------------------------------------------------"
read -r -p "Do you want to start server? [Y/n] " response
echo
response=${response,,} # tolower
if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
echo "---------------------------------------------------"
echo "Making migrations"
echo "---------------------------------------------------"
python manage.py migrate
echo "---------------------------------------------------"
python manage.py runserver
fi
if [[ $response =~ ^(no|n| ) ]] || [[ -z $response ]]; then
exit
fi