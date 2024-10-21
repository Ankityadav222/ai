import queue as Q
from dictinary3 import dict_hn
from dictinary3 import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''


# Calculate f(n) = g(n) + h(n)
def get_fn(citystr):
    cities = citystr.split(',')
    gn = 0
    for ctr in range(0, len(cities) - 1):
        gn += dict_gn[cities[ctr]][cities[ctr + 1]]  # g(n): Cost from city to city
    hn = dict_hn[cities[-1]]  # h(n): Heuristic cost for the last city
    return hn + gn


# Print the contents of the priority queue
def printout(cityq):
    for i in range(cityq.qsize()):
        print(cityq.queue[i])


# Expand nodes and explore the next cities
def expand(cityq):
    global result
    if cityq.empty():
        return  # Stop if queue is empty

    tot, citystr, thiscity = cityq.get()

    if thiscity == goal:  # Check if we've reached the goal
        result = citystr + ' :: ' + str(tot)
        return

    print("Expanded city:", thiscity)

    # Expand the current city and add neighboring cities to the queue
    for neighbor in dict_gn[thiscity]:
        new_citystr = citystr + ',' + neighbor
        cityq.put((get_fn(new_citystr), new_citystr, neighbor))

    printout(cityq)
    expand(cityq)  # Recursively expand the next city in the priority queue


def main():
    cityq = Q.PriorityQueue()
    thiscity = start

    # Start with the first city (Arad)
    cityq.put((get_fn(start), start, thiscity))
    expand(cityq)

    if result:
        print("Result:", result)
    else:
        print("No path found to the goal.")


main()
