"""docker image cleaner"""

import docker
import os
import sys

client = docker.from_env()


# equivalent of: `docker images`
def list_images():
	print(client.images.list(all=True, filters={
		"dangling": True
	}))

def list_ignored():
	# simple txt file, each row is a image name
	path = os.path.expanduser('~/.imageignore')

	with open(path, 'r') as f:
		data = f.read().split('\n')
		ignored = list(filter(None, data))

	return ignored

def remove_images():
	ignored = list_ignored()
	print('ignored: %s' % ignored)

	remove_images_safe()

	removed = []
	for image in client.images.list(all=True):
		img_name = '' if len(image.tags) < 1 else image.tags[0]
		img_id = image.id
		print('name: %s,\n id: %s' % (img_name, img_id))

		if img_name not in ignored:
			# remove fails: https://stackoverflow.com/a/26692854
			client.images.remove(image=img_id, force=True)

			removed.append(img_name)

	print('removed: %s' % removed)

def remove_images_safe():
	# --safe - using built-in prune method, 
	#          it will delete unused images only
	list_images()

	# similar command
	# docker rmi $(docker images -f "dangling=true" -q)
	pruned = client.images.prune(filters={
		"dangling": True
	})
	print('pruned: %s' % pruned)

	list_images()


if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == '--safe':
			remove_images_safe()
	else:
		remove_images()
