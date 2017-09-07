# helper_functions.py

import json
import requests
import pandas as pd


def build_url(func, **kwargs):
	"""
	"""

	if func in ['coinlist', 'coinsnapshot']:
		url = "https://www.cryptocompare.com/api/data/{}?".format(func)
	else:
		url = "https://min-api.cryptocompare.com/data/{}?".format(func)
	
	# collect url parts in list
	url_parts = []

	for key, value in kwargs.items():
		if key == 'fsym':
			url_parts.append("fsym={}".format(value))
		elif key == 'fsyms':
			url_parts.append("fsyms={}".format(",".join(value)))
		elif key == 'tsym':
			url_parts.append("tsym={}".format(value))
		elif key == 'tsyms':
			url_parts.append("tsyms={}".format(",".join(value)))
		elif key == 'e' and value != 'all':
			url_parts.append("e={}".format(value))
		elif key == 'try_conversion' and not value:
			url_parts.append("tryConversion=false")
		elif key == 'markets' and value != 'all':
			url_parts.append("markets={}".format(",".join(value)))
		elif key == 'avgType' and value != 'HourVWAP':
			url_parts.append("avgType={}".format(value))
		elif key == 'UTCHourDiff' and value != 0:
			url_parts.append("UTCHourDiff={}".format(value))
		elif key == 'ts':
			url_parts.append("ts={}".format(value))
		elif key == 'aggregate' and value != 1:
			url_parts.append("aggregate={}".format(value))
		elif key == 'limit' and value != 1440:
			url_parts.append("limit={}".format(value))
		elif key == 'allData' and value:
			url_parts.append("allData=true")
		elif key == 'toTS':
			url_parts.append("toTS={}".format(value))

	# put url together
	url = url + "&".join(url_parts)
	print(url)
	return url


def to_pandas(data, datetime_cols=()):
	df = pd.DataFrame.from_records(data)
	for c in datetime_cols:
		df[c] = pd.to_datetime(df[c], unit='s')
	return df

def load_data(url):
	"""
	"""

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()

	return data