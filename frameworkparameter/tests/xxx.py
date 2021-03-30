import json

def load_test_data(path):
	with open(path) as data_file :
		data=json.load(data_file)
		print(data)


load_test_data(r'F:\pytest\frameworkparameter\tests\test_data.json')