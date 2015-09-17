"""Player Entity"""

from entity import Entity
class Player(Entity): 
    def __init__(self):
        self.hp = 100
        self.speed = 1
