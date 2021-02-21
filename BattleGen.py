import Drawfield
import random
import Heuristic_proto


def getNeighbor(p,length):
        lists=None
        up=p-length
        down=p+length
        right=p+1
        left=p-1
        if p==1:
            lists=[right,down]
        elif p==length:
            lists=[left,down]
        elif p==length*length-length+1:
            lists=[up,right]
        elif p==length*length:
            lists=[left,up]
        elif p%length==1:#left edge
            lists=[up,right,down]
        elif p%length==0:#right edge
            lists=[up,left,down]
        elif p>1 and p<length: #first row
            lists=[left,down,right]
        elif p<length*length and p>length*length-length+1:
            lists=[left,up,right]
        else:
            lists=[up,down,left,right]
        return lists

class BattleGen:
    def __init__(self):
        pass

    def genMap(self,length):
        points= list(range(1,length*length+1))
        lists=[]
        for i in range(length):
            seed=points[int(random.random()*len(points))]
            temp=[]
            temp.append(seed)
            points.remove(seed)
            lists.append(temp)
        while(len(points)!=0):
            if(random.random()>0.9):
                group=lists[int(random.random()*len(lists))]
            else:
                group=sorted(lists,key=len)[0]
            index=int(random.random()*len(group))
            p=group[index]
            grow=getNeighbor(p,length)
            selected=grow[ int( random.random()*len(grow))  ]
            if selected in points:
                group.append(selected)
                points.remove(selected)
        return lists


import Heuristic_proto
import Star
from Star import StarList
import Drawfield
import Read
def testGen():
    t=BattleGen()
    arrays=[]
    for i in range(100):
        testArray=t.genMap(8)
        arrays.append(testArray)
        print(i,'-->',testArray)



#
# while(len(points)!=0):
#     print(len(points))
#     if(random.random()>0.75):
#         index1=int(random.random()*len(lists))
#     else:
#         index1=lists.index(sorted(lists,key=len)[0])
#     index2=int(random.random()*len(lists[index1]))
#     if len(lists[index1])>length*1.8:
#         continue
#     p=lists[index1][index2]
#     grow=getNeighbor(p,length)
#     # i=grow[int(random.random()*len(grow))]
#     # if i in points:
#     #     lists[index1].append(i)
#     #     points.remove(i)
#     for i in grow:
#         if i not in points:
#             grow.remove(i)
#     selected=grow[int(random.random()*len(grow))]
#     if(selected in points):
#         lists[index1].append(selected)
#         points.remove(selected)
# print(lists)
#
# # Drawfield.drawGUI(lists,[])
# import Heuristic_proto
# import Star
# # Drawfield.drawGUI(lists,[])
# solution=Star.Starlists(length*2)
# Heuristic_proto.backTraceHybrid(solution,0,lists)
# print(solution)
# print(solution.getCount())
# Drawfield.drawGUI(lists,solution.getSolutionlists())


