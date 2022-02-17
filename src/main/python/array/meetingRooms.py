def minMeetingRooms(intervals):
    if not intervals:
        return 0

    used_rooms = 0
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])


    end_index = 0
    start_index = 0

    while start_index < len(intervals):
        # previous meeting has ended
        if end_times[end_index] <= start_times[start_index]:
            used_rooms -= 1
            end_index += 1

        # add a room
        used_rooms += 1
        start_index += 1

    return used_rooms

print (minMeetingRooms([[0,30],[5,10],[15,20]]))