# -*- coding: ISO-8859-1 -*-
import shapefile
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sys
# Coordinates (from Wikipedia) and shift
MRD = [  -71.144393, 8.597356]
shift = [0, 2]
proj = 'tmerc'
# Colours
cMRD = '#006600' # Green tone

# 70 km by 70 km, Transverse Mercator, resolution does not
# matter, as we use other data for the borders
width = 170000
height = 200000
#dshift = [-.133, -.05]
dshift = [-0.14,- 0.15]

fig2 = plt.figure(figsize=(8,8))

# Create basemaps for Mexico and Switzerland
m_mrd = Basemap(width=width, height=height,resolution='h', projection=proj,
            lon_0=MRD[0]+dshift[0], lat_0=MRD[1]+dshift[1])

m_mrd.drawcoastlines(color=cMRD, linewidth=1.8)
m_mrd.drawcountries(color=cMRD, linewidth=1.8)
# Draw the district of Aargau
VEN_adm1 = shapefile.Reader('data/basemap/VEN_adm1')
#iag = [i for i, s in enumerate(VEN_adm1.records()) if 'Barinas' in s][0]
#print type(iag)  
iag=13
aglonlat = np.array(VEN_adm1.shapes()[iag].points)
m_mrd.plot(aglonlat[:, 0], aglonlat[:, 1], '-', c=cMRD, lw=2)
agx, agy = m_mrd(aglonlat[:, 0], aglonlat[:, 1])
plt.fill(agx, agy, cMRD, ec='none', alpha=.4)




lat = []
lon = []

file=open(sys.argv[1])
for line in file:
  row = line.split(',')
  if row[0][0]=='#':
    continue
  if row[1]=='':
    continue
  lat.append(float(row[1]))
  lon.append(float(row[2]))


#lat = [8.571246,8.615729]
#lon = [-71.076297,-71.655986]
x,y = m_mrd(lon,lat)
m_mrd.plot(x,y,'wo',markersize=10,label='Productores mano a mano\nenero 2014')
lg = plt.legend(loc='lower left', fontsize=16, numpoints=1)
lg.get_frame().set_alpha(.8) # A little transparency


plt.show()
