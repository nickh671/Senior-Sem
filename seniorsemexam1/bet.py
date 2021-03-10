#class to hold a bet
#each bet has a monetary amount and criteria for the bet attached to it
class Bet:
    def __init__(self, amount, criteria, betType):
        self.amount = amount
        self.criteria = criteria
        self.betType = betType