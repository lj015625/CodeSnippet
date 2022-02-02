"""Given a list of sorted integer lists, write a function sort_lists to create a combined list
while maintaining sorted order without importing any libraries or using the ‘sort’ or ‘sorted’ functions in Python."""

def sort_lists(lists_numbers):
    # use list of indexes where every element point to the index of a list where we stand now
    indexes = [0]*len(lists_numbers)
    end_flag = False
    sorted_list = []
    const_max_number = max([max(inner_list) for inner_list in lists_numbers])+1
    # using end flag to be true if all lists reaches their ends
    while not end_flag:
        end_flag = True
        min_index = 0
        min_number = const_max_number
        # loop through every list and compare elements using the indexes to chooses the minimum one
        for i in range(len(lists_numbers)):
            # if a list doesnt reach it's end then we aren't done yet
            if indexes[i] < len(lists_numbers[i]):
                end_flag = False
            else:
                continue

            #compare elements from diffrent lists
            if lists_numbers[i][indexes[i]] < min_number:
                min_number = lists_numbers[i][indexes[i]]
                min_index = i

        if not end_flag:
            sorted_list.append(min_number)
            indexes[min_index] += 1
    return sorted_list

lists = [
    [1,2,3,4,5,6],
    [2,5,7,8],
    [3,9,10,12],
    [0,1,2,8]
]
print(sort_lists(lists))
