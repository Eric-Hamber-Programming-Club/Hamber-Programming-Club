#remember this?
from collections import deque
#This code was written around a year ago, so cut me some slack :b

#flooring available, rows, columns
f, r, c = (int(input()) for i in range(3))
#A map to change a character to either 0 or 1 for easier parsing
charmap = {"I": 0, ".": 1}
#get the floor plan and turn it into our 2d list
plan = [[charmap[x] for x in input()] for y in range(r)]
#searched set
searched = set()
#This will store room sizes
rooms = []

def adjac(point) -> list:
    ''' returns a list of all adjacent coordinates'''
    #unpacking: a statement suck as a, b = [x, y] is the same as a=x and b=y
    x, y = point
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

#MATRICES ARE NOT COORDINATE PLANES! To avoid getting confused between x/y, use rows and columns when referring to graphs
#general tip: use rows and columns always when working with 2d lists (provided they are rectangular)
#loop through every cell
for row in range(r):
    for col in range(c):
        #get our coords
        coords = (col, row)
        #extra important to not doublesearch a cell here, as we will see soon
        if coords in searched:
            continue
        #mark them as searched
        searched.add(coords)
        #get our tile data
        unit = plan[col][row]
        #room search algorithm
        #this will output the size of a room provided any tile in that room
        #we preform this if we have an unvisited floor tile
        if unit:
            #make a bfs queue
            queue = deque()
            queue.append(coords)
            #this stores the size of the room
            room_n = 1
            #bfs loop
            while queue:
                #get the first queue element
                p = queue.popleft()
                #check adjacent cells
                for point in adjac(p):
                    #if it's already seen, we don't care lol
                    if point in searched:
                        continue
                    b, a = point
                    #this is to make sure our coords are not outside our grid (index error)
                    if not (r>b>=0 and c>a>=0):
                        continue
                    #check if tile is wall or floor
                    status = plan[b][a]
                    #mark as seen
                    searched.add(point)
                    #if floor, increase size and add it to the queue
                    #this is so we can search its neighbors later
                    #you can think of this algorithm as a sort of "disease" search that stops when it is enclosed by walls
                    if status:
                        room_n += 1
                        queue.append(point)
            #we add the roomsize to the list of room sizes
            rooms.append(room_n)
#we sort the room sizes in descending order
rooms = sorted(rooms, reverse=True)
#this is basically a flag due to input wackiness
possible_n = 0
#find how many rooms we can completely floor (starting from the largest)
for r in rooms:
    f -= r
    if f < 0:
        f += r
        break
    possible_n += 1
#output
if possible_n == 1:
    print("1 room, {} square metre(s) left over".format(f))
else:
    print("{} rooms, {} square metre(s) left over".format(possible_n, f))
