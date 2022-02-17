"""Say you are given a list of tuples where
the first element is the slope of a line and the second element is the y-intercept of a line.
Write a function find_intersecting to find which lines, if any, intersect with any of the others in the given x_range.
"""

def find_intersecting_lines(list_lines, range_x):
    output = []
    for i in range(len(list_lines)):
        for j in range(i+1, len(list_lines)):
            m1, c1 = list_lines[i]
            m2, c2 = list_lines[j]
            try:
                x = (-1*(c1 - c2))/(m1-m2)
                if x <= range_x[1] and x >= range_x[0]:
                    if list_lines[i] not in output:
                        output.append(list_lines[i])
                    if list_lines[j] not in output:
                        output.append(list_lines[j])
            except:
                continue
    return output


tuple_list = [(2, 3), (-3, 5), (4, 6), (5, 7)]
x_range = (0, 1)
print(find_intersecting_lines(tuple_list, x_range))
