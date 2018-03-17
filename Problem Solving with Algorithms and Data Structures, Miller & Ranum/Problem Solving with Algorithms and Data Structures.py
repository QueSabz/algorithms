
# coding: utf-8

# # 1.12 Infinite Monkey Theorem
# 
# Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
# 
# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.
# 
# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string. To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1,000 tries.

# In[1]:


import string
import random

alphabet = string.ascii_lowercase + ' '

def generate(strlength):
    return ''.join(random.choices(alphabet, k = strlength))

def score(string, answer):
    return sum([1 for i in range(len(string)) if string[i] == answer[i]])

def trials(n, answer):
    best_score = 0
    best_string = ''
    for i in range(n):
        new_string = generate(len(answer))
        new_score = score(new_string, answer)
        if new_score > best_score:
            best_score = new_score
            best_string = new_string
        if (i % 1000) == 0:
            print(best_score, best_string)
            
trials(10000, "methinks it is like a weasel")


# See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.

# In[2]:


def better_generate(answer):
    string = generate(len(answer))
    count = 0
    for i in range(len(answer)):
        while string[i] != answer[i]:
            list_string = list(string)
            list_string[i] = generate(1)
            string = ''.join(list_string)
            count += 1
    return string, answer, count

better_generate("methinks it is like a weasel")


# # 1.13 Fractions
# 
# To make sure you understand how operators are implemented in Python classes, and how to properly write methods, write some methods to implement *, /, and - . Also implement comparison operators > and <

# In[3]:


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)
        
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum,newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def __mul__(self, other):
        newnum = self.num * other.num 
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    def __truediv__(self, other):
        return Fraction.__mul__(self, Fraction(other.den, other.num))
    
    def __sub__(self, other):
        return Fraction.__add__(self, Fraction(-other.num, other.den))
    
    def __gt__(self, other):
        return Fraction.__sub__(self, other).num > 0
    
    def __lt__(self, other):
        return Fraction.__sub__(self, other).num < 0
    
x = Fraction(1,2)
y = Fraction(2,3)
print(x + y)
print(x == y)
print(x * y)
print(x / y)
print(x - y)
print(x > y)
print(x < y)


# # 1.13 Logic Gates and Circuits
# 
# Create a two new gate classes, one called NorGate the other called NandGate. NandGates work like AndGates that have a Not attached to the output. NorGates work lake OrGates that have a Not attached to the output.
# 
# Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D). Make sure to use some of your new gates in the simulation.

# In[4]:


class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    
class NandGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        andgate = AndGate(self.name)
        notgate = NotGate(self.name)
        Connector(andgate, notgate)
        return notgate.performGateLogic()
    
class NorGate(BinaryGate):
    
    def __init__(self,n):
        BinaryGate.__init__(self,n)
        
    def performGateLogic(self):
        orgate = OrGate(self.name)
        notgate = NotGate(self.name)
        Connector(orgate, notgate)
        return notgate.performGateLogic()

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())
    
    g1 = NandGate("G1")
    g2 = NandGate("G2")
    g3 = AndGate("G3")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    print(g3.getOutput())

main()


# # 2.3 Minimum Number in a List
# 
# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list `O(n^2)`. The second function should be linear `O(n)`.

# In[5]:


def minimum_n2(seq):
    minimum = seq[0]
    for s in seq:
        for t in seq:
            if s <= t:
                pass
            else:
                break
            minimum = s
    return minimum

def minimum_n(seq):
    minimum = seq[0]
    for s in seq:
        if s <= minimum:
            minimum = s
    return minimum

x = [1,2,3,4,5,0,12,-1,-2,-3]
print(minimum_n2(x))
print(minimum_n(x))


# # 2.11 List Indexing
# 
# Devise an experiment to verify that the list index operator is `O(1)`.

# In[6]:


import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

y = []
x = range(10000, 1000001, 20000)
for xx in x:
    seq = list(range(xx))
    t = timeit.Timer("seq[random.randrange(%d)]" %xx, "from __main__ import random, seq")
    time = t.timeit(number=1000)
    y.append(time)

plt.scatter(x, y)
plt.show()


# # 3.5 Stacks and String Reversal
# 
# Write a function `revstring(mystr)` that uses a stack to reverse the characters in a string.

# In[7]:


