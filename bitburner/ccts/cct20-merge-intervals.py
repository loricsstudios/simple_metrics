def merge_intervals(intervals):
    # If there are no intervals, return an empty list
    if not intervals:
        return []

    # Step 1: Sort the intervals by the start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize the list to hold merged intervals
    merged = []

    for interval in intervals:
        # If merged is empty or if the current interval does not overlap with the previous one, add it to merged
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is overlap, so merge the current interval with the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Given intervals
# intervals = [[16,19],[8,13],[14,24],[9,17],[4,6],[7,12],[2,10],[4,12],[7,14],[4,8],[16,20]]
intervals =  [[19,27],[7,11],[1,5],[8,10],[23,31]]

# Get merged intervals
merged_intervals = merge_intervals(intervals)
print(merged_intervals)
