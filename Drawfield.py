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
# blocks=Read.getBlock('8x8 p1.txt')
blocks=Read.getBlock('14x14 p1.txt')

length=Read.getLength(Read.getSize(blocks))

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
            if y>=10:
                y=hex(y)
                y=str(y)[len(str(y))-1]

            row=row+str(y)+'|'
        print(row)
        print('+'+'-+'*(b))

def drawGUI(array,solution):
    window=Tk()
    window.title("StarBattle")
    load=PhotoImage(file='pT78o6pec.gif')
    star='***********'
    window.geometry('1920x1080')
    # frame=Frame(window,relief=RAISED,borderwidth=2)
    # frame.pack(side=TOP, fill=BOTH,ipadx=50, ipady=50, expand=1)
    for x in range(len(array)):
        subarray=array[x]
        for y in subarray:
            if y in solution:
                Label (window,bg=COLORS[x-1],relief=GROOVE,text=star,width=5,height=3) .grid(row=int((y-1)/len(array)),column=(y-1)%len(array) )
            else:
                Label (window,bg=COLORS[x-1],relief=GROOVE,width=5,height=3) .grid(row=int((y-1)/len(array)),column=(y-1)%len(array) )
    window.mainloop()

temp=createField(length,length)
counter=1
for i in blocks:
    fillBlock(counter,i,temp)
    counter=counter+1
# printField(temp)
# https://python-reference.readthedocs.io/en/latest/docs/brackets/indexing.html

#https://blog.csdn.net/ahilll/article/details/81531587
# http://www.weixueyuan.net/a/557.html
from tkinter import *
COLORS=['honeydew4', 'LightBlue4', 'LightGoldenrod2', 'LavenderBlush4', 'gray74', 'AntiqueWhite4', 'gray64', 'yellow green', 'gray71', 'orange', 'maroon3', 'SteelBlue2', 'gray30', 'maroon2', 'SlateGray2', 'chocolate3']
COLORS=['LightCyan2', 'medium violet red', 'burlywood1', 'old lace', 'tan2', 'LightBlue3', 'firebrick2', 'green2', 'gray34', 'dodger blue', 'steel blue', 'gray6', 'DarkOrange2', 'turquoise1', 'gray38', 'LemonChiffon4']
# window=Tk()
# window.title("StarBattle")
# window.geometry('1280x720')
# frame=Frame(window,relief=RAISED,borderwidth=2)
# frame.pack(side=TOP, fill=BOTH,ipadx=5, ipady=5, expand=1)
# # for i in range (5):
# #     for j in range (5):
# #         Label (frame,bg='green',relief=RIDGE,width=10,height=5) .grid(row=i,column=j )

#
# window.mainloop()
