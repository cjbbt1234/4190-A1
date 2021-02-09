class Node:

    def __init__(self,r,c):
        self.row=r
        self.col=c
        # status: 0-empty 1-star 2-temporary flag 3-permanent flag
        self.status=0
        self.neig=[]
    def addNeighbor(self,n):
        self.neig.append(n)
    def changeToEmpty(self):
        self.status=0
    def changeToStar(self):
        self.status=1
    def changeToTflag(self):
        self.status=2
    def changeToPflag(self):
        self.status=3

