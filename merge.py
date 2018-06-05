# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        start_dict = {}
        for i in range(len(intervals)):
            start_dict[(intervals[i].start, intervals[i].end)] = i
        new_intervals = []
        for key in sorted(start_dict.keys()):
            new_intervals.append(intervals[start_dict[key]])

        while i < len(new_intervals)-1:
            if new_intervals[i].end >= new_intervals[i + 1].start:
                new_intervals[i + 1].start = new_intervals[i].start
                new_intervals[i + 1].end = max(new_intervals[i].end, new_intervals[i + 1].end)
                new_intervals[i] = Interval(-1,-1)
        result = []
        for i in new_intervals:
            if i.start>0:
                result.append(i)
        return result


u = Solution()
interval1 = Interval(0,2)
interval2 = Interval(0,5)
interval3 = Interval(1,6)
test = [
[interval1,interval2,interval3]


]


for x in test:
    print(u.merge(x))


