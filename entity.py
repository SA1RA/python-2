"""Entity class (is alive has stats)"""
from stats import HasStats
from inventory import HasInventory
class Entity(HasStats,HasInventory):
    pass
