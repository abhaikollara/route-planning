from graph import DirectedGraph, Node
from lib import Location, haversine_distance

start_location = Location(75.40322081327923, 13.222724042514256)
end_location = Location(74.77418178783742, 13.113723901464716)


print(haversine_distance(start_location, end_location))