#!/bin/python3
from statsmodels.tsa.ar_model import ARResults
import numpy
from pandas import read_csv
import sys
import os

if len(sys.argv) < 2:
	print("Select a country");

else:
	os.system("tac imports/"+sys.argv[1]+"/data.csv > /tmp/"+sys.argv[1]+".csv")
	series = read_csv("/tmp/"+sys.argv[1]+".csv", header=0, index_col=0)
	print(series.head(20))
	os.system("rm /tmp/"+sys.argv[1]+".csv")


	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('Prediction: %f' % yhat)
	prediction = '%f' % yhat


	os.system("cat imports/"+sys.argv[1]+"/data.csv > /tmp/"+sys.argv[1]+".csv")
	os.system("utils/addtemp.sh "+sys.argv[1]+" "+prediction)
	os.system("rm /tmp/"+sys.argv[1]+".csv")


	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('2nd Prediction: %f' % yhat)
	prediction = '%f' % yhat


	os.system("cat imports/"+sys.argv[1]+"/data.csv > /tmp/"+sys.argv[1]+".csv")
	os.system("utils/addtemp.sh "+sys.argv[1]+" "+prediction)
	os.system("rm /tmp/"+sys.argv[1]+".csv")


	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('3rd Prediction: %f' % yhat)
	prediction = '%f' % yhat



	os.system("cat imports/"+sys.argv[1]+"/data.csv > /tmp/"+sys.argv[1]+".csv")
	os.system("utils/addtemp.sh "+sys.argv[1]+" "+prediction)
	os.system("rm /tmp/"+sys.argv[1]+".csv")


	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('4th Prediction: %f' % yhat)
	prediction = '%f' % yhat

	os.system("cat imports/"+sys.argv[1]+"/data.csv > /tmp/"+sys.argv[1]+".csv")
	os.system("utils/addtemp.sh "+sys.argv[1]+" "+prediction)
	os.system("rm /tmp/"+sys.argv[1]+".csv")


	model = ARResults.load('data/'+sys.argv[1]+'/ar_model.pkl')
	data = numpy.load('data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('data/'+sys.argv[1]+'/ar_obs.npy')
	predictions = model.predict(start=len(data), end=len(data))
	yhat = predictions[0] + last_ob[0]
	print('5th Prediction: %f' % yhat)
	prediction = '%f' % yhat

	os.system("rm /tmp/"+sys.argv[1]+".csv &> /dev/null")
	os.system("./utils/reinitback.sh ireland")

	#	os.system("./init.py "+sys.argv[1])
