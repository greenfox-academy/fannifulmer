'''Information on the elements

The Garden
is able to hold unlimited amount of flowers or trees
when watering it should only water those what needs water with equally divided amount amongst them
eg. watering with 40 and 4 of them need water then each gets watered with 10
The Flower
needs water if its current water amount is less then 5
when watering it the flower can only absorb the 75% of the water
eg. watering with 10 the flower's amount of water should only increase with 7.5
The Tree
needs water if its current water amount is less then 10
when watering it the tree can only absorb the 40% of the water
eg. watering with 10 the tree's amount of water should only increase with 4'''

class Garden():
    flowers = []
    trees = []
    
    def needs_water(self):
        plant_needs_water = 0
        
        for f in garden.flowers:
            if f[1] < 5:
                plants_needs_water += 1
        return plants_needs_water
        
        # for t in trees:
        #     if t[1] < 10:
        #         plants_needs_water += 1
        # return plants_needs_water
                
    def watering(self, water_amount):
        self.water_amount = water_amount
        water_for_one_plant = water_amount / self.needs_water()
        for flower in flowers:
            if flower[1] < 5:
                flower[1] += water_for_one_plant*0.75
            print("The", self.color, self.type, "needs water")
        
        
class Flower(Garden):
    def __init__(self, color, water_level):
        self.color = color
        self.water_level = water_level
        self.flowers.append([self.color, self.water_level])
        
class Tree(Garden):
    def __init__(self, color, water_level):
        self.color = color
        self.water_level = water_level
        
garden = Garden()
rose = Flower('red', 0)
garden.watering(40)
print(garden.flowers)
        

    
