from unsplash_python.unsplash import Unsplash
import time
import urllib
import os, random
import ctypes
import datetime
import shutil
def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False


flag = internet_on()

if (flag):
	unsplash = Unsplash({

		'application_id':'8ca7c148002e3ced1fb61965ce004da6f645c7879f6db940d00c022a0c7e8a92',
		'secret':'045560a1fabe3a944699eba795db0e9561ef0672628bee4c93c551cdb8242277',
		'callback_url':'urn:ietf:wg:oauth:2.0:oob'
	})

	photos = unsplash.photos().get_random_photo(query="space")

	photourl = photos[0]['urls']['full']

	#print(photourl)
	ts = time.time()
	locationurl = "G:/Unsplash/IMG_"+str(ts)
	locationurlnew = locationurl.replace(".","")
	locationurlfinal = locationurlnew+".jpg"
	#print(locationurlfinal)
	urllib.request.urlretrieve(photourl, locationurlfinal)

	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, locationurlfinal , SPIF_UPDATEINIFILE)

else:
	#print("No internet")
	randpic = random.choice(os.listdir("G:/Unsplash"))
	finalrandpic = "G:/Unsplash/"+randpic
	SPI_SETDESKWALLPAPER = 20
	SPIF_UPDATEINIFILE = 1
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, finalrandpic, SPIF_UPDATEINIFILE)
