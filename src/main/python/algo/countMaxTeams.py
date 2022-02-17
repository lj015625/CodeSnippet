
def countMaximumTeams(skill, teamSize, maxDiff):
    # find sublist in skill with size teamSize and maxDiff between skill in team
    if teamSize == 0 or maxDiff == 0:
        return 0

    high = max(skill)
    #print(high)
    low = min(skill)
    #print(low)

    # sort the skill first
    skill.sort()
    #print(skill)
    #print(teamSize)
    #print(maxDiff)

    team_count = 0
    current_size = 0
    # begin index and end index for a team skills
    beg = 0
    for i in range(len(skill)):
        current = skill[i]
        # if current is within the max range of skill then add it to current team
        if current <= (maxDiff + skill[beg]):
            current_size += 1
            #print(current_size)
            if current_size == teamSize:
                team_count += 1
                current_size = 0
                # reset beg index to the next
                beg = i+1
        # reset restart at current skill again
        else:
            current_size = 1
            beg = i

    return team_count

skill = [1, 3, 6, 9, 10, 22, 22, 23, 27, 29, 42, 49, 51, 58, 63, 68, 70, 95, 97, 98]
teamSize = 3
maxDiff = 12

print(countMaximumTeams(skill, teamSize, maxDiff))