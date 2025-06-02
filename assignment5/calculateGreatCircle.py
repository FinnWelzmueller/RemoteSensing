"""
This script calculates the Great-Circle distance in km from two coordinates
"""
import math
import numpy as np
lat1 = [72, 41, 58]
lon1 = [129, 0, 15]
lat2 = [72, 36, 7]
lon2 = [129, 23, 13]

R = 6378

def load_angle(inp):
    return (inp[0] + inp[1] / 60 + inp[2] / 3600)* math.pi/180


lam1 = load_angle(lat1)
lam2 = load_angle(lat2)
phi1 = load_angle(lon1)
phi2 = load_angle(lon2)

d = R * math.acos(math.cos(lam1)*math.cos(lam2)*math.cos(phi1 - phi2) + math.sin(lam1)*math.sin(lam2))

print("Coordinate Set 1: "+str(lam1)+" radians, "+str(phi1)+" radians.")
print("Coordinate Set 2: "+str(lam2)+" radians, "+str(phi2)+" radians.")
print("Great-Circle Distance: "+str(np.around(d,3))+" km.")