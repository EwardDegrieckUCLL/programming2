class Duration:
    def __init__(self, *, time_in_seconds):
        self.__time_in_seconds = time_in_seconds

    @property
    def seconds(self):
        return self.__time_in_seconds

    @property
    def minutes(self):
        return self.__time_in_seconds / 60

    @property
    def hours(self):
        return self.__time_in_seconds / 3600

    @staticmethod
    def from_seconds(time):
        return Duration(time_in_seconds=time)

    @staticmethod
    def from_minutes(time):
        return Duration(time_in_seconds=(time*60))

    @staticmethod
    def from_hours(time):
        return Duration(time_in_seconds=(time*3600))