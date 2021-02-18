from itertools import combinations
import Read
import Star
from Star import StarList
import Drawfield
print("Hello world")
p=list(range(0,5))
print(p)
print(list(combinations(p,2)))
# a=list(combinations(p,2))
# print(a)



limit=2
fileName='10x10 puzzle-1.txt'
blocks=Read.getBlock(fileName)
size=Read.getSize(blocks)
length=Read.getLength(size)

print(blocks,size,length)

for r in range(length):
    print(list(range(r*length,r*length+length)))

def searchBlockNum(b,p):
    for i in range(len(b)):
        temp=b[i]
        if p in temp:
            return i

solution=StarList(length*limit)

def backTrace(sol,r):
    sol=StarList(sol)
    # if sol.getSize()==sol.getCount():
    if sol.neighborCheck()^sol.blockCheck()^sol.colCheck()^sol.rowCheck():
        return sol
    else:
        rowNum=list(range(r*length,r*length+length))
        candidate=list(combinations(rowNum,limit))
        for i in candidate:
            indexOne=r*limit-1
            indexTwo=r*limit-2
            (a,b)=i
            blockOne=searchBlockNum(blocks,a)
            blockTwo=searchBlockNum(blocks,b)




