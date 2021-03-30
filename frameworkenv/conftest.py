from pytest import fixture

from selenium import webdriver

@fixture(scope='function')
def chrome_browser():
	browser=webdriver.Chrome(executable_path=r'C:\Users\bikra\.wdm\drivers\chromedriver\win32\88.0.4324.96\chromedriver.exe')
	return browser