class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
def revstring(mystr):
    m = Stack()
    revstr = ''
    for s in mystr:
        m.push(s)
    while not m.isEmpty():
        revstr += m.pop()
    return revstr

revstring('apple')


# # 3.9 General Infix-to-Postfix Conversion¶
# 
# Modify the `infixToPostfix` function so that it can convert the following expression: `5 * 3 ** (4 - 2)`. Modify the infix-to-postfix algorithm so that it can handle errors

# In[8]:


def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in prec.keys():
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        else:
            raise ValueError("Input contains an invalid token")

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))
# print(infixToPostfix("5 * 3 *** ( 4 - 2 )"))


# # 3.9 Postfix Evaluation
# 
# Modify the postfix evaluation algorithm so that it can handle errors

# In[9]:


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token in "+-/*":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
        else:
            raise ValueError("Input contains an invalid token")
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    else:
        raise ValueError("Input contains an invalid operator")
    
print(postfixEval('7 8 + 3 2 + /'))
# print(postfixEval('7 8 + 3 2 + //'))


# # 3.11 Queue ADT
# 
# Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list. Design and implement an experiment to do benchmark comparisons of the two queue implementations. What can you learn from such an experiment?

# In[10]:


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class QueueList:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        self.items.pop()
        
    def size(self):
        return len(self.items)

y1 = []
y2 = []
x = range(1, 102001, 2000)
fastQueue = QueueList()
slowQueue = Queue()

for experiment in x:
    for loop in range(max(0, experiment - 2000), experiment):
        fastQueue.enqueue(loop)
        slowQueue.enqueue(loop)       
    timer1 = timeit.Timer("fastQueue.enqueue(random.randrange(%d))" %experiment, "from __main__ import random, fastQueue")
    timer2 = timeit.Timer("slowQueue.enqueue(random.randrange(%d))" %experiment, "from __main__ import random, slowQueue")
    t1 = timer1.timeit(number=1000)
    t2 = timer2.timeit(number=1000)
    y1.append(t1)
    y2.append(t2)

plt.scatter(x, y1, label="Fast Queue")
plt.scatter(x, y2, label="Slow Queue")
plt.legend()
plt.show()


# # 3.14 Printer Queue Simulation
# 
# How would you modify the printer simulation to reflect a larger number of students? Suppose that the number of students was doubled. You make need to make some reasonable assumptions about how this simulation was put together but what would you change? Modify the code. 
# 
# Also, suppose that the length of the average print task was cut in half. Change the code to reflect that change. Finally, how would you parametertize the number of students? Rather than changing the code we would like to make the number of students a parameter of the simulation.

# In[11]:


import random
    
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate
        
class Task:
    def __init__(self, time, averagePageLength):
        self.timestamp = time
        self.pages = random.randrange(1, averagePageLength + 1)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
def simulation(numSeconds, pagesPerMinute, students, averagePageLength):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask(students):
            task = Task(currentSecond, averagePageLength)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
      
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))


def newPrintTask(students):
    tasksPerStudent = 2
    secondsPerTask = 3600 / (students * tasksPerStudent)
    num = random.randrange(1, 180 + 1)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5, 10, 10)


# # 3.17 Deque

# In[12]:


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# # 3.21 Implementing an Unordered List: Linked Lists
# 
# Part I: Implement the append method for UnorderedList. What is the time complexity of the method you created?
# 
# Part II: In the previous problem, you most likely created an append method that was `O(n)`. If you add an instance variable to the UnorderedList class you can create an append method that is `O(1)`. Modify your append method to be `O(1)`. Be careful! To really do this correctly you will need to consider a couple of special cases that may require you to make a modification to the add method as well.

# In[13]:


class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self,item):
        current = self.head
        stop = False
        while not stop:
            if current == None or current.getNext() == None:
                stop = True
            else:
                current = current.getNext()
        
        temp = Node(item)
        if current == None:
            self.head = temp
        else:
            current.setNext(temp)
            
mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

mylist = UnorderedList()
mylist.append(1)
mylist.append(2)
print(mylist.search(1))
print(mylist.head.getData())
mylist.remove(1)
print(mylist.search(1))
print(mylist.search(2))
print(mylist.head.getData())
mylist.add(1)
print(mylist.search(1))
print(mylist.head.getData())


