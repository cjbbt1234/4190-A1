from itertools import combinations
import Read
import Star
from Star import StarList
import Drawfield
from Heuristic_proto import *


limit=2
# fileName='10x10 puzzle-1.txt'
# fileName='14x14 p1.txt'
fileName='8x8 p1.txt'
# fileName='12x12 p1.txt'
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
import time

# tic=time.perf_counter()
# backTrace(solution,0)
# if(solution.getCount()!=solution.getSize()):
#     print("No solution")
# else:
#     print(solution)
# # print('end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program end of program ')
# toc=time.perf_counter()
# print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")

def solvepuzzle(solution,k,blocks):
    s=StarList(length*limit)

    start=timeit.default_timer()

    solution=backTrace(s,0)
    stop=timeit.default_timer()
    print('Time cost: ',stop-start,'second')

    print(solution)
    Drawfield.drawGUI(blocks,solution.getSolutionList())

def timefuction(solution,k,blocks):
    solution=StarList(length*limit)

    start=timeit.default_timer()


    # Start bar as a process
    p1 = multiprocessing.Process(target=solvepuzzle,args=(solution,0,blocks,))
    p2 = multiprocessing.Process(target=solvepuzzle,args=(StarList(length*limit),0,[[49, 57, 41, 58, 50, 42, 33], [32, 31, 30, 38, 22, 39, 29, 47, 37, 40], [60, 59, 52, 44, 53, 61, 45, 51], [26, 34, 18, 35, 43, 27, 25, 36], [24, 16, 8, 23, 15, 14, 6, 7], [21, 13, 20, 12, 28, 4, 5], [9, 10, 2, 11, 17, 1, 19, 3], [63, 62, 64, 56, 54, 55, 46, 48]],))
    p1.start()
    p2.start()

    # Wait for 10 seconds or until process finishes
    p1.join(3)
    p2.join(3)

    # If thread is still active
    if p1.is_alive():
        print("running... let's kill it...No solution")

        # Terminate - may not work if process is stuck for good
        # p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        p1.kill()

        p1.join()

import multiprocessing
import time

if __name__ == '__main__':
    timefuction(solution,0,blocks)







