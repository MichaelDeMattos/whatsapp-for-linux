#!/usr/bin/bash

echo -n "Enter the username to start the installation: "
 read user

echo "Installation is starting"

apt update 

apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 -y

apt update

apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 -y

apt update 

apt install webkit2gtk-driver -y

cp -r /home/$user/whatsapp-for-linux /usr/local/bin/
chmod +x /usr/local/bin/whatsapp-for-linux/app/whatsapp.pyc
cp /usr/local/bin/whatsapp-for-linux/app/whatsapp.desktop /usr/share/applications/
chmod +x /usr/share/applications/whatsapp.desktop
echo "Installation completed"
