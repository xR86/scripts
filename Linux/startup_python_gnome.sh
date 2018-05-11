gnome-terminal\
	--tab\
		--working-directory=$PWD\
		-e "bash -c 'printf \"***python3 server***\n\n\";\
								python3 -m http.server'"\
	--tab\
		--working-directory=$PWD\
		-e "bash -c 'printf \"***git/other window***\n\n\";\
								git status';bash"\

# python3 -> localhost files served by python built-in server (blocking)
# git status -> shows current changes (non-blocking)

# If separate windows are needed, just add gnome-terminal\ before --tab
