from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
# while True:
driver=webdriver.Firefox();
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://web003.com/Users/Login")
actions = ActionChains(driver)
actions.send_keys('admin')
actions.send_keys(Keys.TAB);
actions.send_keys('admin')
actions.send_keys(Keys.ENTER);
actions.perform()
driver.get("http://web003.com/Message")
buttons=driver.find_elements_by_class_name("btn")
for i in range(len(buttons)):
	buttons[i].click()
	try:
		Alert(driver).accept()
		pass
	except Exception as e:
		pass
	finally:
		driver.back()
		buttons=driver.find_elements_by_class_name("btn")
		pass
driver.quit()
# pass
