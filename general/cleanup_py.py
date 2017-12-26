"""
Utility functions for finding dependencies locations.
"""
import site

def get_package_install_locations():
	'''
	There was also this method:
	```
	from distutils.sysconfig import get_python_lib
	print(get_python_lib())
	```
	'''
	return site.getsitepackages()

def recursive_find_peer_deps(find_peerdep):
	'''
	Call get_package_install_locations and start from there.
	Find any requirements.txt files where find_peerdep is listed, save to list
	Print list with locations of the packages where peerdep is needed(parse pip freeze ??)
	Print list with locations of the packages where peerdep is needed(parse pip freeze ??)
	'''
	pass

def json_file_location_stub():
	import json # is this lazy importing ?
	return json.__file__

def pip_freeze():
	from pip.operations import freeze
	x = freeze.freeze()
	return list(x)


if __name__ == '__main__':
	
	# get_package_install_locations()
	print(get_package_install_locations())
	print()

	# json_file_location_stub()
	print(json_file_location_stub())
	print()

	# pip_freeze()
	# print(help('modules'))
	p_fr = pip_freeze()
	# print('\n'.join('{}: {}'.format(*k) for k in enumerate(p_fr)))
	print('\n'.join('%s' % pkg for pkg in p_fr))
