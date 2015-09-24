""" pokemon class/interface"""

class Pokemon():
    level = 1
    xp = 0
    height = 0
    weight = 0
    speed = 0
    hp = 0
    attack = 0
    spattack = 0
    defence = 0
    spdefence = 0
    type1 = ""
    type2 = ""
    usable_moves = []
    moves = []

    def choose_move(self,move):
        if move in usable_moves:
            self.move = move

    def attack(self,target):
        """resolve attack"""
        # TODO apply stats


