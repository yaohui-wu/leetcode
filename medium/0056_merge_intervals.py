class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if length == 0 or length == 1:
            return intervals
        # Sort the intervals by the start of each interval.
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]
        for interval in intervals:
            # Combine the intervals if they overlap.
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        return merged
