# Inkplate 10 on Raspberry Pi
- Install ardiuno-cli
- arduino-cli config init
- arduino-cli config add board_manager.additional_urls https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
- arduino-cli update
- arduino-cli core install Inkplate_Boards:esp32
- arduino-cli lib install InkplateLibrary
- arduino-cli board search Inkplate
- arduino-cli compile -b Inkplate_Boards:esp32:Inkplate10V2
- arduino-cli board list
- arduino-cli upload -b Inkplate_Boards:esp32:Inkplate10V2 -p /dev/ttyS0

# Headless browser rendering on Raspberry Pi
- sudo pip install pyvirtualdisplay selenium