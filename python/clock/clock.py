class Clock:
    def __init__(self, hour, minute):
        total_min = (hour * 60) + minute
        self.__hour, self.__minute = self.__extract_hour_min(total_min)

    def __repr__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return (self.__hour == other.__hour) and (self.__minute == other.__minute)
        return False

    def __add__(self, minutes):
        return Clock(self.__hour, self.__minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.__hour, self.__minute - minutes)

    def __extract_hour_min(self, minutes):
        m = minutes % 60  # Split hours
        h = minutes // 60 # Split the minutes left over
        h = h % 24        # Wrap to 24 hour clock
        return h, m