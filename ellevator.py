from accept_input import AcceptInput

door_string = 'DOORS OPENING ON FLOOR {}'
moving_string = '...Moving {} to floor {}...'
dir_num_2_str = {
    1: 'up',
    0: 'exit',
    -1: 'down'
}


class Ellevator(object):

    def __init__(self, max_floor, min_floor):

        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        self.dir = 1

    def determine_direction(self, queue):
        dests = queue._get_queue()

        if len(dests.keys()) == 0:
            self.dir = -1
        elif max(dests.keys()) > self.current_floor and self.dir == 1:
            self.dir = 1
        elif min(dests.keys()) < self.current_floor and self.dir == -1:
            self.dir = -1
        elif min(dests.keys()) >= self.current_floor and self.dir == -1:
            self.dir = 1
        elif min(dests.keys()) <= self.current_floor and self.dir == 1:
            self.dir = -1

    def door_open(self, queue):
        dests = queue._get_queue()
        cf = self.current_floor
        d = self.dir

        #switched to 1, -1, 0 and accounted for sad two direction abandonment (same floor, up/down both pressed)
        if (cf in dests and d in dests[cf] and -d in dests[cf]):
            queue._delete_from_queue(cf)
            queue._add_to_queue(cf, -d)
            print(door_string.format(cf))
            self.status(queue)
            return True
        elif (cf in dests and d in dests[cf]) | (cf in dests and 0 in dests[cf]):
            queue._delete_from_queue(cf)
            print(door_string.format(cf))
            self.status(queue)
            return True
        else:
            return False

    def move(self):
        if self.dir == 1 and self.current_floor != self.max_floor:
            print(moving_string.format(dir_num_2_str[self.dir], self.current_floor + 1))
            self.current_floor += 1
        else:
            print(moving_string.format(dir_num_2_str[self.dir], self.current_floor - 1))
            self.current_floor -= 1

    def reset(self):
        self.current_floor = self.min_floor
        self.dir = 1
        print('Elevator Reset.')

    def status(self, queue):
        dests = queue._get_queue()
        print('STATUS')
        print(' Direction: {}'.format(dir_num_2_str[self.dir]))
        print(' Current Floor: {}'.format(self.current_floor))
        print(' Elevator Current Queue: ')
        print(dests)

    def accept_input(self, queue):
        s = AcceptInput(floor=self.current_floor,
                        direction=self.dir,
                        max_floor=self.max_floor,
                        min_floor=self.min_floor,
                        queue=queue)

