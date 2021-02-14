#This is our graph variable
graph = {}
#get number of pages
pages = int(input())
#create a graph - our variable rep is the current page(node) and the input will be the pages
#leading from it
for rep in range(1, pages + 1):
    #initialize, get inputs
    m = list(map(int, input().split()))
    #check for ending page (special case)
    if 0 in m:
        graph[rep] = [0]
        continue
    #assign pages to parent page
    #note that this is a directed graph. In a non-directed graph, we would also add
    #the parent node to the nodes next to the subnode.
    #For example, graph[0].append(1) would have to be followed by graph[1].append(0)
    graph[rep] = m[1:]

#Start our breadth-first-search, with a queue containing page(node) 1:
queue = [1]
#Create the visited set.
#Sets are important since checking for element existence takes O(1) time
#in english, checking for an element's existence in a set is a lot faster than in a list.
visited = set()
visited.add(1)
#We don't want to search an ending page
visited.add(0)
#create variables for the depth, and our answer
depth = 0
ans = 0

#keep searching while the queue is full
while queue:
    #increase depth through each iteration of breadth first search
    depth += 1
    #copy the queue to create the next layer of bfs
    q2 = queue.copy()
    #clear the old queue
    #note that not using .copy() when copying arrays causes issues.
    queue = []
    #iterate through list of nodes
    for p in q2:
        #iterate through subnodes
        for page in graph[p]:
            #if the page is 0 (0==false), set ans to the current depth
            #note that due to the nature of our graph traversal, the first found path is always the shortest
            if not ans and page == 0:
                ans = depth
            #skip page processing if already been seen
            elif page not in visited:
                #add to queue and mark as seen
                queue.append(page)
                visited.add(page)

#print our stuff
print("Y" if all(elem in visited for elem in list(range(1, pages + 1))) else "N")
print(ans)
