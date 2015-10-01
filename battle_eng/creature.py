""" pokemon class/interface"""

class Pokemon():
    uid = 0
    name = ""
    description = ""
    level = 1
    xp = 0
    happiness = 0
    height = 0
    weight = 0
    speed = 0
    total = 0
    hp = 0
    attack = 0
    evolves_at = 0
    species = ""
    catch_rate = 0
    growth_rate = 0
    spattack = 0
    defence = 0
    spdefence = 0
    type1 = ""
    type2 = ""
    usable_moves = []
    moves = []

    class Move():
        uid = 0
        name = ""
        description = ""
        category = ""
        learn_type = ""
        power = 0
        accuracy = 0
        pp = 0
        learned_at = ""

    class Ability():
        uid = 0
        name = ""
        decription = ""

    class Type():
        uid = 0
        name = ""
        description = ""

"""
class controller():
"""

    def attack(self,target):
        """resolve attack"""
        # TODO apply stats


