"""Logging Utils

Mirror of https://github.com/xR86/faster-research/blob/master/modules-py/custom_logging.py, as of commit 4ebcf5e
Source repo/components will be published.
"""
import logging
import csv
from io import StringIO

from datetime import datetime as dt
from pathlib import Path

LEN_STR_TRESH = 50
LIMIT_SYMBOL = '[...]'

stringify_list = lambda x: [str(arg) for arg in x]
stringify_dict = lambda x: {key:(str(val)) for key,val in x.items()}
# Prevent possible long strings to be saved to logs (doesn't prevent long lists or dicts though)
shorten_items_list = lambda x: [arg[:LEN_STR_TRESH] + LIMIT_SYMBOL if len(arg) > LEN_STR_TRESH else arg for arg in x]
shorten_values_dict= lambda x: {key:(val[:LEN_STR_TRESH] + LIMIT_SYMBOL if len(val) > LEN_STR_TRESH else val) for key,val in x.items() }

# Escape eventual unicode characters, in case logging isn't configured properly
uescape_items_list = lambda x: [arg.encode('ascii', 'backslashreplace') for arg in x]
uescape_values_dict= lambda x: {key:val.encode('ascii', 'backslashreplace') for key,val in x.items()}


# TODO: BUG
# "20200625-093200","INFO","save_pages_text","[b'../data/raw/arxiv/mine-paper-example/1809.02104.pd[...]'"," b""fitz.Document('../data/raw/arxiv/mine-paper-exampl[...]""];{}","call"
# check uescaping

class CsvFormatter(logging.Formatter):
	def __init__(self):
		super().__init__()
		self.output = StringIO()
		self.writer = csv.writer(self.output, quoting=csv.QUOTE_ALL)

	def format(self, record):
		# , record.filename\
		# with microsecond - '%Y%m%d-%H%M%S.%f'
		row = [dt.now().strftime('%Y%m%d-%H%M%S'), record.levelname] + record.msg.split(',')
		self.writer.writerow(row)
		data = self.output.getvalue()
		self.output.truncate(0)
		self.output.seek(0)
		return data.strip()

# decorator
def logged(func):
	# from datetime import datetime as dt
	# from pathlib import Path

	def wrapper(*args, **kwargs):
		try:
			args_shortened   = shorten_items_list(stringify_list(args))
			kwargs_shortened = shorten_values_dict(stringify_dict(kwargs))

			args_shortened = uescape_items_list(args_shortened)
			kwargs_shortened = uescape_values_dict(kwargs_shortened)

			logging.info(
				"{0},{1};{2},call".format(func.__name__, args_shortened, kwargs_shortened)
			)
			# return func(*args, **kwargs)

			sta = dt.now()
			result = func(*args, **kwargs)
			end = dt.now()

			logging.info(
				"{0},{1},time".format(func.__name__, (end - sta).microseconds)
			)

			return result
		except Exception as e:
			logging.error("{0},{1},exception".format(func.__name__, e))

	# TODO: Bad practice ?
	# Needed this change for the main code in models_summarization.py:
	# `print(summarizer.__name__)`
	func_name = func.__name__
	wrapper.__name__ = func_name

	return wrapper

@logged
def test_func(val):
	print(val/2)

def inst_logging(module_path):
	logging.basicConfig(
		filename='%s__%s.log' % (
			dt.now().strftime('%Y%m%d-%H%M%S'),
			Path(module_path).stem
		),
		level=logging.DEBUG
	)
	logger = logging.getLogger(__name__)
	logging.root.handlers[0].setFormatter(CsvFormatter())
	# note: logging.error(e) won't work
	# note: but logging.error("{0}".format(e)) will work


if __name__ == '__main__':

	# Sanity Checks
	## Lambdas
	args = ('♞aaaaaaaaaaaaaa♞aaaa', 121)
	kwargs = {'t': '♞asdasd♞asdasdas'}

	args_shortened   = shorten_items_list( stringify_list(args)  )
	kwargs_shortened = shorten_values_dict(stringify_dict(kwargs))

	args_shortened = uescape_items_list(args_shortened)
	kwargs_shortened = uescape_values_dict(kwargs_shortened)

	print(args_shortened, kwargs_shortened)

	## Logging
	inst_logging(__file__)
	test_func(2)
