from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# I suggest to include chromedriver in path variable
# Else chromedriver is included in directory use following code:
# ------------------------------------------------------
# chromedriver = r"your clone directory\chromedriver"
# driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome()

# Go to link ----- Enter your own url if you want to modify
driver.get("https://my.uic.edu/Shibboleth.sso/Login?target=https://my.uic.edu/uPortal/Login")

# wait for load
driver.implicitly_wait(10)

# Select radio button
radio = driver.find_elements_by_id("https://shibboleth.uic.edu/shibboleth")[0].click()
driver.find_element_by_name("Select").click()

driver.find_element_by_name("UserID").send_keys("your user name")
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("disable-on-click").click()

driver.implicitly_wait(10)
driver.find_element_by_id("Pluto_207_u29l1n40_801_app").click()
driver.implicitly_wait(5)

# switch to new tab
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_id("keyword_in_id").send_keys("123")