# # 4.5 String Reversal and Palindromes
# 
# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string. Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. For example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. for example: madam i’m adam is a palindrome.

# In[14]:


import string
def stringReversal(string):
    return ''.join(list(string)[::-1])

print(stringReversal("kayak"))
print(stringReversal("palindrome"))

def palindrome(sample):
    translator = str.maketrans('', '', string.punctuation)
    newSample = ''.join([ss for s in sample.translate(translator).split(' ') for ss in list(s)]).lower()
    return newSample == stringReversal(newSample)

print(palindrome("Reviled did I live, said I, as evil I did deliver"))
print(palindrome("Able was I ere I saw Elba"))
print(palindrome("madam i'm adam"))


# # 4.7 Draw Fractal Tree with Turtle
# 
# Modify the recursive tree program using one or all of the following ideas:
# 
# * Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
# * Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
# * Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
# * Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

# In[15]:


import turtle
import random

min_color = 5
max_color = 255
angle = random.randrange(10, 50, 10)
length = random.randrange(10, 50, 10)

def tree(branchLen,t):
    if branchLen > 5:
        t.pensize(branchLen / 10)
        green = round((max_color - min_color) / (branchLen / 10))
        t.color((0, green, 0))
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - length,t)
        t.left(2 * angle)
        tree(branchLen - length,t)
        t.right(angle)
        t.backward(branchLen)
        green = round((max_color - min_color) / ((branchLen + 15) / 10))
        t.color((0, green, 0))

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.colormode(255)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(100,t)
    myWin.exitonclick()

# main()


# # 4.10 Tower of Hanoi
# 
# Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.

# In[16]:


class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
    
moveTower(3,"A","B","C")


# # 4.11 Exploring a Maze
# 
# Modify the maze search program so that the calls to searchFrom are in a different order. Watch the program run. Can you explain why the behavior is different? Can you predict what path the turtle will follow for a given change in order?

# In[17]:


PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
    # try each of four directions from this point until we find a way out.
    # base Case return values:
    #  1. We have run into an obstacle, return false
    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or             searchFrom(maze, startRow, startColumn-1) or             searchFrom(maze, startRow+1, startColumn) or             searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

myMaze = Maze('maze2.txt')
# myMaze.drawMaze()
# myMaze.updatePosition(myMaze.startRow,myMaze.startCol)
# searchFrom(myMaze, myMaze.startRow, myMaze.startCol)


# # 4.12 Dynamic Programming
# 
# Using the dynamic programming algorithm for making change, find the smallest number of coins that you can use to make 33 cents in change. In addition to the usual coins assume that you have an 8 cent coin.

# In[18]:


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
        
def main():
    amnt = 33
    clist = [1,5,8,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()


# # 4.17 Factorial
# 
# Write a recursive function to compute the factorial of a number.

# In[19]:


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(0))


# # 4.17 Reverse a List
# 
# Write a recursive function to reverse a list.

# In[20]:


def reverseList(l):
    if len(l) <= 1:
        return l
    else:
        return [l[len(l)-1]] + reverseList(l[:len(l)-1])
        
reverseList([1,2,3,4,5,6])


# # 5.4 Binary Search
# 
# One additional analysis issue needs to be addressed. In the recursive solution, the recursive call, `binarySearch(alist[:midpoint],item)` uses the slice operator to create the left half of the list that is then passed to the next invocation (similarly for the right half as well). The analysis that we did assumed that the slice operator takes constant time. However, we know that the slice operator in Python is actually `O(k)`. This means that the binary search using slice will not perform in strict logarithmic time. Luckily this can be remedied by passing the list along with the starting and ending indices. The indices can be calculated as we did in Listing 3. We leave this implementation as an exercise.

# In[21]:


def binarySearch(alist, item, first, last):
    if len(alist) == 0 or first == last:
        return False
    else:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist, item, first, midpoint - 1)
            else:
                return binarySearch(alist, item, midpoint + 1, last)
            
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3, 0, len(testlist) - 1))
print(binarySearch(testlist, 40, 0, len(testlist) - 1))
print(binarySearch(testlist, 13, 0, len(testlist) - 1))


# # 5.5 Hashing
# 
# It is interesting to note that when using this hash function, anagrams will always be given the same hash value. To remedy this, we could use the position of the character as a weight. The modification to the hash function is left as an exercise.

