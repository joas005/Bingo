import random
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Defining -
myBingoCard = [
    [0, 0, 0],
    [0, 'BINGO', 0],
    [0, 0, 0]
]
rolledNumbers = []
numbersMarked = []
numberChecked = False

# Functions -
def printBingo():
    print()
    for linha in myBingoCard:
        print('| ', end='')
        for item in linha:
            print(f"{item:^5}", end=' | ')
        print('\n' + 25*'-')
    print()

def generateBingo():
    for linha in range(3):
        for item in range(3):
            if item == 1 and linha == 1:
                pass
            else:
                myBingoCard[linha][item] = random.randint(1, 90)

def rollNumber():
    rolledNumber = random.randint(1, 90)
    print(f'The number rolled this round was: ')
    print(34*'.')
    if rolledNumber not in rolledNumbers:
        print(f'\033[35m--{rolledNumber:^30}--\033[0m')
        rolledNumbers.append(rolledNumber)
    else:
        rolledNumber = random.randint(1, 90)
        print(f'\033[35m--{rolledNumber:^30}--\033[0m')
    print()
    time.sleep(2)
    checkNumber(rolledNumber)

def checkNumber(rolledNumber):
    printBingo()
    checked = input(
        f'Do you have the number \033[35m-{rolledNumber}-\033[0m on your card? ').strip().lower()
    if checked == '':
        verifyUserAwnser(rolledNumber)
    elif checked[0] in 'yis':
        verifyUserAwnser(rolledNumber)
    else:
        print('\nMore luck next time!')
        input('Enter continues...')
        os.system('cls' if os.name == 'nt' else 'clear')

def verifyUserAwnser(rolledNumber):
    numberChecked = False
    for row in myBingoCard:
        if rolledNumber in row:
            index = row.index(rolledNumber)
            row[index] = 'XX'
            numberChecked = True
            print(f"\n\033[32mCongrats!\nYou've marked the number {rolledNumber}!\033[0m")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
    if not numberChecked:
        print("\nDoesn't look like you have this number!")
        print('More luck next time!')
        input('Enter continues...')
        os.system('cls' if os.name == 'nt' else 'clear')

def exitProgram():
    print('\nThank you for playing!\n\nCome back anytime XD')
    time.sleep(2)
    exit()

def gameWon():
    print("\033[32mYou've won the game!\033[0m")
    input('Enter continues...')
    exit()

# Main -
print('\033[35m', 10*'-', 'My bingo!', 10*'-', '\033[0m\n')

start = input(
    "Type anything to start playing or 'q' to exit.\n > ").strip().lower()
if start == 'q':
    exitProgram()

os.system('cls' if os.name == 'nt' else 'clear')
generateBingo()
print('\nHere is your bingo card: ')
printBingo()
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("\033[32mNow let's start playing!\033[0m\n")
while True:
    for row in myBingoCard:
        for item in row:
            if str(item).isdigit():
                int(item)
                rollNumber()
            else:
                if item not in numbersMarked:
                    numbersMarked.append(item)
                    if len(numbersMarked) == 8:
                        gameWon()