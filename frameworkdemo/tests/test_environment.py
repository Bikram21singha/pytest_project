from pytest import mark


def test_environment_is_qa(app_config):
	#assert env=='qa'
	base_url=app_config.base_url
	port=app_config.app_port
	assert base_url=='https://myqa-env.com'
	assert port ==80

@mark.skip(reason="not a qa environment")
def test_environment_is_dev(app_config):
	#assert env=='dev'
	base_url=app_config.base_url
	port=app_config.app_port
	assert base_url=='https://mydev-env.com'
	assert port ==8080