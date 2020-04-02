#!/bin/python3
import numpy
import sys
if len(sys.argv) < 2:
	print("Select a country");

else:
	# get real observation
	observation = 48
	# load the saved data
	data = numpy.load('../data/'+sys.argv[1]+'/ar_data.npy')
	last_ob = numpy.load('../data/'+sys.argv[1]+'/ar_obs.npy')
	# update and save differenced observation
	diffed = observation - last_ob[0]
	data = numpy.append(data, [diffed], axis=0)
	numpy.save('../data/'+sys.argv[1]+'/ar_data.npy', data)
	# update and save real observation
	last_ob[0] = observation
	numpy.save('../data/'+sys.argv[1]+'/ar_obs.npy', last_ob)
