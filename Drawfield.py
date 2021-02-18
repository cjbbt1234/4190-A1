from array import *
import Read
def createField (col,row):
    arr=[]
    for i in range(col):
        col=[]
        for j in range(row):
            col.append(0)
        arr.append(col)
    return arr

# blocks=[[1,2,3,6,7,8],
#         [4,5,10],
#         [9,14,15],
#         [11,12,16,17,21,22,23,24],
#         [13,18,19,20,25]]

#blocks=Read.getBlock('10x10 puzzle-1.txt')
blocks=Read.getBlock('8x8 p1.txt')

def fillBlock(blcokNum,cells,array):
    a=len(array)
    b=len(array[0])
    for i in cells:
        # print(i)
        row=int((i-1)/a)
        col=(i-1)%b
        # print(row,col)
        array[row][col]=blcokNum
        # print(array)


def printField(array):
    a=len(array)
    b=len(array[0])
    # print(a,b)
    print('+'+'-+'*(b))
    for x in array:
        row='|'
        for y in x:
            if y==10:
                y=0
            row=row+str(y)+'|'
        print(row)
        print('+'+'-+'*(b))

temp=createField(8,8)
counter=1
for i in blocks:
    fillBlock(counter,i,temp)
    counter=counter+1
printField(temp)
# https://python-reference.readthedocs.io/en/latest/docs/brackets/indexing.html
