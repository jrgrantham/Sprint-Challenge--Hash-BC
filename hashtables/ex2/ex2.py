#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # loop over tickets
    for ticket in tickets:
        # insert into hash table key=S, val=D
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    key = 'NONE'
    # loop over hash table to find next ticket
    for i in range(0, (length)):
        # retrieve S=none, D=val
        current = hash_table_retrieve(hashtable, key)
        # set S=val
        key = current
        # set route index
        route[i] = key
    return route[:-1]

    pass
