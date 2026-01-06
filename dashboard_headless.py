import requests
from time import sleep
from io import BytesIO
from inky.auto import auto
from PIL import Image
from PIL import ImageChops

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

# Headless browser for image rendering
print("Creating headless browser")
service = Service(executable_path="/usr/bin/geckodriver")
options = FirefoxOptions()
options.add_argument("--headless")
# options.add_argument("-width=1200")
# options.add_argument("-height=1600")
driver = webdriver.Firefox(service=service, options=options)

# Create inky impression display handle
print("Creating inky impression handle")
last_image = None
inky = auto()

try:
    while True:
        try:
            # Browser screenshot
            print("Getting browser screenshot")
            driver.set_window_size(1200, 1686)
            driver.get("http://nas:2356/dashboard/v2/calendar/")
            sleep(3)
            screenshot = driver.get_screenshot_as_png()
            image = Image.open(BytesIO(screenshot))

            show_image = True
            
            if last_image is not None:
                # Compare images if update neccessary
                print("Comparing images")
                diff = ImageChops.difference(last_image, image)
                if diff.getbbox():
                    show_image = True
                else:
                    show_image = False

            if show_image:
                # Display image on inky impression
                print("Showing image on inky impression")
                # cropped_image = image.crop((0,0,1200,1600))
                rotated_image = image.rotate(90, expand=True)
                inky.set_image(rotated_image, saturation=0.7)
                inky.show()
                print("Updated inky image")
            else:
                print("No need to update inky image")

            # Keep last image
            last_image = image
        except Exception as e:
            print(e)

        # Wait until repeat
        print("Waiting for next iteration")
        sleep(60) # 1 minute
finally:
    print("Closing browser")
    driver.quit()
