class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = (hour%12)*30+minutes*0.5
        b = minutes*6

        diff = abs(a- b)

        return min(diff, 360 - diff)