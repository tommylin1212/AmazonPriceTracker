from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DestinationUrl = "http://amazon.com"


ChromeOptions = webdriver.ChromeOptions()
#ChromeOptions.add_argument("--headless")
ChromeDriverInstance = webdriver.Chrome(executable_path='PATH TO CHROMEDRIVER.EXE',
                                        chrome_options=ChromeOptions)
# driver.implicitly_wait(30)
ChromeDriverInstance.get(DestinationUrl)

SearchBar = ChromeDriverInstance.find_element_by_name("field-keywords")  # name of the search bar on amazon.com
SearchBar.clear()
SearchBar.send_keys("echo dot")  # easy to replace from csv list

SearchBar.send_keys(Keys.RETURN)
ChromeDriverInstance.close()
