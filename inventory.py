"""inventory"""

class HasInventory():
    items = []
    
    def carry_weight(self):
        weight = 0
        for item in items:
            weight += item.weight
        return weight
