#!/usr/bin/python
#thatApp.py
"""
Will Delise

Application Basis containing Calc widget
"""







'''
Calculator Application
'''
# from varLib import * #Unnecessary if compiled seperately
#ran = True
#runIt = True
getFunction = 'Please input desired function'
getX = 'Please input the first numerical value'
getY = 'Please input the second numerical value'
ans = 'Null'
desFunction = 'Library Connection Error'
#End Assignments
#Begin Definitions
import time
def funcdir():
    functionli = ['add', 'subtract', 'multiply', 'divide', 'square root', 'base 2', 'Grade Me'] #Lists available functions in Calc
    print functionli #prints the list for the user
def checkFunction():
    desFunction = raw_input('>>>') #gets user input for which function
    
    '''
    Example of borderline overcommenting below
    '''
    if desFunction == 'add': #addition
        add()
    elif desFunction == 'subtract': #subtraction
        subtract()
    elif desFunction == 'multiply': #multiplication
        multiply()
    elif desFunction == 'divide': #division
        divide()
    elif desFunction == 'square root': #sort
        sqroot()
    elif desFunction == 'halt': #ends process
        runIt = False
    elif desFunction == 'help': #prints help dialogue
        funcdir()
    elif desFunction == 'base 2': #converts to base two; binary 
        funcBin()
    elif desFunction == 'Library Connection Error': #not sure what this is tbh but I'm scared to comment it out
        print desFunction
    elif desFunction == "Grade Me": #calculates your percentage and letter grade from a fraction
        findGrade()
        
    '''
    Example of overcommenting below
    '''
def add():
    print getX #asks for first value
    inLine = raw_input('>>>') #gets input
    x = inLine
    print getY #asks for second value
    inLine = raw_input('>>>') #gets input
    y = inLine
    ans = float(x) + float(y)
    print ans #prints the answer
def subtract():
    print getX #asks for first value
    inLine = raw_input('>>>') #gets input
    x = inLine
    print getY #asks for second value
    inLine = raw_input('>>>') #gets input
    y = inLine
    ans = float(x) - float(y)
    print ans #prints the answer
def multiply():
    print getX #asks for first value
    inLine = raw_input('>>>') #gets input
    x = inLine
    print getY #asks for second value
    inLine = raw_input('>>>') #gets input
    y = inLine
    ans = float(x) * float(y)
    print ans #prints the answer
def divide():
    print getX #asks for first value
    inLine = raw_input('>>>') #gets input
    x = inLine
    print getY #asks for second value
    inLine = raw_input('>>>') #gets input
    y = inLine
    ans = float(x) / float(y)
    print ans #prints the answer
def sqroot():
    import math #imports advanced functions
    num = input('>>>') #gets input
    print math.sqrt(num) #prints the sort function from the math object in the math module with the argument (num)
def funcBin():
    num = input('>>>') #gets input
    print bin(float(num))
def findGrade():
    print('Input your score')
    x = raw_input('>>>') #gets input
    print('Input the max score in the same units')
    y = raw_input('>>>') #gets input
    ans = float(x) / float(y) #sets the answer to the first number divided by the second number
    print int(100 * float(ans)) #converts ans to float value #multiplies the answer by 100 for percentage
    time.sleep(1)
    print('Checking Letter Grade:')
    '''
    Example of lazy and snarky dev commenting (you should aspire to this)
    '''
    #Note: I am quite aware how inefficient the check is, but I'm too lazy to fix it
    if float(ans) > 1: #Checks if over 100 for snarky comment
        print('A++')
        print("If you didn't have extra credit you might want to check again...")
    elif float(ans) >= .98: 
        if float(ans) <= 1: #float because yeh know, data types and all
            print('A+')
    elif float(ans) >= 0.93:
        if float(ans) <= 0.97:
            print('A')
    elif float(ans) >= 0.90:
        if float(ans) <= 0.93:
            print('A-')
    elif float(ans) >= 0.87:
        if float(ans) <= 0.89:
            print('B+')
    elif float(ans) >= 0.83:
        if float(ans) <= 0.86:
            print('B')
    elif float(ans) >= 0.80:
        if float(ans) <= 0.82:
            print('B-')
    elif float(ans) >= 0.76:
        if float(ans) <= 0.79:
            print('C+')
    elif float(ans) >= 0.73:
        if float(ans) <= 0.76:
            print('C')
    elif float(ans) >= 0.70:
        if float(ans) <= 0.72:
            print('C-')
    elif float(ans) >= 0.67:
        if float(ans) <= 0.69:
            print('D+')
    elif float(ans) >= 0.63:
        if float(ans) <= 0.66:
            print('D')
    elif float(ans) >= 0.60:
        if float(ans) <= 0.62:
            print('D-')
    elif float(ans) >= 0:
        if float(ans) <= 0.59:
            print('F')
            print('*Sadface*')
    elif float(ans) < 0: #checks for lower than 0 for snarky comment
        print("Not even sure how you can get a score this low")
    else:
        print('Unable to find letter value') #if this errors, or it can't catch the number value for some reason this is the error message
