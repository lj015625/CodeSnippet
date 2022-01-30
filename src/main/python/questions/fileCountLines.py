# Python program to count the
# number of lines in a text file
def count_lines(file_path):
    file = open(file_path, "r")
    count = 0

    # Reading from file
    content = file.read()
    contentList = content.split("\n")
    for i in contentList:
        if i:
            count += 1

    return count
