import random

class playerPicker:
    def __init__(self, people, playerNum):
        self.people = people
        self.playerCount = len(self.people)
        self.playerNum = playerNum
    
    def firstPlayer(self):
        self.playerNum = random.randint(0, self.playerCount-1)
        return self.playerNum

    def nextPlayer(self):
        if self.playerNum == (self.playerCount-1):
            self.playerNum = 0
        else:
            self.playerNum += 1
        return self.playerNum
        
        