def runCalc():
    print('Version 2.1.0 Beta') #meaningless version code
    print('Current Functions:')
    funcdir() #prints the functions #ugh not camel case)
    print getFunction #request message #see variables designations below
    checkFunction()
    
'''
Graphing Function
'''
#Improtts
import turtle
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
    global barCount
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
        global barMax
        barCount += 1
        if barCount == barMax:
            print("Graph Full")
            break
    
        
def getConfig_onstart():
    global barMax
    global barWidth
    print("This is a basic graphing program.")
    print("This program uses Python Turtle Graphics")
    print("Please input your choice of settings as requested")
    barWidth_str = raw_input("Width of bars? (Micro, Small, Normal, Wide, XL) : ")
    if barWidth_str == "Micro":
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

'''
Extra Functions
'''
#from varLib import *
#from varLib import *                                                                                          #Example of commenting out extra snippets
#from Calc import runCalc
'''
Example of good commenting
'''
def showProjName(): #function for excessive displaying of the project name because why not 
    print projName
def printAppDir(): #same as above
    print directory
#Breaks
def br():
    print(' ') #breaks by one line
def timeBr():
    print(' ')
    time.sleep(1) #breaks by one line and system sleeps 1 second
def dotBr():
    print('...')
    time.sleep(1) #breaks by one line with ... filler and system sleeps 1 second
def userSelectApp(): #prints request dialogue
    print('Please Indicate The App You Would Like To Use') 
def openApp(): #sets the current app to the raw_input then runs the app
    currentApp = raw_input('>>>') 
    if currentApp == 'Calc': #checks for calc app
        run = True #that mystery variable that I'm too scared to comment out
        runCalc()
    elif currentApp == 'Info': #checks for info app
        showInfoApp()
    elif currentApp == 'Graph': #checks for graph app
        global columnTurtle
        global scaleTurtle
        global scaleCount
        wn = turtle.Screen() #that screen declaration
        columnTurtle = turtle.Turtle() #turtle in charge of creating columns
        scaleTurtle = turtle.Turtle() #turtle in charge of the scale
        scaleCount = 0
        main()
    else:
        print('Unable To Recognize Application - Cap-Sensitive') #error if you type an incorrect name or miss capitalization 
def showInfoApp(): #that readMe doe                              #ok maybe this should be under the lazy dev category
    print('This App aims to :')
    print(' ')
    print('    - Make everyday processes simpler')
    #print('    - Make your computer safer') 
    #print('    - Potentially Allow amateurs to practice and decrypt unique Stenography') 
    print('    - Act as a compendium for various works')
    #print('    - At some point find an appropriate definition for its acronym')
    print(' ')
    print(' ')
    print("Basically, this App's goal is to make tech filled lives easier and safer.")
    print('')
    print('This App is not :')
    print(' ')
    #print('    - An effective alternative to firewalls or antivirus software')
    print('    - Created to purposefully harm or tamper with your software')
    print('    - A perfect software bundle, and is under development')
    print(' ')
    print('This App is :')
    print(' ')
    print('    - A fun project that allows me to further my knowledge of software development')
    print('    - Open source, so feel free to spread your wings and hack away')
    print('    - Under development so expect bugs and irregular updates')
    print(' ')
    print(' ')
    print(' ')
    print(' ')

'''
Variables
'''
#Common Directory of Variables
projName = 'dunno, m8' #*shrugs*
'''
Examples of stuff you don't need to comment
'''
directory = ['Info, Calc, Graph']
currentApp = 'Unassigned'
ran = True
run = True
runIt = True
getFunction = 'Please input desired function'
getX = 'Please input the first numerical value'
getY = 'Please input the second numerical value'
ans = 'Null'
desFunction = 'Library Connection Error'

'''
Root
'''
while True: #This is the only active piece of the program
    time.sleep(2) #Spaces time between result and recursion
    printAppDir() #Prints directory of available application names. Must be typed exactly as shown.
    userSelectApp() #Prints request for choice
    openApp() #Collects raw_input and iterates apps #Uses if, elif for iteration. 