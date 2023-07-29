# echo "Installing libraries"
# sudo apt install libjpeg-dev zlib1g-dev
# sudo apt install python3-pip
# pip install spotipy --upgrade
# #  To open images
# pip install pillow --upgrade
# # Create graphic interface
# sudo apt-get install python3-tk

echo "Enter your Spotify Client ID:"
read spotify_client_id

echo "Enter your Spotify Client Secret:"
read spotify_client_secret

echo "Enter your Spotify Redirect URI:"
read spotify_redirect_uri

install_path=$(pwd)

echo "Removing spotict service if it exists:"
sudo systemctl stop spotict
sudo rm -rf /etc/systemd/system/spotict.*
sudo systemctl daemon-reload
echo "...done"

echo "Creating spotict service:"
sudo cp ./services/spotict.service /etc/systemd/system/
sudo sed -i -e "/\[Service\]/a ExecStart=/usr/bin/python3 ${install_path}/app.py" /etc/systemd/system/spotict.service
sudo sed -i -e "/\[Service\]/a Environment=\"SPOTIPY_REDIRECT_URI=${spotify_redirect_uri}\"" /etc/systemd/system/spotict.service
sudo sed -i -e "/\[Service\]/a Environment=\"SPOTIPY_CLIENT_SECRET=${spotify_client_secret}\"" /etc/systemd/system/spotict.service
sudo sed -i -e "/\[Service\]/a Environment=\"SPOTIPY_CLIENT_ID=${spotify_client_id}\"" /etc/systemd/system/spotict.service
sudo sed -i -e "/\[Service\]/a User=${$USER}" /etc/systemd/system/spotict.service
sudo systemctl daemon-reload
sudo systemctl start spotict
sudo systemctl enable spotict
echo "...done"

echo -n "In order to finish setup a reboot is necessary..."
echo -n "REBOOT NOW? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
        echo "Exiting without reboot."
        exit 0
fi
echo "Reboot started..."
reboot
sleep infinity
