
class Clock:

    def __init__(self, hour, block = 0):
        self.__hour = hour
        self.__block = block

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__block * 5

    def next_block(self):
        if self.__block == 11:

            if self.__hour == 23:
                return Clock(0, 0)
            
            return Clock(self.__hour + 1, 0)

        return Clock(self.__hour, self.__block + 1)

    def str(self):
        return "{:02}:{:02}".format(self.hour(), self.minute())

    def block_range_str(self):
        return "{:02}:{:02}-{:02}:{:02}".format(self.hour(), self.minute(), self.hour(), self.minute() + 4)

    def __str__(self):
        return self.str()

