import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

service = Service(executable_path="/usr/bin/geckodriver")
options = FirefoxOptions()
options.add_argument("--headless")
# options.add_argument("-width=1200")
# options.add_argument("-height=1600")
driver = webdriver.Firefox(service=service, options=options)

driver.set_window_size(1200, 1600)
driver.get("http://nas:2356/dashboard/v2/calendar/")
time.sleep(3)
driver.save_screenshot("screenshot.png")
driver.quit()