## Elytra
storing and syncing data from real time sensors and precalculated simulations

## Psycharts
performance optimizations on displaying 10k data points

## Human behaviour simulations
top down vs bottom up approach for syncing user events and interactions


## LUX
real time simulations in the browser allow for much more flexibility in terms of user selections and interactions. Build the geometry from scratch and make it dynamic, different degree of resolution for the simulation. UI/UX challenges as well - display large amounts of data and in different ways - 2d, 3d ,summary, lists.

## CDP
making a real time connection with (rpc, sockets? Don’t even remember). Compressing geometry in a condensed format and sending data over tcp/udp (tcp for establishing the first connection and then udp). Making a pluggable system - so defining very clear boundaries between the engine and plugins which run simulations. 

## Solar envelopes
Geometry calculations using raytracing, concurrency in python for faster simulations. Geometry edge cases and calculation optimizations.