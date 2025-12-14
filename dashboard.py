import requests
from time import sleep
from io import BytesIO
from inky.auto import auto
from PIL import Image
from PIL import ImageChops

# Create inky impression display handle
last_image = None
inky = auto()

while True:
    show_image = True

    # Take website screenshot
    response = requests.get("http://nas:5000/screenshot?width=1200&height=1687&url=http://nas:2356/dashboard/v2/")
    image = Image.open(BytesIO(response.content))

    if last_image is not None:
        # Compare images if update neccessary
        diff = ImageChops.difference(last_image, image)
        if diff.getbbox():
            show_image = True
        else:
            show_image = False

    if show_image:
        # Display image on inky impression
        cropped_image = image.crop((0,0,1200,1600))
        rotated_image = cropped_image.rotate(90, expand=True)
        inky.set_image(rotated_image, saturation=0.7)
        inky.show()
        print("Updated inky image")
    else:
        print("No need to update inky image")

    # Keep last image
    last_image = image

    # Wait until repeat
    sleep(1*60) # 4 minutes
