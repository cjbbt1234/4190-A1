class Node:

    def __init__(self,r,c):
        self.row=r
        self.col=c
        # status: 0-empty 1-star 2-temporary flag 3-permanent flag
        self.status=0
