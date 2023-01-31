# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# * plane flying in a straight line at a constant
#   altitude on an infinite flat earth
# * infinite hearing distance
# * observer at (0.0 , 0.0) = (location, altitude)
# t = time, seconds, t = 0.0 is the fly over moment
s = 343.0 # speed of sound, meters per second
# p = speed of the plane
h = 343.0 # fly over altitude, meters

# location of the plane relative to ground
# x location on earth of the plane with velocity p at time t
# negative values indicate approaching the fly over point and
# positive values flying away
def location(t, p):
    return p*t

# distance of the plane at from the observer
# "location" is distance along the ground and "h" is the altitude
def distance(location, h):
    return np.sqrt(location**2 + h**2)

# time to hear the plane from "distance" away
# i.e. time it takes for sound to reach the observer
def hearingDelay(distance, s):
    return distance/s

# make a list of t=time points (for the x-axis of the plots)
t = np.linspace(-2.0, 0.25, 3000) # list of values where to calculate

# plot location, distance, and time when heard
# (p=speed of the plane, h=altitude,
#   s=speed of sound, t=list of time points,
#   figures to plot onto [0]=locatio [1]=distance, [2]=time plane is heard
#   label to be used on the plot)
def plots(p, h, s, t, figures, label):
    loca = location(p, t) # locations at t
    dist = distance(loca, h) # distance at t
    hearAt = t + hearingDelay(dist, s) # when sound made at time t is heard
    plt.figure(figures[0])
    plt.plot(t, loca, label=label)
    plt.figure(figures[1])
    plt.plot(t, dist, label=label)
    plt.figure(figures[2])
    plt.plot(t, hearAt, label=label)
    # when is the first to be heard sound emitted and when is it heard
    tminheardIndex = np.argmin(hearAt)
    tminheard = t[tminheardIndex]
    heardAtmin = hearAt[tminheardIndex] # when is the first heard sound heard
    print("Earliest observation:", label, ", emitted: ", tminheard, ", heard: ", heardAtmin)
    plt.plot(tminheard, heardAtmin, 'r.') # red dot to when first heard

figures = [None, None, None] # initialize empty 3 element list of figures
figures[0] = plt.figure() # Location at time t
plt.title("Location of the plane relative to fly over point")
figures[1] = plt.figure() # Distance to observer a time t
plt.title("Distance of the plane from observer (accounts for altitude)")
figures[2] = plt.figure() # Sound made at time t is heard
plt.title("When is the sound made at time t heard\nRed dot = first observation")

# Here we go, put the numbers in and plot stuff
plots(0.5*s, h, s, t, figures, '0.5 Mach')
plots(1.0*s, h, s, t, figures, '1.0 Mach')
plots(2.0*s, h, s, t, figures, '2.0 Mach')
plots(4.0*s, h, s, t, figures, '4.0 Mach')

# some finalizing for the plots
for f in figures:
    plt.xlabel("time relative to fly over moment")
    plt.figure(f)
    plt.grid()
    plt.legend()

