import copy


class Star:
    def __init__(self):
        self.position=-1
        self.block=-1
    #
    # def __init__(self,p,block):
    #     self.position=p
    #     self.block=block

    def setPosition(self,p):
        self.position=p

    def getPosition(self):
        return self.position

    def setBlock(self,b):
        self.block=b

    def getBlock(self):
        return self.block

    # def conflict(self,arrayOfStar):
    #     counter=0
    #     for i in arrayOfStar:
    #         if self.block==i.getBlock():
    #             counter=counter+1
    #         if counter>1:
    #             return False
    #     return True

    def __str__(self):
        return str(self.position)+'+'+str(self.block)



class StarList:
    def __init__(self,size):
        self.list=[]
        self.size=size #size of list
        for i in range(size):
            self.list.append(Star())
        self.count=0

    def __str__(self):
        a=[]
        for i in self.list:
            a.append('('+str(i)+')')
        return str(a)

    def getSolutionList(self):
        result=[]
        for s in self.list:
            result.append(s.getPosition())
        return result

    def setStar(self,index,p,b):
        temp=self.list[index]
        temp.setPosition(p)
        temp.setBlock(b)
        self.count=self.count+1
    def resetStar(self,index):
        temp=self.list[index]
        temp.setBlock(-1)
        temp.setPosition(-1)
        self.count=self.count-1
    def addStar(self,star):
        self.list.append(star)
    def getStar(self,index):
        return self.list[index]
    def getSize(self):
        return self.size
    def getCount(self):
        return self.count

    def neighborCheck(self):
        size=len(self.list)/2
        for i in range(len(self.list)):
            a=self.list[i].getPosition()
            for j in range(i,len(self.list)):
                b=self.list[j].getPosition()
                # if((a-b==1)|(b-a==1)|(a-b==size)|(b-a==size)|(a-b==size-1)|(b-a==size-1)|(a-b==size+1)|(b-a==size+1)):
                #     return False
                (x1,y1)=(int( (a-1)/size ),(a-1)%size)
                (x2,y2)=(int( (b-1)/size ),(b-1)%size)
                if(abs(x1-x2)+abs(y1-y2)==1 or abs(x1-x2)+abs(y1-y2)==2):
                    return False
        return True
    def localNeighborCheck(self):
        size=len(self.list)/2
        for i in range(self.count):
            a=self.list[i].getPosition()
            for j in range(i,self.count):
                b=self.list[j].getPosition()
                # if((a-b==1)|(b-a==1)|(a-b==size)|(b-a==size)|(a-b==size-1)|(b-a==size-1)|(a-b==size+1)|(b-a==size+1)):
                #     # print(a,b,"false")
                #     return False
                (x1,y1)=(int( (a-1)/size ),(a-1)%size)
                (x2,y2)=(int( (b-1)/size ),(b-1)%size)
                if(abs(x1-x2)+abs(y1-y2)==1 or (abs(x1-x2)==1 and abs(y1-y2)==1)):
                    # print(a,b,'problem')
                    return False
        return True


    def blockCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list:
            counter[i.getBlock()-1]=counter[i.getBlock()-1]+1
            if(counter[i.getBlock()-1]>limit):
                return False
        for i in counter:
            if(i!=limit):
                return False
        return True
    def localBlockCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list[0:self.count]:
            # print(i)
            counter[i.getBlock()-1]=counter[i.getBlock()-1]+1
            if(counter[i.getBlock()-1]>limit):
                return False
        return True


    def rowCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list:
            temp=i.getPosition()
            counter[ int((temp-1)/size) ]=counter[ int((temp-1)/size) ]+1
            if(counter[ int((temp-1)/size) ]>limit):
                return False
        for i in counter:
            if(i!=limit):
                return False
        return True
    def localRowCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list[0:self.count]:
            temp=i.getPosition()
            counter[ int((temp-1)/size) ]=counter[ int((temp-1)/size) ]+1
            if(counter[ int((temp-1)/size) ]>limit):
                return False
        for i in counter:
            if(i>limit):
                return False
        return True


    def colCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list:
            temp=i.getPosition()
            counter[(temp-1)%size]=counter[(temp-1)%size]+1
            if counter[(temp - 1) % size]>limit:
                return False
        for i in counter:
            if(i!=limit):
                return False
        return True

    def localColCheck(self,limit):
        size=int(len(self.list)/limit)
        counter=[]
        for i in range(size):
            counter.append(0)
        for i in self.list[0:self.count]:
            temp=i.getPosition()
            counter[(temp-1)%size]=counter[(temp-1)%size]+1
            if counter[(temp - 1) % size]>limit:
                return False
        for i in counter:
            if(i>limit):
                return False
        return True

    def localCheckAll(self,limit):
        # print("-----------------------------------------------------------")
        # if not self.localNeighborCheck():
        #     print("self.localNeighborCheck() false")
        # if not self.localBlockCheck(limit):
        #     print("self.localBlockCheck(limit) false")
        # if not self.localColCheck(limit):
        #     print("self.localColCheck(limit) false")
        # if not self.localRowCheck(limit):
        #     print("self.localRowCheck(limit) false")
        return self.localNeighborCheck() and self.localBlockCheck(limit) and self.localColCheck(limit) and self.localRowCheck(limit)

def extendedArray(size):
    s=size+2
    array=[]
    for i in range(s):
        subA=[]
        for j in range(s):

            if(i!=0 and j!=0 and i!=s-1 and j!=s-1):
                subA.append(str((i-1)*size+j).zfill(2))
            else:
                subA.append('00')
        print(subA)

extendedArray(10)
a=StarList(20)
# a.addStar(Star(2,0))
# a.addStar(Star(8,1))
# a.addStar(Star(16,0))
# a.addStar(Star(20,9))
# a.addStar(Star(22,2))
# a.addStar(Star(24,2))
# a.addStar(Star(37,1))
# a.addStar(Star(40,9))
# a.setStar(0,3,0)
# a.setStar(1,5,1)
# a.setStar(2,17,2)
# a.setStar(3,19,3)
# a.setStar(4,23,0)
# a.setStar(5,25,1)
# a.setStar(6,31,4)
# a.setStar(7,38,2)
# a.setStar(8,44,5)
# a.setStar(9,50,3)
# a.setStar(10,51,4)
# a.setStar(11,56,6)
# a.setStar(12,68,7)
# a.setStar(13,70,8)
# a.setStar(14,72,5)
# a.setStar(15,76,6)
# a.setStar(16,84,9)
# a.setStar(17,89,8)
# a.setStar(18,92,9)
# a.setStar(19,97,7)
# print(a.count)
# print(a.localNeighborCheck())
# print(a.localBlockCheck(2))
# print(a.localRowCheck(2),a.localColCheck(2))
# print(a.neighborCheck())
# print(a.blockCheck(2))
# print(a.rowCheck(2),a.colCheck(2))



