# Headless browser rendering on Raspberry Pi
- sudo apt install firefox
- sudo apt install xvfb
- pip install pyvirtualdisplay selenium
- wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux-aarch64.tar.gz
- tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
- chmod +x geckodriver
- sudo cp geckodriver /usr/bin/