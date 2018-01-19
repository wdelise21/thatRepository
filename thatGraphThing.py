#Improtts
import turtle
# # #
wn = turtle.Screen() #that screen declaration
columnTurtle = turtle.Turtle() #turtle in charge of creating columns
scaleTurtle = turtle.Turtle() #turtle in charge of the scale
scaleCount = 0

# # #
def quickLoad():
    columnTurtle.speed(10) #max speed w/ animation
    scaleTurtle.speed(0) #minimum animation

#Root func
def main():
    getConfig_onstart()
    TlDr() #generates bottom line
    orientTurtles() #default orientation = north, left side
    plotScale()
    barCount = 0
    print(".")
    print(".")
    print("Each tick on the left bar represents 5 units.")
    print(".")
    print(".")
    print(".")
    print("There is a rough maximum value of 65 units due to size constraints")
    print("")
    print("")
    while True:
        plotBar() #asks for #, plots bar.
        global barCount
        global barMax
        barCount += 1
        if barCount == barMax:
            print("Graph Full")
            break
        
def getConfig_onstart():
    global barMax
    print("This is a basic graphing program.")
    print("This program uses Python Turtle Graphics")
    print("Please input your choice of settings as requested")
    barWidth_str = raw_input("Width of bars? (Micro, Small, Normal, Wide, XL) : ")
    if barWidth_str == "Micro":
        global barWidth
        print("Micro Selected") # 22 max
        barWidth = 5
        barMax = 22
    elif barWidth_str == "Small":
        print("Small Selected") # 16 max 
        barWidth = 15
        barMax = 16
    elif barWidth_str == "Normal":
        print("Normal Selected") # 11 max
        barWidth = 30
        barMax = 11
    elif barWidth_str == "Wide": # 8 max
        print("Wide Selected")
        barWidth = 45
        barMax = 8
    elif barWidth_str == "XL": # 7 max
        print("XL selected")
        barWidth = 60
        barMax = 7
    else:
        print("Couldn't find that option, sorry. Setting to default.")
    quickLoad_var = raw_input("Quick Load? (Y/N): ")
    if quickLoad_var == "Y":
        quickLoad()
    elif quickLoad_var == "y":
        quickLoad()

def orientTurtles(): #orients turtles in the beginning (after box is drawn)
    columnTurtle.left(180)
    columnTurtle.forward(250)
    columnTurtle.right(90)

def TlDr(): #not actually a Tl;Dr, it's the bottom line, get it...
    columnTurtle.right(90)
    columnTurtle.penup()
    columnTurtle.forward(300)
    columnTurtle.left(90)
    columnTurtle.pendown() #now positioned at bottom of screen
    columnTurtle.forward(300)
    columnTurtle.left(90)
    columnTurtle.forward(600)  
    columnTurtle.left(90)
    columnTurtle.forward(600)  
    columnTurtle.left(90)
    columnTurtle.forward(600) 
    columnTurtle.left(90)
    columnTurtle.forward(300) #box is now drawn

def plotScale(): #plots the scale, with a 5 interval
    scaleTurtle.right(90)
    scaleTurtle.penup()
    scaleTurtle.forward(300)
    scaleTurtle.left(90)
    scaleTurtle.pendown() 
    scaleTurtle.penup()
    scaleTurtle.left(180)
    scaleTurtle.forward(300)
    scaleTurtle.pendown()
    scaleTurtle.right(90)
    while True: #this iterates each tab up to 60
        scaleTurtle.forward(45) 
        scaleTurtle.right(90) 
        scaleTurtle.forward(15)
        scaleTurtle.left(180)
        scaleTurtle.forward(15)
        scaleTurtle.right(90)
        global scaleCount
        scaleCount += 1 #increases counter
        if scaleCount > 12: #not scaled for window
            break
        
def scooch(): #scooches the turtle over
    columnTurtle.left(90)
    columnTurtle.forward(20) 
    columnTurtle.left(90)

def plotBar():
    columnTurtle.speed(5) #slightly better agile animation
    global barWidth
    global columnHeight
    columnHeight = str(input("Input Value: "))
    columnTurtle.forward(int(columnHeight)*9) #the 9 is for unit measurements
    columnTurtle.right(90)
    columnTurtle.forward(barWidth)
    columnTurtle.right(90)
    columnTurtle.forward(int(columnHeight)*9) #9 is the same as above
    scooch()


# Execution
main() #runs main function
wn.exitonclick() #if not glitched, screen will end when clicked
