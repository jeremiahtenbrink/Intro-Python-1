# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    lat: ''
    lon: ''

    def __init__(self, lat, lng):
        self.lat = lat
        self.lon = lng

    def __str__(self):
        return f"Lat: {self.lat}, Lon: {self.lon}"


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    name: ''

    def __init__(self, name, lat, lng):
        super().__init__(lat, lng)
        self.name = name

    def __str__(self):
        return super().__str__() + f" Name: {self.name}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    difficulty: ''
    size: ''

    def __init__(self, name, diff, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = diff
        self.size = size

    def __str__(self):
        return super().__str__() + f" Dif: {self.difficulty}, Size: {self.size}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
