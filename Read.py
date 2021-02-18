import math
def getBlock(filename):
    f = open(filename,'r')
    a=[]
    for lines in f:
        # print(lines)
        index=lines.find('t')
        block=list(map(int,lines[index+1:len(lines)].split(',')))
        # print(block)
        a.append(block)
    return a

def getSize(a):
    sum=0
    for i in a:
        sum=sum+len(i)
    # print(sum)
    return sum

def getLength(size):
    return int(math.sqrt(size))

print(getLength(getSize(getBlock('10x10 puzzle-1.txt'))))

