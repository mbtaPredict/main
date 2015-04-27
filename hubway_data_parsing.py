from os import path
import csv

def load_trips(year):
	"""
	Input: Year in which you want to return stored Hubway data.
	Output: List of dictionaries, where each dict contains the
			data for one Hubway trip
	"""
	data = []
	file_path = path.relpath("HubwayData/%s_hubway_trips.csv") % year
	
	#loads data from csv as a list of dictionaries
	with open(file_path) as f:
		reader = csv.DictReader(f)
		for row in reader:
			data.append(row)

	return data

if __name__ == "__main__":
    print load_trips(2013)