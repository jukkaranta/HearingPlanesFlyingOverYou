# HearingPlanesFlyingOverYou

A quickie inspired by https://www.reddit.com/r/askscience/comments/10ow25s/if_two_planes_pass_above_me_at_the_exact_same/

When does the sound of an aeroplane flying over you reach you?

Code is commented but basic premise is that a plane flies over you at some altitude. When does the sound from that plane reach you? How does the speed of the plane affect the time when you hear it? Which plane do you hear first if they have different speeds but fly over at the same moment?

## Basics
Fix the flying altitude. Assume flat infinite earth over which the plane flies in a straight line at constant altitude. Ignore the third (side ways) dimension, i.e. just look at the situation from the side: plane flies in the direction of the horizontal axis and altitude is the vertical axis and observer listening to the noise is in the origin. Normalize the whole thing so that t=0.0 is the fly over moment. Check from wikipedia what the speed of sound is.

## Calculations and plots

Calculate the location of the plane relative to ground. This is just velocity * time. Negative times are negative locations of an approaching plane, at time zero location is zero, i.e. above you, positive times give positive locations after fly over.

1st plot: (time, location) horizontal axis is the normalized time, vertical axis location.

Calculate distance of the plane from you (the observer): Just the normal distance based on location (L) and altitude (h), distance = sqrt(L**2 + h**2).

2nd plot: (time, distance) horizontal axis again the normalized time, vertical axis distance of the plane

Caculate when a sound is heard: Calculate how long it takes for sound to reach you from a position of the plane. And adjust for the time when the sound was emitted: distance/speed of sound + time when the sound was emitted.

3rd plot: (time, time when heard) Horizontal axis same as previous plots, vertical axis is the time the sound is heard, i.e. point at coordinates (X, Y) means that sound made by the plane at time X is heard at time Y. For the list of time values, plot a red dot to the smallest "time when heard" value, i.e. the first observation.

## Notes

The sound the planes make when right above is heard at the same time (= altitude / speed of sound) after the fly over.

A subsonic Mach < 1.0 plane is heard an infinity away. The earlier it makes the sound the earlier that sound is heard. The "time when heard" function goes to -infinity as time goes to -infinity.

A sonic Mach = 1.0 plane is heard the moment it flies over but that sound comes from an infinity away. If altitude is zero we hear all sound before that time at the same time. The "time when heard" approaches 0 as time goes to -infinity in case of non-zero altitude; or is flat zero for all times <0 in case of zero altitude.

Supersonic Mach > 1.0 planes have a distinct minimum of the "time when heard"-function, i.e. time when they are first heard (that's when the shock wave cone reaches the observer). You hear slower planes first. After hearing that first sound (sonic boom) you actually hear two sounds: a sound the plane made during approach and a sound it made when going away.
