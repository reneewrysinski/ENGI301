# PocketTetris

## PocketBeagle Setup
1. Wire up components as described in Hackster post.
2. Connect PocketBeagle to the internet.
3. Configure PocketBeagle to run Python by running the following commands: 
`sudo apt-get update`
`sudo apt-get install build-essential python-dev python setuptools python-smbus -y`
`sudo apt-get install python-pip python3-pip -y`
4. Install Adafruit BBIO by running `sudo pip3 install --upgrade Adafruit_BBIO`

## Software Installation
1. Clone the `tetris` folder of this repo to your PocketBeagle.
2. Run `tetris.py` by navigating to the `tetris` directory on your PocketBeagle and running the `python3 tetris.py`