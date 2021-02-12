# You may create additional functions here:
import random

print('welcome to Minesweepers')

# Implement your Minesweeper Solution Below:

def play(dim_size, num_bombs):
#this is what will place the bombs in random locations  
    #this will determine which row (r) and column (c) to place the bomb randomly
    # 
    def placebomb(b):
        r = random.randint(0, 9)
        c = random.randint(0, 9)

    currentRow = b[r]
    if not currentRow[c] == '*':
        currentRow[c] = '*'
    else:
        placebomb(b)
#the b is fo bombs and this is a 2 dismensional = array
b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for n in range (0,10):
    placeBomb(b)


for r in range (0,9):
    for c in range (0,9):
        value = 1 : int(r, c, b)
        if value == '*':
            pass
        'updateValues'(r, c, b)



#Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
     , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
     , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
     , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
     , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


'printBoard'(k)

#Start timer
startTime = time.time()

'play'(b, k, startTime)

#Gets the value of a coordinate on the grid.
def l (r, c, b):
    return b [r] [c]



#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 10 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 10 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 10 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 10 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

def zeroProcedure(r, c, k, b):

    #Row above
    if r-1 > -1:
        row = k[r-1]
        if c-1 > -1: row[c-1] = l(r-1, c-1, b)
        row[c] = l(r-1, c, b)
        if 10 > c+1: row[c+1] = l(r-1, c+1, b)

    #Same row
    row = k[r]
    if c-1 > -1: row[c-1] = l(r, c-1, b)
    if 10 > c+1: row[c+1] = l(r, c+1, b)

    #Row below
    if 10 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = l(r+1, c-1, b)
        row[c] = l(r+1, c, b)
        if 10 > c+1: row[c+1] = l(r+1, c+1, b)

#Checks known grid for 0s.
def checkZeros(k, b, r, c):
    oldGrid = copy.deepcopy(k)
    zeroProcedure(r, c, k, b)
    if oldGrid == k:
        return
    while True:
        oldGrid = copy.deepcopy(k)
        for x in range (10):
            for y in range (10):
                if l(x, y, k) == 0:
                    zeroProcedure(x, y, k, b)
        if oldGrid == k:
            return


#Places a marker in the given location.
def marker(r, c, k):
    k[r][c] = '⚐'
    printBoard(k)


#this is what will print the playing board
def printBoard(b):
    'clear'()
    print()
    print('    A   B   C   D   E   F   G   H   I   J')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')

for r in range (0, 9):
    print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║',l(r,9,b),'║')
    if not r == 8:
        print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')


#The player chooses a location.
def choose(b, k, startTime):
    #Variables 'n stuff.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i', 'j']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #Loop in case of invalid entry.
    while True:
        chosen = input('Please choose a square (eg. D1) or place a marker (eg. mD4): ').lower()
        #Checks for valid square.
        if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
            c, r = (ord(chosen[1]))-97, int(chosen[2])
            marker(r, c, k)
            play(b, k, startTime)
            break
        elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers: return (ord(chosen[0]))-97, int(chosen[1])
        else: choose(b, k, startTime)         



#play Function Ends Here


if __name__=='__main__':
    play()
    