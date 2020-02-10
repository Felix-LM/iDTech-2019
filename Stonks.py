# Imports

from random import randint


# Variables

coins = 100

# Game functions

def printInfo(s, m, c):
    print()
    print("New investment opportunity!")
    print("Odds of success: " + str(int(s * 100)) + "%")
    print("Mulitiplier: " + "x" + str(m))
    print("You have %s coins!" % c)

def getInput(c):
    investment = input("How many coins would you like to invest? ")
    while investment.isdigit() == False or int(investment) > c:
        investment = input("Try again! (Enter a number within your budget): ")
    return int(investment)

def decide(s, m, c, inv):
    if randint(1, 100) / 100 <= s:
        print("Venture succeeded! You have gained %s coins!" % (inv * m))
        c += (inv * m)
    else:
        print("The venture failed! You have lost %s coins!" % inv)
        c -= inv
    return(c)

def main(coins):
    success = randint(15, 85) / 100.0
    multiplier = randint(1, 6)

    printInfo(success, multiplier, coins)

    coins = decide(success, multiplier, coins, getInput(coins))
    return coins


# Main

print("Welcome to Stonks! Try to reach 2000 coins!")

while coins < 2000:
    coins = main(coins)
    if coins <= 0:
        coins = 0
            
        print("You're out of coins!")
        exit()

print("Good Job! You've reached 2000 coins!")