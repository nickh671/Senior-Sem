import random
from bet import Bet

#a collection of valid inputs for each type of bet
#used for input validation
validBets = {
    'individual': range(0,37),
    'red': "red",
    'black': "black",
    'even': "even",
    'odd': "odd",
    'oneToEighteen': range(1,19),
    'nineteenToThirtySix': range(19, 37),
    'column': range(1,4),
    'dozen': range(1,4)
}

#dictionary to hold the different win rates of the roulette game
winRates = {
    'individual': 35,
    'red': 1,
    'black': 1,
    'even': 1,
    'odd': 1,
    'oneToEighteen': 1,
    'nineteenToThirtySix': 1,
    'column': 2,
    'dozen': 2
}

#variable to keep track of the users winnings/losings
balance = 0

#function to display the outcome of each individual bet
def displayOutcome(win, amount):
    if win == True:
        print(f'Congrats, you won ${amount}\n')
    else:
        print(f'Sorry, you lost ${amount}\n')

#function used to display the current balance of the user
def displayBalance():
    global balance
    print(f'Current balance is: ${balance}\n')

#function used for the individual bet
def individualBet():
    global balance
    #get our current bet
    currentBet = getBet('individual')
    #get the outcome of the wheel spin
    spinOutcome = spinWheel()

    #it outcome matches our bets criteria, user wins, else, loss
    if currentBet.criteria == spinOutcome:
        balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
        displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
    else:
        balance -= currentBet.amount
        displayOutcome(False, currentBet.amount)

#function used for the red/black bet
def redBlackBet(isRed):
    global balance
    #tuples to hold which numbers are black and which are red
    redNumbers = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
    blackNumbers = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)

    #saving out outcome from spinning the wheel even though not necessary
    spinOutcome = spinWheel()

    #if red is bet
    if isRed:
        #get current bet criteria
        currentBet = getBet('red')
        #if spin outcome is inside of the red tuple, win, else a loss
        if spinOutcome in redNumbers:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if black is bet
    else:
        #get current bet criteria
        currentBet = getBet('black')
        #if output is in the black tuple, win, else a loss
        if spinOutcome in blackNumbers:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)


#function used for the even/odd bett
def evenOddBet(isEven):
    global balance
    #saving our spin outcome
    spinOutcome = spinWheel()
    #if even bet
    if isEven:
        currentBet = getBet('even')
        #if spin output is an even number, win, else loss
        if spinOutcome in range(2, 37, 2):
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if odd bet
    else:
        currentBet = getBet('odd')
        #if spin output is an odd number, win, else loss
        if spinOutcome in range(1, 36, 2):
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    

#function for 1-18 bet
def oneToEighteenBet():
    global balance
    currentBet = getBet('oneToEighteen')
    spinOutcome = spinWheel()
    #if spin outcome is in 1-18, win, else loss
    if spinOutcome in range(1, 19):
        balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
        displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
    else:
        balance -= currentBet.amount
        displayOutcome(False, currentBet.amount)

#function for 19-36 bet
def nineteenToThirtySixBet():
    global balance
    currentBet = getBet('nineteenToThirtySix')
    spinOutcome = spinWheel()
    #if spin outcome is in 19-36, win, else loss
    if spinOutcome in range(19, 37):
        balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
        displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
    else:
        balance -= currentBet.amount
        displayOutcome(False, currentBet.amount)

#functino for column bet
def columnBet():
    global balance
    #lists to hold which cols have which values
    firstCol = range(1,35,3)
    secondCol = range(2, 36, 3)
    thirdCol = range(3,37,3)
    currentBet = getBet('column')
    spinOutcome = spinWheel()

    #if column 1
    if currentBet.criteria == 1:
        #if outcome is in col 1 list, win, else loss
        if spinOutcome in firstCol:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if column 2
    elif currentBet.criteria == 2:
        #if outcome is in col 2 list, win, else loss
        if spinOutcome in secondCol:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if column 3
    else:
        #if outcome is in col 3 list, win, else loss
        if spinOutcome in thirdCol:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)


