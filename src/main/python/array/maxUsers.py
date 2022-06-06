import re

# O(h) + O(u) time complexity | O(h) space complexity
def maxHours(logs, numOfHours):
    # 1. parse the begin and end hours from the logs

    hours = [0] * numOfHours
    for log in logs:
        # or we could parse use JSON library
        array = log.split(' ')
        part1, part2, part3 = array[0], array[1], array[2]
        # user id is not used
        userId = int(re.search('(?<=userId:)\d', part1).group(0), 16)
        beginHour = int(re.search('(?<=begin:)\d', part2).group(0))
        endHour = int(re.search('(?<=end:)\d', part3).group(0))

    # 2. initialize array and increment on begin hour and decrement on end hour
        for i in range(beginHour, endHour):
            hours[i] += 1
        hours[i] -= 1

    # 3. find the max index hours
    # 0 represent hour 1 therefore +1
    return hours.index(max(hours)) + 1


logs = ["userId:1 begin:2 end:3",
        "userId:2 begin:3 end:5",
        "userId:3 begin:4 end:5"]

print(maxHours(logs, 48))
