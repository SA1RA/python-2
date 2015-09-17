"""Player Entity"""


from stats import HasStats
from inventory import HasInventory
import dice

class Player(HasStats,HasInventory): 
    
    def __init(self):
        self.hp = 100
        self.speed = dice.roll(2,6)
