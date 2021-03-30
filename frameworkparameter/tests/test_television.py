from pytest import mark

@mark.skip
@mark.parametrize('tv_brand',[('samsung'),('sony'),('onida')])
def test_teleision_turns_on(tv_brand):
	print(f'{tv_brand} turns on as expected')

@mark.skip
def test_teleision_turns_on2(tv_brand):
	print(f'{tv_brand} turns on as expected')
'''
def test_teleision_turns_on3(test_data):
	print(f'{test_data} turns on as expected')

	'''

