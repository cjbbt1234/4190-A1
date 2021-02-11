import copy


class Star:

    def __init__(self,p,block):
        self.position=p
        self.block=block

    def getPosition(self):
        return self.position

    def getBlock(self):
        return self.block

    def conflict(self,arrayOfStar):
        counter=0
        for i in arrayOfStar:
            if self.block==i.getBlock():
                counter=counter+1
            if counter>1:
                return False
        return True

    def __str__(self):
        return str(self.position)+'+'+str(self.block)



class StarList:
    def __init__(self):
        self.list=[]
    def addStar(self,star):
        self.list.append(star)
    def getStar(self,index):
        return self.list[index]
    def neighborCheck(self):
        size=len(self.list)/2
        for i in range(len(self.list)):
            a=self.list[i].getPosition()
            for j in range(i,len(self.list)):
                b=self.list[j].getPosition()
                if((a-b==1)|(b-a==1)|(a-b==size)|(b-a==size)|(a-b==size-1)|(b-a==size-1)|(a-b==size+1)|(b-a==size+1)):
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


a=StarList()
a.addStar(Star(7,1))
a.addStar(Star(4,2))
a.addStar(Star(15,3))
a.addStar(Star(18,4))
a.addStar(Star(21,5))
print(a.neighborCheck())
print(a.blockCheck(1))
print(a.rowCheck(1),a.colCheck(1))

