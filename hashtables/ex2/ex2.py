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
    # find the start looping through tickets
    for ticket in tickets:
        if ticket.source == "NONE":
            start = ticket.source
            next_stop = ticket.destination
            travel_cache[ticket.source] = ticket.destination


    # chain them to build the travel cache
    # while self.destination is not none
    # for length, append travel cache i - 1 to route

    print(travel_cache)
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
print(reconstruct_trip(tickets, len(tickets)))