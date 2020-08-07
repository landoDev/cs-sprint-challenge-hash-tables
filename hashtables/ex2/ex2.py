#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source # starting place
        self.destination = destination # ending place


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Understand
    # need to find the ordered path of my destination
    # my final flight has a destination of None
    # return the list "route" with the ordered sources and destinations
    # starting location is the key and the destination is the value
    # when constructing the route, the ith location can be found by checking the hash table for i-1th location

    # intialize the travel cache
    travel_cache = {}
    route = []
    print(route)
    start = [ticket for ticket in tickets if ticket.source == "NONE"]
    # find the start looping through tickets
    for ticket in tickets:
        travel_cache[ticket.source] = ticket.destination
    # for i in range(length):
    #     route[i] = travel_cache[i - 1]
    # print(len(travel_cache), length)
    while True:
        if len(route) == length:
            break
        for ticket in travel_cache:
            print(travel_cache[ticket])
            if ticket == "NONE":
                route.append(travel_cache[ticket])
            elif route[-1] == ticket:
                route.append(travel_cache[ticket])
            else:
                print("why")

    # chain them to build the travel cache
    # for length, append travel cache i - 1 to route
    
    # print(travel_cache)
    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, len(tickets)))

