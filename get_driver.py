"""
Use this script to download the chrome driver for your machine
if it doesn't exist

NOTE : This only downloads the chrome driver, so firefox or any other browsers are not yet
available for auto download by this script

"""

import os
import sys
import wget
import zipfile

# FOR WINDOWS (PREFERRED PATH)
CHROMEPATHW = 'C:\\webdrivers\\'


# formats the chromedriver download link to the suitable os
def get_download(os):
    return f"https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_{os}.zip"


# gets the OS
def get_platform():
    platforms = {
        'linux1': 'linux64',
        'linux2': 'linux64',
        'darwin': 'mac64',
        'win32': 'win32'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


# checks for driver
# if it doesn't exist downloads it
# respective to the os in the current dir inside /driver/chromedriver.exe
def check(wdriver=CHROMEPATHW):
    if os.path.exists(wdriver):
        return wdriver+"chromedriver"
    if not os.path.exists("driver"):
        os.mkdir("driver")
        filename = wget.download(url=get_download(get_platform()), out="driver/chromedriver.zip")
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall("driver/")

        os.remove(filename)
        return filename

    return None


if __name__ == "__main__":
    res = check()
    print(res)
