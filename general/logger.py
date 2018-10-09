"""Logger misc.

"""
import datetime as dt
import sys

def logger(msg):
	"""Logs stuff for stuff
	
	Arguments:
		msg [str] -- [description]
	"""
	# pending more intelligent logging
	now = dt.datetime.now().strftime('%H:%M:%S')
	caller = sys._getframe(1).f_code.co_name

	# https://pypi.org/project/colorama/
	# https://misc.flogisoft.com/bash/tip_colors_and_formatting
	# https://gist.github.com/chrisopedia/8754917
	# 
	# red = '\033[31m'
	# reset = '\033[30m'

	print('\033[31m %s \033[0m-\033[36m %s()\033[0m - %s' % (now, caller, msg))


def misc_colors():
	print('Normal \033[1mBold\033[0m \033[2mDim\033[0m \033[4mUnderlined\033[0m \033[5mBlink\033[0m \033[7minverted\033[0m \033[8mHidden\033[0m')
	print('Default \033[39mDefault \033[30mBlack \033[31mRed \033[32mGreen \033[33mYellow \033[34mBlue \033[35mMagenta \033[36mCyan  \033[37mLight gray \033[90mDark gray \033[91mLight red \033[92mLight green \033[93mLight yellow \033[94mLight blue \033[105mLight magenta \033[106mLight cyan \033[107mWhite \033[0m')

	print("".join(
		["\033[38;5;%sm#\033[0m" % 
		i for i in 
			list(range(0, 257))
		]))

	print("".join(
		["\033[38;5;%sm#\033[0m" % 
		i for i in 
			list(range(16, 22)) + list(range(16, 22))[::-1]
		]))

	print("".join(
		["\033[48;5;%sm#\033[0m" % 
		i for i in 
			list(range(16, 22)) + list(range(16, 22))[::-1]
		]))

	# print("".join(
	# 	["\033[48;5;%sm#\033[0m" % 
	# 	i for i in 
	# 		list(range(0, 257))
	# 	]))
	code = ["\033[48;5;%sm  %s  \033[0m" % 
		(i,i) for i in 
			list(range(0, 257))
		]

	print(''.join(l + '\n' * (n % 3 == 2) for n, l in enumerate(code)))


if __name__ == '__main__':
	logger('This happened')
	misc_colors()
