'''
Run with:
make -f Makefile-flask
'''

#import tema as tm
#from . import tema as tm

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	name = 'Flask boilerplate app'
	return render_template('mdl_index.html', name=name)


# Route handlers
@app.route('/api/add', methods=['GET']) # works also without methods (default: GET)
def calculate_add_get_wrapper():
	return str('Add function, use POST.')


@app.route('/api/add', methods=['POST'])
def calculate_add_post_wrapper():
	print(request.get_json()) #force=True
	a = int(request.get_json()["a"])
	b = int(request.get_json()["b"])

	temp = a + b
	
	return str(temp)


@app.route('/result')
def smth_wrapper():
	return str('Not implemented')
