from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
# while True:
browser=webdriver.Firefox();
browser.get("http://web003.com/Users/Login")
# # ActionChains(browser).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
# browser.execute_script('''window.open("http://bings.com","_blank");''')
# windows = browser.window_handles
# browser.switch_to.window(windows[0])
# time.sleep(1)
# browser.switch_to.window(windows[1])


actions = ActionChains(browser)
actions.send_keys('admin')
actions.send_keys(Keys.TAB);
actions.send_keys('admin')
actions.send_keys(Keys.ENTER);
actions.perform()
browser.get("http://web003.com/Message")
buttons=browser.find_elements_by_class_name("btn")
# for button in buttons:
buttons[0].send_keys(Keys.CONTROL+Keys.RETURN)
windows = browser.window_handles
browser.switch_to.window(windows[1])

browser.implicitly_wait(30)
browser.maximize_window()
time.sleep(5)
# browser.quit()
	# pa	ss
