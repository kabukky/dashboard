import os
from time import sleep
from inky.auto import auto

# Create inky impression display handle
inky_display = auto()

while True:
    # Take website screenshot
    os.system("chromium-browser --headless --screenshot=current.png --window-size=1600,1200 --disable-gpu --full-page --no-sandbox --timeout=3000 --hide-scrollbars http://nas:2356/dashboard/")

    # Display image on inky impression
    img = Image.open("current.png")
    inky_display.set_image(img)
    inky_display.show()

    # Wait until repeat
    sleep(3*60) # 3 minutes
