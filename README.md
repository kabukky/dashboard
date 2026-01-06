# Headless browser rendering on Raspberry Pi
- sudo apt install firefox
- sudo apt install xvfb
- pip install pyvirtualdisplay selenium
- wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux-aarch64.tar.gz
- tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
- chmod +x geckodriver
- sudo cp geckodriver /usr/bin/

# Service on Raspberry Pi
- cd /lib/systemd/system/
- sudo nano dashboard.service
- Insert:

[Unit]
Description=Job that runs the dashboard daemon

[Service]
ExecStart=/home/kabukky/dashboard/run.sh
User=kabukky

[Install]
WantedBy=multi-user.target

- sudo systemctl enable dashboard
- sudo service dashboard start
- Show logs using:
    - journalctl -u dashboard