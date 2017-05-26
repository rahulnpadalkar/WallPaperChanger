from unsplash_python.unsplash import Unsplash
import time
import urllib
import os, random
import ctypes
import datetime
import shutil
def internet_on():
    try:
	#pinging google servers to check for internet connectivity
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False


flag = internet_on()

if (flag):
	unsplash = Unsplash({

		'application_id':'YOUR_APP_ID_HERE',
		'secret':'YOUR_SECRET_CODE_HERE',
		'callback_url':'CALLBACK_URL_HERE'
	})

	photos = unsplash.photos().get_random_photo(query="space")

	photourl = photos[0]['urls']['full']

	#print(photourl)
	ts = time.time()
	locationurl = "PATH:/TO/IMAGE/IMG_"+str(ts)
	locationurlnew = locationurl.replace(".","")
	locationurlfinal = locationurlnew+".jpg"
	#print(locationurlfinal)
	urllib.request.urlretrieve(photourl, locationurlfinal)

	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, locationurlfinal , SPIF_UPDATEINIFILE)

else:
	#print("No internet")
	randpic = random.choice(os.listdir("PATH:/TO/IMAGE"))
	finalrandpic = "PATH:/TO/IMAGE"+randpic
	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, finalrandpic, SPIF_UPDATEINIFILE)
