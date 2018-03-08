'''
# IDEAS.md
---
+ latest_image_size -> use it for a chrome plugin to display 
statistics on docker hub alongside the original data


---
https://stackoverflow.com/questions/2513479/redirect-prints-to-log-file

'''

'''
API route examples:

https://docs.docker.com/registry/spec/api/
https://stackoverflow.com/questions/37203102/pagination-for-search-dockerhub-api


https://hub.docker.com/v2/repositories/
https://hub.docker.com/v2/repositories/ghost/ ???

https://hub.docker.com/v2/repositories/library/ghost/

https://hub.docker.com/r/library/ghost/tags/
https://hub.docker.com/v2/repositories/library/ghost/tags/?page_size=100
https://hub.docker.com/v2/repositories/library/ghost/tags/latest/
'''
import json
import math
from urllib.request import urlopen

# PRIMITIVES
def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

def urlsave(entry_query):
	# print('Saving %s' % entry_query)
	stream = urlopen(entry_query)

	response = ''
	if stream.getcode() == 200:
		response = json.loads(stream.read().decode('utf-8'))

	stream.close()
	# print(stream.closed)
	return response

def pretty_print_json(json_obj):
	return json.dumps(json_obj, indent=4, sort_keys=True)

# Advanced functions
def paginate_response(entry_query):
	final_response = []
	
	next_page = entry_query
	count = urlsave(api_query)['count']
	running_count = 0

	while next_page:
		print('Fetching: %s/%s results' % (running_count, count))

		response = urlsave(next_page)
		final_response.extend(response['results'])

		running_count += len(response['results'])
		next_page = response['next']

	print('pagination exhausted')
	return final_response

def test_paginate_response():
	api_query = 'https://hub.docker.com/v2/repositories/library/ghost/tags/?page_size=1000'
	final_response = paginate_response(api_query)

	print(urlsave(api_query)['count'])
	print(len(final_response))
	# print(final_response)

# https://github.com/adambullmer/sublime_docblockr_python
# https://github.com/adambullmer/sublime_docblockr_python/blob/master/commands.py
# https://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-and-what-are-raw-string-literals
def latest_image_size(repo_name):	
	r"""Displays image size for given repo for the 'latest' tag
	
	Image size will be given by default for amd64 architecture 
	(considered 'full_size in the API')
	
	Arguments:
		repo_name {String} -- provides 'user/repo' for the API
			(for root repos, user will be 'library')
	
	Examples:
		>>> latest_image_size('library/ghost')
		'202.68 MB'

	Returns:
		{String} -- string with size and unit type
	"""
	response = urlsave(
		'https://hub.docker.com/v2/repositories/' +
		repo_name +
		'/tags/latest/')

	return convert_size(response['full_size'])


print(latest_image_size('library/ghost'))