# In[22]:


def hash(astring, tablesize):
    result = 0
    index = 1
    for pos in range(len(astring)):
        result += ord(astring[pos]) * index
        index += 1

    return result % tablesize

hash("cat", 11)


# # 5.5 Hash Table
# 
# The final methods of the HashTable class provide additional dictionary functionality. We overload the `__getitem__` and `__setitem__` methods to allow access using `[]`. This means that once a HashTable has been created, the familiar index operator will be available. We leave the remaining methods as exercises.

# In[23]:


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
        
    def __delitem__(self,key):
        self.put(key,None)
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == key:
            self.slots[hashvalue] = None
        else:
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
            self.slots[nextslot] = None
        
            
    def __len__(self):
        return self.size
    
    def __contains__(self,key):
        return self.get(key) != None     
        
    
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20] = 'duck'
print(H[20])
print(H.data)
print(H[99])
print(len(H))
print(20 in H)
del H[20]
print(H[20])
print(H.slots)
print(H.data)


# # 5.11 The Merge Sort
# 
# Recall that the slicing operator is `O(k)` where k is the size of the slice. In order to guarantee that `mergeSort` will be `O(nlogn)` we will need to remove the slice operator. Again, this is possible if we simply pass the starting and ending indices along with the list when we make the recursive call. We leave this as an exercise.

# In[24]:


def mergeSort(alist, start, end):
    if start < end:
        mid = (start + end - 1) // 2
        mergeSort(alist, start, mid)
        mergeSort(alist, mid + 1, end)

        i, j, k = 0, 0, start        
        
        n1 = mid - start + 1
        n2 = end - mid
        
        L = [alist[start + l] for l in range(n1)]
        R = [alist[mid + r + 1] for r in range(n2)]
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                alist[k] = L[i]
                i += 1
            else:
                alist[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            alist[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            alist[k] = R[j]
            j += 1
            k += 1
            
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist, 0, len(alist) - 1)
print(alist)


# # 5.12 The Quick Sort
# 
# We mentioned earlier that there are different ways to choose the pivot value. In particular, we can attempt to alleviate some of the potential for an uneven division by using a technique called median of three. To choose the pivot value, we will consider the first, the middle, and the last element in the list. In our example, those are 54, 77, and 20. Now pick the median value, in our case 54, and use it for the pivot value (of course, that was the pivot value we used originally). The idea is that in the case where the the first item in the list does not belong toward the middle of the list, the median of three will choose a better “middle” value. This will be particularly useful when the original list is somewhat sorted to begin with. We leave the implementation of this pivot value selection as an exercise.

# In[25]:


import statistics
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = statistics.median([alist[first], alist[(last - first) // 2], alist[last]])
    leftmark = first + 1
    rightmark = last
    
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


# # 6.4 List of Lists Representation
# 
# Write a function `buildTree` that returns a tree using the list of lists functions.

# In[26]:


def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def buildTree():
    t = BinaryTree("a")
    insertLeft(t, "b")
    insertRight(t, "c")
    l = getLeftChild(t)
    r = getRightChild(t)
    insertRight(l, "d")
    insertLeft(r, "e")
    insertRight(r, "f")
    print(t)
    
buildTree()


# # 6.5 Nodes and References
# 
# Write a function `buildTree` that returns a tree using the nodes and references implementation. 

# In[27]:


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def buildTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    l = t.getLeftChild()
    r = t.getRightChild()
    l.insertRight('d')
    r.insertLeft('e')
    r.insertRight('f')
    print(t.getRootVal())
    print(t.getLeftChild().getRootVal())
    print(t.getRightChild().getRootVal())
    print(t.getLeftChild().getRightChild().getRootVal())
    print(t.getRightChild().getLeftChild().getRootVal())
    print(t.getRightChild().getRightChild().getRootVal())
    
buildTree()


# # 6.13 Search Tree Implementation

# In[28]:


class TreeNode:
    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent = currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                  return res.payload
            else:
                  return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
                    
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
print(mytree[6])
print(mytree[2])


# # 7.6 Graph Implementation

# In[29]:


class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
g = Graph()
for i in range(6):
    g.addVertex(i)
    
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

