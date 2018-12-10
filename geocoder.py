__author__ = "Alberto Andrade"
__email__ = "araneto.ctba@gmail.com"

import geocoder
import time
import pandas as pd

coordLat = []
coordLong = []
adresses = []

with open('adresses.csv') as x:
    geoDailyLimit = 2500
    for location in x:
        if geoDailyLimit > 0:
            g = geocoder.google(location)
            addr, lat, long = g.address, g.lat, g.lng
            adresses.append(addr)
            coordLat.append(lat)
            coordLong.append(long)
            geoDailyLimit -= 1
        else:
            pass
    x.close()

data = {'Adress': adresses,
        'Latitude': coordLat,
        'Longitude': coordLong}

df = pd.DataFrame(data=data, index=adresses, columns=['Adress', 'Latitude', 'Longitude'])
df.to_csv('output.csv', sep='|')

