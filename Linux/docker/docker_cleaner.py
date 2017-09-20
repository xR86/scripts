"""docker cleaner"""

import docker
client = docker.from_env()

print(client.containers.list(all=True))

# simple txt file, each row is a container name
with open('.containerignore', 'r') as f:
	data = f.read().split('\n')
	ignored = list(filter(None, data))
	print('data: %s' % data)

for container in client.containers.list(all=True):
	if container.name not in ignored:
		container.remove()
