__author__ = "Alberto Andrade"
__email__ = "araneto.ctba@gmail.com"

# import libs
# geocoder: https://geocoder.readthedocs.io/
import geocoder
import time
import pandas as pd

# init dicts
coordLat = []
coordLong = []
adresses = []

# Loop over the csv file
# 'geoDailyLimit' is the daily query limit of the google api
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

# construct columns of dataframe
data = {'Adress': adresses,
        'Latitude': coordLat,
        'Longitude': coordLong}
# populate and saving dataframe to csv file
df = pd.DataFrame(data=data, index=adresses, columns=['Adress', 'Latitude', 'Longitude'])
df.to_csv('output.csv', sep='|')

