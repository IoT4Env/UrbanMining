from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list_values(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))

class Statuses(ExtendedEnum):
    SHUT = 0
    OK = 1
    DANGER = 2

class Functionalities(ExtendedEnum):
    CONTROLLER = 0
    SEPARATOR = 1

class Settings(ExtendedEnum):
    AUTO = 0
    MANUAL = 1

class Directions(ExtendedEnum):
    FORWARD = 0
    BACKWARDS = 1

class Weights(ExtendedEnum):
    L = 0
    M = 1
    H = 2

class Materials(ExtendedEnum):
    STEEL = 0
    COPPER = 1
    GOLD = 3
    CLAY = 4
    STONE = 5

