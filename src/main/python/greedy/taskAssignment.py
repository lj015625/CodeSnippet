"""
Given an integer k is number of workers, and an integer task array represent the duration of tasks to be completed
find the assignment of task that can complete all tasks in lowest time.
"""


def taskAssignment(k, tasks):
    # create a dict to store task indices first
    taskIndices = {}
    for i, task in enumerate(tasks):
        if task not in taskIndices:
            taskIndices[task] = [i]
        else:
            taskIndices[task].append(i)

    # create a copy of sorted tasks
    sortedTask = sorted(tasks)
    beginIdx = 0
    endIdx = len(tasks) - 1
    paired = []
    # repeat k times
    while beginIdx < endIdx and len(paired) <= k:
        # get index of smallest and
        smallestIdx = taskIndices[sortedTask[beginIdx]].pop()
        largestIdx = taskIndices[sortedTask[endIdx]].pop()
        # get smallest and largest to pair will minimize duration
        paired.append([smallestIdx, largestIdx])
        beginIdx += 1
        endIdx -= 1

    return paired


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        k = 3
        tasks = [1, 3, 5, 3, 1, 4]
        expected = [[4, 2], [0, 5], [3, 1]]
        actual = taskAssignment(k, tasks)
        self.assertEqual(actual, expected)
