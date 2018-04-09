import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_dir = os.path.join(os.path.dirname(__file__), 'data')

#factor = 1.05

def load_scenario(scen=4,solar=50,wind=1489,rooftop=1070):
	#loads a scenario (each scenario is a different day)
	#specify installed solar/wind installed capacity using kwargs `wind`, `solar, and PV
	df = pd.read_csv("{0}/scenario_{1}.csv".format(data_dir,scen),parse_dates=['SETTLEMENTDATE'])
	df.WIND = df.WIND * wind
	df.SOLAR = df.SOLAR * solar
	df.ROOFTOP = df.ROOFTOP * rooftop
	return df

def scale_demand_by(df, factor=1.05):
	df.TOTALDEMAND *= factor
	return df
	