import time
def selectionSort(data, drawData, timeTick):
   
    for step in range(len(data)):
        min_idx = step

        for i in range(step + 1, len(data)):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if data[i] < data[min_idx]:
                min_idx = i
            drawData(data,['green' if x==i  else 'red' for x in range(len(data))])
            time.sleep(timeTick)    
    
         
        # put min at the correct position
        (data[step], data[min_idx]) = (data[min_idx], data[step])
        
        drawData(data, ['green' for x in range(len(data))])

