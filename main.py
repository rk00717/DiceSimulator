from random import randint

class dice_simulator:
    def __init__(self):
        go_on = True
        while go_on:
            self.start()
            go_on = True if input("\n\nDo you want to roll it again?[Y/N]  :  ").lower() == "y" else False

    def roll_dice(self, limit):
        result = randint(1, limit)
        return result

    def start(self):
        dices={
            # id   : name, limit of dice
            "dice1":["(D4)  Tetrahedron", 4],
            "dice2":["(D6)  Cube", 6],
            "dice3":["(D8)  Octahedron", 8],
            "dice4":["(D10) Pentagonal Trapezohedron", 10],
            "dice5":["(D12) Dodecahedron", 12],
            "dice6":["(D20) Icoshedron", 20]
        }
        
        print("Available Dices")
        for i in range(1, len(dices)+1):
            print(f"{i}. {dices['dice'+str(i)][0]}")
        choice = dices["dice" + input("Select A Dice to Roll[1/6] : ")][1]
        print(f"Results\n\tDice 1:  {self.roll_dice(choice)}\n\tDice 2:  {self.roll_dice(choice)}")
    
if __name__ == "__main__":
    dice_simulator()