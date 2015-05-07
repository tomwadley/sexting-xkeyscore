from functools import total_ordering

@total_ordering
class Clock:

    def __init__(self, hour, block = 0, day = 0):
        self._hour = hour
        self._block = block
        self._day = day

    def hour(self):
        return self._hour

    def minute(self):
        return self._block * 5

    def day(self):
        return self._day

    def next_block(self):
        if self._block == 11:

            if self._hour == 23:
                return Clock(0, 0, self._day + 1)
            
            return Clock(self._hour + 1, 0, self._day)

        return Clock(self._hour, self._block + 1, self._day)

    def jump_forward(self, blocks):
        return reduce(lambda c, _: c.next_block(), range(blocks), self)

    def str(self):
        return "{:02}:{:02}".format(self.hour(), self.minute())

    def block_range_str(self):
        return "{:02}:{:02}-{:02}:{:02}".format(self.hour(), self.minute(), self.hour(), self.minute() + 4)

    def __str__(self):
        return self.str()

    def __eq__(self, other):
        return (self._hour == other._hour) and (self._block == other._block) and (self._day == other._day)

    def __lt__(self, other):
        if not self._day == other._day:
            return self._day < other._day
        if not self._hour == other._hour:
            return self._hour < other._hour
        return self._block < other._block

