"""Entity class (is alive has stats)
"""

from inventory import Inventory
from entity import Entity

"""Classes

assassin
sneaking highdamage _____

rogue
speed mediumdamage climbing


archer
range _____ lowdamage

ranger
speed climbing lowdamage


knight
slow defence mediumdamage

samuri
speed highdamage


mage
wizard
"""

class HasStats():
    abilities = []
    hp = 20
    xp = 0
    defence = 0
    attack = None
    speed = 0
    
