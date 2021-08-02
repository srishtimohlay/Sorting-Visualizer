import time

def partition(data, head, tail, drawData, timeTick):
    border=head
    pivot=data[tail]
    drawData(data, getcolorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for i in range(head,tail):
         
         if data[i]<pivot:
            drawData(data, getcolorArray(len(data), head, tail, border, i,True))
            time.sleep(timeTick)
            data[border], data[i]= data[i], data[border]
            border+=1
         drawData(data, getcolorArray(len(data), head, tail, border, i))
         time.sleep(timeTick)

    drawData(data, getcolorArray(len(data), head, tail, border, i,True))
    time.sleep(timeTick)
    data[border],data[tail]=data[tail],data[border]
    return border

    



def quickSort(data, head, tail, drawData, timeTick):
    if head<tail:
        pIndex=partition(data, head, tail,drawData,timeTick)

        quickSort(data,head,pIndex-1,drawData,timeTick)

        quickSort(data,pIndex+1,tail,drawData,timeTick)


def getcolorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):  
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray