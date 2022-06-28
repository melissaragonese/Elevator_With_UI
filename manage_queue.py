'''
Queue class to maintain queue from outside of the elevator
Moved Elevator queue outside of Elevator to possibly allow for multiple Elevators?
No idea how to deal with multiple Elevators.
'''
from collections import defaultdict

class Queue(object):
    def __init__(self):
        self.dests = defaultdict(list)

    def _get_queue(self):
        return self.dests

    def _add_to_queue(self, floor, direction):
        self.dests[int(floor)].append(direction.lower())
        return self.dests

    def _delete_from_queue(self, floor):
        del self.dests[int(floor)]
