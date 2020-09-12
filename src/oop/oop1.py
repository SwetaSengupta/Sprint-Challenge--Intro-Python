# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # base class for groundvehicle and flightvehicle
    pass

class FlightVehicle(Vehicle):
    # base class for airplane and starship
    pass
class Starship(FlightVehicle):
    pass

class GroundVehicle(Vehicle):
    # base class for car and motorcycle
    pass
class Airplane(FlightVehicle):
    pass
class Car(GroundVehicle):
    pass
class Motorcycle(GroundVehicle):
    pass
