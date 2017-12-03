# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:36:11 2017

@author: ANASTASIS
"""

import json
import numpy as np


jsondata = json.load(open('Geofences.json'))

jsondata1 = jsondata['features'][0]['geometry']['coordinates']



p1 = jsondata1[0][0]
p2 = jsondata1[0][1]
p3 = jsondata1[0][2]
p4 = jsondata1[0][3]
p5 = jsondata1[0][4]

p1 = np.asarray(p1)
p2 = np.asarray(p2)
p3 = np.asarray(p3)
p4 = np.asarray(p4)
p5 = np.asarray(p5)


#import matplotlib.path as mplPath

polygon = np.array([p1,p2,p3,p4,p5])


#polygon
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

lats = np.array([p1[0],p2[0],p3[0],p4[0],p5[0]])
lons = np.array([p1[1],p2[1],p3[1],p4[1],p5[1]])

lons_lats_vect = np.column_stack((lons,lats))

polygon1 = Polygon(lons_lats_vect)
point = Point(x1,y1)
print(polygon1.contains(point))

#
#from shapely.geometry.polygon import LinearRing
#ring = LinearRing(lons_lats_vect)
#x, y = ring.xy
#
import matplotlib.pyplot as plt
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(x, y , color='#6699cc', alpha=0.7,linewidth=3)
#ax.set_title('man')
##ax.set_xlim([min(p1[0],p2[0],p3[0],p4[0],p5[0]),max(p1[0],p2[0],p3[0],p4[0],p5[0])])
##ax.set_ylim([min(p1[1],p2[1],p3[1],p4[1],p5[1]),max(p1[1],p2[1],p3[1],p4[1],p5[1])])
plt.scatter(p1[0],p1[1], color='red')
plt.scatter(p2[0],p1[1], color='red')
plt.scatter(p3[0],p1[1], color='red')
plt.scatter(p4[0],p1[1], color='red')
plt.scatter(p5[0],p1[1], color='red')
plt.show()






