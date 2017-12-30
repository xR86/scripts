gnome-terminal\
	--tab\
		--working-directory=$PWD\
		-e "bash -c 'printf \"***grunt watch window***\n\n\";\
								grunt watch'"\
	--tab\
		--working-directory=$PWD\
		-e "bash -c 'printf \"***npm window***\n\n\";\
								npm start'"\
	--tab\
		--working-directory=$PWD\
		-e "bash -c 'printf \"***git/other window***\n\n\";\
								git status';bash"\

# grunt watch -> minifies files on change (blocking)
# npm start -> runs the node.js server (blocking)
# git status -> shows current changes (non-blocking)

# If separate windows are needed, just add gnome-terminal\ before --tab
