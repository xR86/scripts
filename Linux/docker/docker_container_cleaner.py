"""docker container cleaner"""

import docker
import os

client = docker.from_env()


# equivalent of: `docker ps -a`
def list_containers():
	print(client.containers.list(all=True))

def list_ignored():
	# simple txt file, each row is a container name
	path = os.path.expanduser('~/.containerignore')

	with open(path, 'r') as f:
		data = f.read().split('\n')
		ignored = list(filter(None, data))

	return ignored

def remove_containers():
	ignored = list_ignored()
	print('ignored: %s' % ignored)

	removed = []
	for container in client.containers.list(all=True):
		if container.name not in ignored:
			if container.status != 'exited':
				container.stop()
			container.remove()

			removed.append(container.name)

	print('removed: %s' % removed)


if __name__ == "__main__":
	remove_containers()
