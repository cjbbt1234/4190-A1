from itertools import combinations
import Read
from Star import  StarList
import Drawfield
import timeit
from copy import copy,deepcopy
import random

limit=2

# fileName='10x10 puzzle-1.txt'
fileName='14x14 p1.txt'
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

def checkRemainDomain(sol,block):
    result = True
    length = int(sol.getSize()/2)
    UnSignBlock = sol.getCount()
    for i in range(UnSignBlock, length):
        domainCount = len(block[i])
        if domainCount <=2:
            result = False
            break
        elif domainCount >=5:
            continue
        else:
            minValue = min(block[i])
            currBlock = block[i]
            if domainCount == 3:
                if(minValue+1 in currBlock and (minValue+length in currBlock or minValue+length+1 in currBlock)):
                    result = False
                    break
                elif(minValue+length in block[i] and (minValue+length-1 in currBlock or minValue+length+1 in currBlock)):
                    result = False
                    break
            elif domainCount == 4:
                if(minValue+1 in currBlock and minValue+length in currBlock and minValue+length+1 in currBlock):
                    result = False
                    break
    return result







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
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                tempCopy=deepcopy2d(block)
                removeNeighbor(a,tempCopy,length)
                removeNeighbor(b,tempCopy,length)
                removeColandRow(sol,tempCopy,length)
                if checkRemainDomain(sol,tempCopy):
                    temp=backTraceWithForward(sol,r+1,tempCopy)
                    if temp is not None:
                        result=temp
                        break
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return result

def backTraceWithH1(sol,r,block):
    result=None
    if sol.getSize()==sol.getCount():
        result=sol
    else:
        # print(blockCopy[r])
        # candidate=list(combinations(blockCopy[r],limit))
        minlength = 1000
        minIndex = -1
        minArray = []
        for i in range(int(sol.getCount()/2),len(block)):
            if len(block[i]) < minlength:
                minlength = len(block[i])
                minArray = []
                minArray.append(i)
                minIndex = i
            elif len(block[i])==minlength:
                minArray.append(i)
        newIndex = random.choice(minArray)
        if r!=newIndex:
            swapA = block[newIndex]
            swapB = block[r]
            block[r] = swapA
            block[newIndex] = swapB
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
            sol.setStar(indexA,a,blockA)
            sol.setStar(indexB,b,blockB)
            if sol.localCheckAll(limit):
                tempCopy=deepcopy2d(block)
                removeNeighbor(a,tempCopy,length)
                removeNeighbor(b,tempCopy,length)
                removeColandRow(sol,tempCopy,length)
                if checkRemainDomain(sol,tempCopy):
                    temp=backTraceWithH1(sol,r+1,tempCopy)
                    if temp is not None:
                        result=temp
                        break
            sol.resetStar(indexA)
            sol.resetStar(indexB)
    return result

def backTraceWithH2(sol,r,block):
    result=None
    if sol.getSize()==sol.getCount():
        result=sol
    else:
        candidate=[]
        for i in range(len(block[r])):
            for j in range(i+1,len(block[r])):
                candidate.append( (block[r][i],block[r][j]) )


def getNeighbor(p,length):
    list=None
    up=p-length
    down=p+length
    right=p+1
    left=p-1
    upleft=p-length-1
    upright=p-length+1
    downleft=p+length-1
    downright=p+length+1
    if p==1:
        list=[right,down,downright]
    elif p==length:
        list=[left,downleft,down]
    elif p==length*length-length+1:
        list=[up,upright,right]
    elif p==length*length:
        list=[left,up,upleft]
    elif p%length==1:#left edge
        list=[up,upright,right,down,downright]
    elif p%length==0:#right edge
        list=[up,upleft,left,downleft,down]
    elif p>1 and p<length: #first row
        list=[left,downleft,down,downright,right]
    elif p<length*length and p>length*length-length+1:
        list=[left,upleft,up,upright,right]
    else:
        list=[up,upright,upleft,left,right,down,downleft,downright]
    return list





def sortCandidate(candidate,block,length,r):
    candidateSortlist=[]
    for c in candidate:
        (x,y)=c
        row={}
        col={}
        neig={}
        #if same row:
        if  int((x-1)/length)==int((y-1)/length):
            r=int((x-1)/length)
            row=set(range(r*length+1,r*length+length+1))
        #if same col
        if (x-1)%length==(y-1)%length:
            c=(x-1)%length
            col=set(range(c+1,length*length+1,length))
        #get all neighbor of x and y




def main():
    solution=StarList(length*limit)

    start=timeit.default_timer()
    backTraceWithH1(solution,0,blocks)
    stop=timeit.default_timer()
    print('Time cost: ',stop-start,'second')

    print(solution)
    # Drawfield.drawGUI(blocks,solution.getSolutionList())

    # solution=StarList(length*limit)
    # start=timeit.default_timer()
    # backTraceWithForward(solution,0,blocks)
    # stop=timeit.default_timer()
    # print('Time cost: ',stop-start,'second')
    # print(solution)



    # Drawfield.drawGUI(blocks,solution.getSolutionList())

# main()
# blocks=a
main()

print('-----------------neig test---------------')
l=[1,4,10,31,41,50,91,98,100]
for i in l:
    print(i,getNeighbor(i,10))
