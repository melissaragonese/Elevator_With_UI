from ellevator import Ellevator
from manage_queue import Queue

if __name__ == '__main__':
    q = Queue()
    e = Ellevator(max_floor=10, min_floor=1)

    e.status(q)
    e.accept_input(q)

    while len(q._get_queue().keys()) > 0:
        e.determine_direction(q)
        e.move()
        open = e.door_open(q)
        if open:
            e.accept_input(q)

        e.determine_direction(q)

        open = e.door_open(q)
        if open:
            e.accept_input(q)

    e.reset()
    e.status(q)
