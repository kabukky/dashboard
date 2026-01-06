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

# Inkplate10 config
inkplate_endpoint = "http://dashboard-inkplate:80/upload"

try:
    while True:
        try:
            # Weather
            print("Getting weather browser screenshot")
            driver.set_window_size(1200, 911)
            driver.get("http://nas:2356/dashboard/v2/weather/")
            sleep(5)
            screenshot_weather = driver.get_screenshot_as_png()
            image_weather = Image.open(BytesIO(screenshot_weather))
            with BytesIO() as f:
                rgb_image = image_weather.convert('RGB')
                rgb_image.save(f, format='JPEG', quality=100)
                f.seek(0)
                # image_rgb = Image.open(f)
                # Upload to inkplate to display image
                payload = {}
                files = [
                    ('',('screenshot.jpg',f,'image/jpeg'))
                ]
                headers = {}
                print("Updating inkplate image")
                requests.request("POST", inkplate_endpoint, headers=headers, data=payload, files=files)

            # Calendar
            # Browser screenshot
            print("Getting calendar browser screenshot")
            driver.set_window_size(1200, 1686)
            driver.get("http://nas:2356/dashboard/v2/calendar/")
            sleep(5)
            screenshot_calendar = driver.get_screenshot_as_png()
            image_calendar = Image.open(BytesIO(screenshot_calendar))

            # Determine if new image should be shown
            show_image = True
            if last_image is not None:
                # Compare images if update neccessary
                diff = ImageChops.difference(last_image.convert("RGB"), image_calendar.convert("RGB"))
                if diff.getbbox():
                    show_image = True
                else:
                    show_image = False

            if show_image:
                # Display image on inky impression
                print("Showing image on inky impression")
                # cropped_image = image.crop((0,0,1200,1600))
                rotated_image = image_calendar.rotate(90, expand=True)
                inky.set_image(rotated_image, saturation=0.7)
                inky.show()
                # Keep last image
                last_image = image_calendar
                print("Updated inky image")
            else:
                print("No need to update inky image")
        except Exception as e:
            print(e)

        # Wait until repeat
        print("Waiting for next iteration")
        sleep(70) # In seconds
finally:
    print("Closing browser")
    driver.quit()
