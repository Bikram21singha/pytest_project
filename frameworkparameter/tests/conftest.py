from pytest import fixture
import json

@fixture(params=['samsung','sony','onida','hshsh'])
def tv_brand(request):
	driver=request.param
	yield(driver)
	#driver.quit()

def load_test_data(path):
	with open(path) as data_file :
		data=json.load(data_file)
		return data
'''
data_path=r'F:\pytest\frameworkparameter\tests\test_data.json'
@fixture(params=load_test_data(data_path))
def test_data(request):
	data=request.param
	return data
	'''
