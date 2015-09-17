
class Move():
    entity = None
    accuracy = None

class Charge(Move):
    accuracy = 100
    damage = 5

    def do(self,target):
       # TODO self.applyBuffs()
       # TODO self.appltDebuffs()
       rolled = dice.roll(1,100)
       if self.accuracy >= rolled:
        target.hp -= self.damage


class WarCry(Move):
    pass

class Slash(Move):
    pass
