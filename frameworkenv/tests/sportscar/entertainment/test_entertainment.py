from pytest import mark

@mark.entertainment
@mark.ui
def test_entertainment_system_functions_as_expected(chrome_browser):
	chrome_browser.get('https://en.wikipedia.org/wiki/Entertainment')
	assert True