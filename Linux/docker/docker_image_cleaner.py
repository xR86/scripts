"""docker image cleaner"""
import docker
import sys

client = docker.from_env()

# equivalent of: `docker images`
def list_images():
	print(client.images.list(all=True, filters={
		"dangling": True
	}))


if len(sys.argv) > 1:

	list_images()
	
	# --safe - using built-in prune method, 
	#          it will delete unused images only
	if sys.argv[1] == '--safe':
		dct = client.images.prune()
		print(dct)

		list_images()
else:
	print('No cleaning method chose')

# # simple txt file, each row is a container name
# with open('~/.imageignore', 'r') as f:
# 	data = f.read().split('\n')
# 	ignored = list(filter(None, data))
# 	print('data: %s' % data)

# for image in client.images.list(all=True):
# 	if image.name not in ignored:
# 		image.remove()
