#!/bin/python3
from pandas import read_csv
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.ar_model import ARResults
import numpy
import sys
import os.path
from os import path
import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.ar_model.AR', FutureWarning)


from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


if len(sys.argv) < 2:
	print("Select a country");

else:

	def difference(dataset):
		diff = list()
		for i in range(1, len(dataset)):
			value = dataset[i] - dataset[i - 1]
			diff.append(value)
		return numpy.array(diff)

	# load dataset
	series = read_csv('tmp/'+sys.argv[1].lower()+'.csv', header=0, index_col=0)
	X = difference(series.values)
	# fit model
	model = AR(X)
	model_fit = model.fit(maxlag=6, disp=False)
	# save model to file
	model_fit.save('data/'+sys.argv[1].lower()+'/ar_model.pkl')
	# save the differenced dataset
	numpy.save('data/'+sys.argv[1].lower()+'/ar_data.npy', X)
	# save the last ob
	numpy.save('data/'+sys.argv[1].lower()+'/ar_obs.npy', [series.values[-1]])

