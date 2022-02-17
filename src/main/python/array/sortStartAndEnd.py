"""Consider a trip from one city to another that may contain many layovers.
Given the list of flights out of order, each with a starting city and end city,
write a function plan_trip to reconstruct the path of the trip so the trip tickets are in order."""


from collections import defaultdict

def plan_trip(flights):
    starts = []
    ends = []
    myMap = defaultdict()
    for flight in flights:
        starts.append(flight[0])
        ends.append(flight[1])
        myMap[flight[0]] = flight[1]

    beg = None
    for flight in flights:
        if flight[0] not in ends:
            beg = flight[0]

    sortedFlights = []
    while len(myMap) > 0:
        end = myMap[beg]
        myMap.pop(beg)
        sortedFlights.append([beg, end])
        #swap begin and end
        beg = end

    return sortedFlights


flights = [
    ['Chennai', 'Bangalore'],
    ['Bombay', 'Delhi'],
    ['Goa', 'Chennai'],
    ['Delhi', 'Goa'],
    ['Bangalore', 'Beijing']
]
print(plan_trip(flights))
# output = [
#     ['Bombay', 'Delhi'],
#     ['Delhi', 'Goa'],
#     ['Goa', 'Chennai'],
#     ['Chennai', 'Bangalore'],
#     ['Bangalore', 'Beijing'],
# ]