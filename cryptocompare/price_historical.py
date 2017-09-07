# price_historical.py

from .helper_functions import build_url, load_data, to_pandas
from .options import use_pandas as USE_PANDAS

def get_historical_minute_price():
	"""

	"""

	pass


def get_historical_hour_price():
	"""

	"""

	pass


def get_historical_day_price(fsym, tsym, e='CCCAGG', try_conversion=True,
							 aggregate=1, limit=30, to_TS=None, all_data=False):
	"""

	:param fsym:
	:param tsym:
	:param e:
	:param try_conversion:
	:param aggregate:
	:param limit:
	:param toTS:
	:return:
	"""

	url = build_url('histoday', fsym=fsym, tsym=tsym, e=e, tryConversion=try_conversion,
					aggregate=aggregate, limit=limit, to_TS=to_TS, allData=all_data)
	res = load_data(url)

	if USE_PANDAS:
		res = to_pandas(res['Data'], datetime_cols=('time',))

	return res

