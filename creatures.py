from entity import Entity

class Creature(Entity):
    pass

class Goblin_Bushwooki(Creature):
    hp = 40 
    speed = 10
    attack = 20 
    defence = 20
    spdefence = 20
    spattack = 20

class Soldier(Creature):
    hp = 20
    speed = 20 
    attack = 20
    defence = 20
    spdefence = 20
    spattack = 20

