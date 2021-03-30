from pytest import mark

@mark.smoke
@mark.body
class BodyTests:

	@mark.ui
	def test_can_naviagte_to(self,chrome_browser):
		chrome_browser.get('https://en.wikipedia.org/wiki/Body')
		assert True
