from tkinter import *
from tkinter import ttk
import random
from bubble import bubbleSort
from quick import quickSort
from insertion import insertionSort
from selection import selectionSort
from merge import mergeSort


root = Tk()
root.title('Sorthing Visualizer')
root.maxsize(900,600)
root.config(bg="#525352")

selected = StringVar()
data=[]
def drawData(data,colorarray):
    canvas.delete("all")
    c_height=380
    c_width=600
    x_width=c_width/(len(data)+1)
    offset=30
    spacing=10
    normalizedData=[i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0=i*x_width+offset+spacing
        y0=c_height-height *340

        x1=(i+1) * x_width +offset
        y1=c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW, text=str(data[i]))
    root.update_idletasks()


def generate():
    global data 
    print('algorithm selected' + selected.get())
    
    data=[]
    minValue=int(min_e.get())

   
 
    maxValue=int(max_e.get())
   

    size=int(size_e.get())
    
    for _ in range(size):
        data.append(random.randrange(minValue, maxValue+1))
    

    drawData(data, ['red' for x in range(len(data))])


def StartAlgo():
    global data
    if not data:return

    if menu.get() == 'Quick Sort':

        quickSort(data,0,len(data)-1,drawData,SpeedScale.get())
        
    
    elif menu.get()== 'Bubble Sort':
         bubbleSort(data, drawData, SpeedScale.get())
    
    elif menu.get()== 'Insertion Sort':
        insertionSort(data, drawData, SpeedScale.get())
    
    elif menu.get()== 'Selection Sort':
        selectionSort(data, drawData, SpeedScale.get())

    elif menu.get()== 'Merge Sort':
        mergeSort(data, drawData, SpeedScale.get())

    drawData(data,['green' for x in range(len(data))])




    

UI_frame= Frame(root, width=600, height=200, bg='#AE8A7B')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600,height=380, bg='#EEE2DA')
canvas.grid(row=1, column=0, padx= 10, pady=5 )


Label(UI_frame, text="Algorithm: ", bg='#AE8A7B').grid(row=0,column=0,padx=5,pady=5,sticky=W)
menu= ttk.Combobox(UI_frame, textvariable=selected,values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort', 'Selection Sort'])
menu.grid(row=0, column=1, padx=5,pady=5)
menu.current(0)

SpeedScale= Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2,resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]")
SpeedScale.grid(row=0,column=2, padx=5,pady=5)


Button(UI_frame, text="Start" , command= StartAlgo, bg='#6F3141').grid(row=0,column=3, padx=5, pady=5)




size_e=SpeedScale= Scale(UI_frame, from_=3,resolution=0.2, orient=HORIZONTAL, label="Data Size")
size_e.grid(row=1,column=0,padx=5,pady=5)



min_e=SpeedScale= Scale(UI_frame, from_=0, to=10,resolution=0.2, orient=HORIZONTAL, label="Minimum Value")
min_e.grid(row=1,column=1,padx=5,pady=5)



max_e=SpeedScale= Scale(UI_frame, from_=10,resolution=0.2, orient=HORIZONTAL, label="Maximum Value")
max_e.grid(row=1,column=2,padx=5,pady=5)


Button(UI_frame, text="Generate" , command= generate, bg='#6F3141').grid(row=1,column=3, padx=5, pady=5)
root.mainloop()


