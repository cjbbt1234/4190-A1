from itertools import combinations
import Read
from Star import  StarList
import Drawfield
import timeit
from copy import copy,deepcopy

limit=2

fileName='10x10 puzzle-1.txt'
# fileName='14x14 p1.txt'
# fileName='8x8 p1.txt'
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


def removeNeighbor(index, block, length):
    if index%length==1: #left edge
        neig=[index - length, index - length + 1, index + 1, index + length, index + length + 1]
    elif index%length==0: #right edge
        neig=[index - length, index - length - 1, index - 1, index + length, index + length - 1]
    else:
        neig=[index - length, index - length - 1, index - 1, index + length, index + length - 1, index - length + 1, index + 1, index + length + 1]
    for i in neig:
        for j in block:
            if i in j:
                j.remove(i)
    return block

def removeColandRow(sol,block,length):
    # sol=StarList(sol)#ready to remove
    rowCount=[]
    colCount=[]
    for i in range(length):
        rowCount.append(0)
        colCount.append(0)
    for index in range(sol.getCount()):
        star=sol.getStar(index)
        pos=star.getPosition()
        row=int((pos-1)/length)
        col=int((pos-1)%length)
        rowCount[row]+=1
        colCount[col]+=1
    for i in range(length):
        if(rowCount[i]==2):
            elements=list( range(i*length+1,i*length+length+1) )
            for j in elements:
                for l in block:
                    if j in l:
                        l.remove(j)
    for i in range(length):
        if(colCount[i]==2):
            elements=list( range(i+1,length*length+1,length) )
            for j in elements:
                for l in block:
                    if j in l:
                        l.remove(j)

def deepcopy2d(block):
    result=[]
    for i in block:
        temp=[]
        for j in i:
            temp.append(j)
        result.append(temp)
    return result

def backTraceWithForward(sol,r,block):
    result=None
    if sol.getSize()==sol.getCount():
        result=sol
    else:
        # print(blockCopy[r])
        # candidate=list(combinations(blockCopy[r],limit))
        candidate=[]
        for i in range(len(block[r])):
            for j in range(i+1,len(block[r])):
                candidate.append( (block[r][i],block[r][j]) )

        for i in candidate:
            indexA=r*limit
            indexB=r*limit+1
            (a,b)=i
            blockA=searchBlockNum(block,a)
            blockB=searchBlockNum(block,b)
            # if(blockA==None or blockB==None):
            #     print(blockCopy[r])
            #     print(candidate)
            #     print(blockCopy,'<<<<<<<<<<<<<<<<<<<<<<<')
            #     break
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                tempCopy=deepcopy2d(block)
                removeNeighbor(a,tempCopy,length)
                removeNeighbor(b,tempCopy,length)
                removeColandRow(sol,tempCopy,length)
                temp=backTraceWithForward(sol,r+1,tempCopy)
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
    Drawfield.drawGUI(blocks,solution.getSolutionList())

    # solution=StarList(length*limit)
    # start=timeit.default_timer()
    # backTrace(solution,0)
    # stop=timeit.default_timer()
    # print('Time cost: ',stop-start,'second')
    # Drawfield.drawGUI(blocks,solution.getSolutionList())

main()
# blocks=a
# main()
