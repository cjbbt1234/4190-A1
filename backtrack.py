from itertools import combinations
import Read
import Star
from Star import StarList
import Drawfield


limit=2
fileName='10x10 puzzle-1.txt'
# fileName='14x14 p1.txt'
# fileName='8x8 p1.txt'
# fileName = '10x10 non-solution.txt'
blocks=Read.getBlock(fileName)
size=Read.getSize(blocks)
length=Read.getLength(size)


def searchBlockNum(b,p):
    for i in range(len(b)):
        temp=b[i]
        if p in temp:
            return i

solution=StarList(length*limit)

# def genCandidate():
#     cand=list(combinations(range(1,length+1),limit))
#     # print(len(cand))
#     for i in cand:
#         if abs(i[0]-i[1])==1:
#             cand.remove(i)
#     # print(len(cand))
#     return cand


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
            if(abs(a-b)==1):
                continue
            blockA=searchBlockNum(blocks,a)
            blockB=searchBlockNum(blocks,b)
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                result=backTrace(sol,r+1)
                if result is not None:
                    return result
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return None

def forward_checking(sol,r):
    sol=StarList(sol)
    numInRow=list(range(r*length+1,r*length+length+1))
    last_assign_1 = sol.getStar(2*(r-1))
    last_assign_2 = sol.getStar(2*r-1)
    for i in [-1, 0, 1]:#check row
        if last_assign_1+i+length in numInRow:
            numInRow.remove(last_assign_1+i+length)
        if last_assign_2+i+length in numInRow:
            numInRow.remove(last_assign_2+i+length)
    return numInRow

def backTracewithForward(sol,r):
    if sol.getSize()==sol.getCount():
        return sol
    else:
        candidate=forward_checking(sol,r)
        for i in candidate:
            indexA=r*limit
            indexB=r*limit+1
            (a,b)=i
            if(abs(a-b)==1):
                continue
            blockA=searchBlockNum(blocks,a)
            blockB=searchBlockNum(blocks,b)
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                result=backTrace(sol,r+1)
                if result is not None:
                    return result
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return None


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




import timeit

start = timeit.default_timer()

backTracewithForward(solution,0)

if(solution.getCount()!=solution.getSize()):
    print("No solution")
else:
    print(solution)

stop = timeit.default_timer()

print('Time: ', stop - start)









