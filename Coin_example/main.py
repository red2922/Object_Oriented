"""import random
class Coin:
    def __init__ (self):
        self.sideup = 'Heads'


    def toss (self):
        if random.radint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup (self):
        return self.get_sideup()

coin = Coin()

print(coin.get_sideup())

for i in range(10):
    coin.toss()
    print("Tossing the coin in round " + str(i+1) + coin.getsideup())
"""

"""
for y in range(2000):
        x = (float(9.8 * y))
        z = (float(10 * (y - 5)))
        if x == z and y > 0:
            print(y)
        """
for y in range(500):
    difference = 1
    x = float((0 * y) + (4.9 * (pow(y,2))))
    z = float((10 * y) + (5 * (pow(y - difference,2))))
    if int(x) < int(z) and y > 5:
        print(x)
        print(z)
        print(y)
        break











