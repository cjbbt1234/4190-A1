from itertools import combinations
import Read
from Star import  StarList
import Drawfield
import timeit

limit=2

# fileName='10x10 puzzle-1.txt'
# fileName='14x14 p1.txt'
# fileName='8x8 p1.txt'
# fileName = '10x10 non-solution.txt'
# fileName = '11x11 p1.txt'
# fileName = '10x10 p2.txt'
# fileName='10x10 p3.txt'
fileName='10x10;2;32;18.txt'

blocks=Read.getBlock(fileName)
size=Read.getSize(blocks)
length=Read.getLength(size)

def searchBlockNum(b,p):
    for i in range(len(b)):
        temp=b[i]
        if p in temp:
            return i

def backTrace(sol,r):
    result=None
    # sol=StarList(sol)#ready to remove
    if sol.getSize()==sol.getCount():
        result=sol
    else:
        candidate=list(combinations(blocks[r],limit))
        for i in candidate:
            indexA=r*limit
            indexB=r*limit+1
            (a,b)=i
            blockA=searchBlockNum(blocks,a)
            blockB=searchBlockNum(blocks,b)
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                temp=backTrace(sol,r+1)
                if temp is not None:
                    result=temp
                    break
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return result

solution=StarList(length*limit)

start=timeit.default_timer()
backTrace(solution,0)
stop=timeit.default_timer()
print('Time cost: ',stop-start,'second')

# print(solution)
Drawfield.drawGUI(blocks,solution.getSolutionList())
