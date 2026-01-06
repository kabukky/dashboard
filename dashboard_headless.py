from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

service = Service(executable_path="/usr/bin/geckodriver")
options = FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1200,1600")
driver = webdriver.Firefox(service=service, options=options)

driver.get("http://nas:2356/dashboard/v2/calendar/")
driver.save_screenshot("screenshot.png")
driver.quit()