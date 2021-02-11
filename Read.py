def getBlock(filename):
    f = open(filename,'r')
    a=[]
    for lines in f:
        print(lines)
        index=lines.find('t')
        block=list(map(int,lines[index+1:len(lines)-1].split(',')))
        # print(block)
        a.append(block)
    return a
print(getBlock('test.txt'))

