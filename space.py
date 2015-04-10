#!/usr/bin/python
# -*- coding: utf8 -*-

class __planets(object):
    def __init__(self):
        self.planets = []
    def append(self, planet):
        self.planets.append(planet)

__planets__ =  __planets()


class Vessel(object):
    def __init__(self, name, position, capacity):
        self.name = str(name)
        self.position = None
        for planet in __planets__.planets:
            if planet.position == position:
                self.position = planet.name
                break
        if not self.position:
            self.position = list(position)
        self.capacity = int(capacity)
        self.occupied = 0
    def report(self):
        if not self.occupied:
            _occupied = "Товаров нет"
        else:
            _occupied = "Груз: %dт" % self.occupied
        print "%s. Местоположение: %s. %s." % (self.name, self.position, _occupied)
    def getFreeSpace(self):
        return self.capacity - self.occupied
    def getOccupiedSpace(self):
        return self.occupied
    def flyTo(self, newPosition):
        if isinstance(newPosition, Planet):
            self.position = newPosition.name
        else:
            for planet in __planets__.planets:
                if planet.position == newPosition:
                    self.position = planet.name
                    return
            self.position = list(newPosition)


class Planet(object):
    def __init__(self, name, position, availableAmountOfCargo):
        self.name = str(name)
        self.position = list(position)
        self.availableAmountOfCargo = int(availableAmountOfCargo)
        __planets__.append(self)
    def report(self):
        if not self.availableAmountOfCargo:
            _occupied = "Товаров нет"
        else:
            _occupied = "Груз: %dт" % self.availableAmountOfCargo
        print "%s. Местоположение: %s. %s." % (self.name, self.position, _occupied)
    def getAvailableAmountOfCargo(self):
        return self.availableAmountOfCargo
    def loadCargoTo(self, vessel, cargoWeight):
        if vessel.position == self.name or vessel.position == self.position:
            if vessel.getFreeSpace() >= cargoWeight:
                if self.getAvailableAmountOfCargo() >= cargoWeight:
                    vessel.occupied += cargoWeight
                    self.availableAmountOfCargo -= cargoWeight
                else:
                    raise Exception("Not such available cargo at %s" % self.name)
            else:
                raise Exception("Not such free space at %s" % vessel.name)
        else:
            raise Exception("Vessel %s is not on the planet %s" % (vessel.name, self.name))
    def unloadCargoFrom(self, vessel, cargoWeight):
        if vessel.position == self.name or vessel.position == self.position:
            if vessel.getOccupiedSpace() >= cargoWeight:
                vessel.occupied -= cargoWeight
                self.availableAmountOfCargo += cargoWeight
            else:
                raise Exception("Not such available cargo at %s" % vessel.name)
        else:
            raise Exception("Vessel %s is not on the planet %s" % (vessel.name, self.name))
