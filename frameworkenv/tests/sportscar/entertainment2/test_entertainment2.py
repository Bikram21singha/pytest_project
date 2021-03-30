from pytest import mark

@mark.entertainment2
class BodyTests:
	def test_entertainment_system_functions_as_expected(self):
		assert True

	def test_bumper(self):
		assert True

	@mark.door
	def test_winshield(self):
		assert True