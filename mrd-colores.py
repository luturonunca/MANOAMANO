# -*- coding: ISO-8859-1 -*-
import shapefile
import numpy as np
import matplotlib 
#matplotlib.use('ps')
#import matplotlib.use as use
#use('ps')
from matplotlib import rc
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
col=[]


file=open(sys.argv[1])
for line in file:
  row = line.split(',')
  if row[0][0]=='#':
    continue
  if row[1]=='':
    continue
  alt= float(row[3])
  if alt>4300:
    col.append('#D358F7')
    continue
  elif alt>3000:
    col.append('#AC58FA') 
    continue
  elif alt>2200:
    col.append('#8258FA')
    continue
  elif alt>1700:
    col.append('#642EFE')
    continue
  elif alt>800:
    col.append('#298A08')
    continue
  elif alt>0:
    col.append('#3ADF00')
    continue
#################################################################
################# Puntos de referencias##########################
#################################################################
########### dibuja puntos en las poblacones importantes##########
#################################################################

#parametros
lat_ciu = [8.59742,8.618826,8.252547,8.747436]
lon_ciu = [-71.144328,-71.648842,-71.829042,-70.920552]
ciudades = ['Merida','El Vigia', 'Bailadores', 'Mucuchies'] 
x,y= m_mrd(lon,lat)
x1,y1 = m_mrd(lon_ciu,lat_ciu)
#aqui se dibuja los circulos

m_mrd.plot(x1,y1,'ko',markersize=15)

rc('text',usetex=True)
rc('text.latex', preamble='\usepackage{color}')

#aqui el nombre

plt.text(x1[0]-7500,y1[0]-9000,ciudades[0],color='#173B0B',fontweight='bold')
plt.text(x1[1]-9000,y1[1]-9000,ciudades[1],color='#173B0B',fontweight='bold')
plt.text(x1[2]-13000,y1[2]-9000,ciudades[2],color='#173B0B',fontweight='bold')
plt.text(x1[3]+5000,y1[3]-5000,ciudades[3],color='#173B0B',fontweight='bold')



#############################################################################
#############################################################################

#ahora dibuja los puntos, al final para que queden arriba de todo

for i in range(len(x)):
  m_mrd.plot(x[i],y[i],'o',markersize=10,markerfacecolor=col[i])



plt.show()
