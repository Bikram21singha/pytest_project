from selenium import webdriver
browser=webdriver.Chrome()


browser.get("https://techstepacademy.com/training-ground")
input_element=browser.find_element_by_css_selector('input[id="ipt2"]')