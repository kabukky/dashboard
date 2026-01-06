from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1200, 1600))
display.start()

driver = webdriver.Firefox()
driver.get("http://nas:2356/dashboard/v2/calendar/")