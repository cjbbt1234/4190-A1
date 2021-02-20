from itertools import combinations
import Read
from Star import  StarList
import Drawfield
import timeit
from copy import copy,deepcopy

limit=2

# fileName='10x10 puzzle-1.txt'
# fileName='14x14 p1.txt'
fileName='8x8 p1.txt'
# fileName = '10x10 non-solution.txt'
# fileName = '11x11 p1.txt'
# fileName = '10x10 p2.txt'
# fileName='10x10 p3.txt'
# fileName='10x10;2;32;18.txt'
# fileName='12x12 p1.txt'

blocks=Read.getBlock(fileName)
size=Read.getSize(blocks)
length=Read.getLength(size)
a=sorted(blocks,key=len)

def testSort():
    print(blocks)
    print(a)

# testSort()

def deepCopyTest():
    b=deepcopy(blocks)
    b[0]=['fuck']
    print(b)
    print(blocks)
    return b

# b=deepCopyTest()
# blocks[1][0]=999999
# print('--------------\n',blocks)
# print(b)


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


def removeNeighbor(index,block,size):
    if index%size==1: #left edge
        neig=[index-size,index-size+1,index+1,index+size,index+size+1]
    elif index%size==0: #right edge
        neig=[index-size,index-size-1,index-1,index+size,index+size-1]
    else:
        neig=[index-size,index-size-1,index-1,index+size,index+size-1,index-size+1,index+1,index+size+1]
    for i in neig:
        for j in block:
            if i in j:
                j.remove(i)
    return block

def deepcopy2d(block):
    result=[]
    for i in block:
        temp=[]
        for j in i:
            temp.append(j)
        result.append(temp)
    return result

def backTraceWithForward(sol,r,block):
    blockCopy=deepcopy2d(block)
    result=None
    if sol.getSize()==sol.getCount():
        result=sol
    else:
        print(blockCopy[r])
        # candidate=list(combinations(blockCopy[r],limit))

        candidate=[]
        for i in range(len(blockCopy[r])):
            for j in range(i+1,len(blockCopy[r])):
                candidate.append( (blockCopy[r][i],blockCopy[r][j]) )

        for i in candidate:
            indexA=r*limit
            indexB=r*limit+1
            (a,b)=i
            blockA=searchBlockNum(blockCopy,a)
            blockB=searchBlockNum(blockCopy,b)
            if(blockA==None or blockB==None):
                print(blockCopy[r])
                print(candidate)
                print(blockCopy,'<<<<<<<<<<<<<<<<<<<<<<<')
                break
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                removeNeighbor(indexA,blockCopy,size)
                removeNeighbor(indexB,blockCopy,size)
                temp=backTraceWithForward(sol,r+1,blockCopy)
                if temp is not None:
                    result=temp
                    break
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return result


def main():
    solution=StarList(length*limit)

    start=timeit.default_timer()
    # backTrace(solution,0)
    backTraceWithForward(solution,0,blocks)
    stop=timeit.default_timer()
    print('Time cost: ',stop-start,'second')

    print(solution)
    # Drawfield.drawGUI(blocks,solution.getSolutionList())

main()
# blocks=a
# main()