def dozenBet():
    global balance
    #3 lists to hold values for each dozen
    firstDozen = range(1,13)
    secondDozen = range(13,25)
    thirdDozen = range(25,37)
    currentBet = getBet('dozen')
    spinOutcome = spinWheel()

    #if dozen 1
    if currentBet.criteria == 1:
        #if spin output is in dozen 1, win, else loss
        if spinOutcome in firstDozen:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if dozen 2
    elif currentBet.criteria == 2:
        #if spin output is in dozen 2, win, else loss
        if spinOutcome in secondDozen:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)
    #if dozen 3
    else:
        #if spin output is in dozen 3, win, else loss
        if spinOutcome in thirdDozen:
            balance += currentBet.amount + (currentBet.amount * winRates[currentBet.betType])
            displayOutcome(True, currentBet.amount * winRates[currentBet.betType])
        else:
            balance -= currentBet.amount
            displayOutcome(False, currentBet.amount)



#function to take input for how much a user will be betting and the criteria of their bet
def getBet(betType):
    #bet type will tell us what type of bet the user wants to make
    #this lets us properly ask the user the criteria they would like to be on and validate that input

    #check if betType only allows for one option (even, odd, red, black)
    if validBets[betType] in ["even", "odd", "red", "black"] or betType in ["oneToEighteen", "nineteenToThirtySix"]:
        moneyAmount = float(input('How much money would you like to bet?: '))

        #cannot bet less than 0
        while moneyAmount <= 0:
            print('You cannot bet less than $0.')
            moneyAmount = float(input('How much money would you like to bet?: '))

        return Bet(moneyAmount, validBets[betType], betType)
    else:
        betString = 'What would you like to place a bet on? '
        #determine the type of bet we are dealing with
        options = validBets[betType]

        #using our options from the global dictionary, build the string that asks the user for input
        #this way, the user can see their options
        betString += '(' + ",".join([str(i) for i in options]) + '): '

        #asking the user for their bet of choice
        betCriteria = int(input(betString))

        #if they enter an invalid bet, they are asked again
        while betCriteria not in validBets[betType]:
            print('Please enter a valid option.')
            betCriteria = int(input(betString))
        
        #asked for a monetary amount for their bet
        moneyAmount = float(input('How much money would you like to bet?: '))

        #users cannot bet less than 0
        while moneyAmount <= 0:
            print('You cannot bet less than $0.')
            moneyAmount = float(input('How much money would you like to bet?: '))

        return Bet(moneyAmount, betCriteria, betType)



#returns a number between 0 and 36
def spinWheel():
    return random.randint(0, 36)

#function to print the menu options
def printMenuOptions():
    print('1. Bet on an individual number')
    print('2. Bet on red')
    print('3. Bet on black')
    print('4. Bet on even')
    print('5. Bet on odd')
    print('6. Bet on 1-18')
    print('7. Bet on 19-36')
    print('8. Bet on a column (1-3)')
    print('9. Bet on a dozen (1-3)')
    print('10. Display Balance\n')

#function used to route the menu choice from user to the proper function
#choice is the users input
def routeChoice(choice):
    if choice == 1:
        individualBet()
    elif choice == 2:
        #pass true if red bed
        redBlackBet(True)
    elif choice == 3:
        #pass false if black bet
        redBlackBet(False)
    elif choice == 4:
        #pass true if even bet
        evenOddBet(True)
    elif choice == 5:
        #pass true if false bet
        evenOddBet(False)
    elif choice == 6:
        oneToEighteenBet()
    elif choice == 7:
        nineteenToThirtySixBet()
    elif choice == 8:
        columnBet()
    elif choice == 9:
        dozenBet()
    elif choice == 10:
        displayBalance()

#function used to take input from user and display menu
#central function
def Menu():
    print('CS453 Roulette Game')
    print('-'*25)

    #printing initial menu and taking input
    printMenuOptions()
    choice = int(input('Enter your choice (0 to quit): '))

    #if choice is to quit, return
    if choice == 0:
        return
    #if valid choice, pass to route function
    elif choice in range(1,11):
        routeChoice(choice)
    #else loop until valid input is found
    else:
        print()
        print('Please enter a valid option (0-10).\n')
        while choice != 0:
            printMenuOptions()
            choice = int(input('Enter your choice (0 to quit): '))
            print()

    #once initial input is given, keep looping until user enters a 0
    while choice != 0:
        printMenuOptions()
        choice = int(input('Enter your choice (0 to quit): '))
        #if user enters a value outside of the allowed options (1-10), give error message and repeat
        if choice in range(1,11):
            print()
            routeChoice(choice)
        else:
            print()
            print('Please enter a valid option (0-10).\n')

#calling the Menu function on start of the python file
if __name__ == '__main__':
    Menu()
