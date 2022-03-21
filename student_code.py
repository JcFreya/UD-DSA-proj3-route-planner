import math # for calculating distance
from queue import PriorityQueue # for saving shortest path


# reference
# https://www.programcreek.com/python/?CodeExample=get+shortest+path
# https://wordaligned.org/articles/priority-queues-in-python

def shortest_path(M,start,goal):
    print("shortest path called")

    # create priority queue to save path
    path = PriorityQueue()
    path.put(start, 0)

    # keep the record of explored intersections and costs
    prev = {start: None}
    path_cost = {start: 0}

    while not path.empty():
        curr = path.get()

        # when hit the goal
        if curr == goal:
            getPath(prev, start, goal)

        # traverse all intersections that current intersection connects to
        for neighbor in M.roads[curr]:
            # get the cost from current intersection to it's neighbor
            new_cost = path_cost[curr] + heuristic(M.intersections[curr], M.intersections[neighbor])

            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost # update neighbor intersection's path cost
                total_cost = new_cost + heuristic(M.intersections[neighbor], M.intersections[goal]) # cost used for priority
                path.put(neighbor, total_cost) # make the move
                prev[neighbor] = curr

    return getPath(prev, start, goal)


# get the distance between two points
def heuristic(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))

# generate the path
def getPath(prev, start, goal):
    curr = goal
    path = [curr]
    # travers all intersections within the path
    while curr != start:
        curr = prev[curr]
        path.append(curr)

    # reorder the intersections for output format
    path.reverse()

    return path
