"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        
        intervals.sort(key=lambda i: i.start)

        print(intervals)
        for i in range(1, len(intervals)):
            last_meeting = intervals[i - 1]
            this_meeting = intervals[i]

            if last_meeting.end > this_meeting.start:
                return False
        
        return True
            
            