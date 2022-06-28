from accept_input import AcceptInput

door_string = 'DOORS OPENING ON FLOOR {}'
moving_string = '...Moving {} to floor {}...'


class Ellevator(object):

    def __init__(self, max_floor, min_floor):

        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        self.dir = 'up'

    def determine_direction(self, queue):
        dests = queue._get_queue()

        if len(dests.keys()) == 0:
            self.dir = 'down'
        elif max(dests.keys()) > self.current_floor and self.dir == 'up':
            self.dir = 'up'
        elif min(dests.keys()) < self.current_floor and self.dir == 'down':
            self.dir = 'down'
        elif min(dests.keys()) >= self.current_floor and self.dir == 'down':
            self.dir = 'up'
        elif min(dests.keys()) <= self.current_floor and self.dir == 'up':
            self.dir = 'down'

    def door_open(self, queue):
        dests = queue._get_queue()

        if (self.current_floor in dests and self.dir in dests[self.current_floor]) | \
                (self.current_floor in dests and 'exit' in dests[self.current_floor]):
            queue._delete_from_queue(self.current_floor)
            print(door_string.format(self.current_floor))
            self.status(queue)
            return True
        else:
            return False

    def move(self):
        if self.dir == 'up' and self.current_floor != self.max_floor:
            print(moving_string.format(self.dir, self.current_floor + 1))
            self.current_floor += 1
        else:
            print(moving_string.format(self.dir, self.current_floor - 1))
            self.current_floor -= 1

    def reset(self):
        self.current_floor = self.min_floor
        self.dir = 'up'
        print('Elevator Reset.')

    def status(self, queue):
        dests = queue._get_queue()
        print('STATUS')
        print(' Direction: {}'.format(self.dir))
        print(' Current Floor: {}'.format(self.current_floor))
        print(' Elevator Current Queue: ')
        print(dests)

    def accept_input(self, queue):
        s = AcceptInput(floor=self.current_floor,
                        direction=self.dir,
                        max_floor=self.max_floor,
                        min_floor=self.min_floor,
                        queue=queue)

