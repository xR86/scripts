
if [ ! -d "/home/$USER/adminMongo-master" ]; then
  echo "adminMongo folder doesn't exists, downloading ..."
  wget -O ~/adminMongo-master.zip "https://github.com/mrvautin/adminMongo/archive/master.zip"
  unzip ~/adminMongo-master.zip -d ~/
  npm install
fi

gnome-terminal\
	--tab\
		--working-directory="/home/$USER/adminMongo-master"\
		-e "bash -c 'printf \"***adminMongo server***\n\n\";\
								npm start'"\

# wait for server to start (so that frontend loads on xdg-open)
sleep 0.5

# xdg-utils must be present
# no outputs printed
xdg-open http://127.0.0.1:1234 > /dev/null 2>&1
# python -m webbrowser "http://127.0.0.1:1234"
