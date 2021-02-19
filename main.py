from itertools import combinations
import Read
import Star
from Star import StarList
import Drawfield
# print("Hello world")
# p=list(range(0+1,5+1))
# print(p)
# print(list(combinations(p,2)))
# a=list(combinations(p,2))
# print(a)

print('--------------------------------')

limit=2
fileName='10x10 puzzle-1.txt'
fileName='8x8 p1.txt'
blocks=Read.getBlock(fileName)
size=Read.getSize(blocks)
length=Read.getLength(size)
print('details:------------------------')
# print(blocks)
print(size,length)
print('end---------------------------------')
# for r in range(length):
#     print(list(range(r*length,r*length+length)))

def searchBlockNum(b,p):
    for i in range(len(b)):
        temp=b[i]
        if p in temp:
            return i

solution=StarList(length*limit)

def backTrace(sol,r):
    if sol.getSize()==sol.getCount():
        return sol
    else:
        numInRow=list(range(r*length+1,r*length+length+1))
        candidate=list(combinations(numInRow,limit))
        for i in candidate:
            indexA=r*limit
            indexB=r*limit+1
            (a,b)=i
            blockA=searchBlockNum(blocks,a)
            blockB=searchBlockNum(blocks,b)
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                print('pass + ',r)
                sol=backTrace(sol,r+1)
                return sol
            else:
                sol.resetStar(indexA)
                sol.resetStar(indexB)


# def backTrace(sol,r):
#     # sol=StarList(sol)
#     # if sol.getSize()==sol.getCount():
#     # if sol.neighborCheck() and sol.blockCheck() and sol.colCheck() and sol.rowCheck():
#     #      return sol
#     print(r,'size',sol.getSize(),'currsize',sol.getCount())
#     print(sol)
#     # if sol.getSize()==sol.getCount():
#     #     print('goooooooooooooooooooood')
#     #     return sol
#     if(False):
#         pass
#     else:
#         rowNum=list(range((r-1)*length,(r-1)*length+length))
#         candidate=list(combinations(rowNum,limit))
#         for i in candidate:
#             indexOne=r*limit-1
#             indexTwo=r*limit-2
#             (a,b)=i
#             blockOne=searchBlockNum(blocks,a+1)
#             blockTwo=searchBlockNum(blocks,b+1)
#             # print(blockOne,'ONE')
#             # print(blockTwo,'TWO')
#             # starOne=sol.getStar(indexOne)
#             # starTwo=sol.getStar(indexTwo)
#             # starOne.setPosition(a)
#             # starOne.setBlock(blockOne)
#             # starTwo.setPosition(b)
#             # starTwo.setBlock(blockTwo)
#             sol.setStar(indexOne,a,blockOne)
#             sol.setStar(indexTwo,b,blockTwo)
#             if sol.localCheckAll(limit):
#                 print('good')
#                 return backTrace(sol,r+1)
#             # else:
#             #     print('bad')
#             #     print(a,b)
#             sol.resetStar(indexOne)
#             # print('immmmmmmm')
#             sol.resetStar(indexTwo)


backTrace(solution,0)
print(solution)
print('end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program ')





