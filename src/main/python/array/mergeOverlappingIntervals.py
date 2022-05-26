""" Given a non-empty arbitrary array of two integer, merge overlapping intervals,
and return new intervals in no particular order. """


def mergeOverlappingIntervals(intervals):
    # sort by first element of the array
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    prev_beg = sorted_intervals[0][0]
    prev_end = sorted_intervals[0][1]

    merged_intervals = []
    for interval in sorted_intervals[1:]:
        beg = interval[0]
        end = interval[1]
        # there is intersection
        if beg <= prev_end:
            prev_end = max(prev_end, end)
        # no intersection
        else:
            merged_intervals.append([prev_beg, prev_end])
            prev_beg, prev_end = beg, end
    # add the last pair
    merged_intervals.append([prev_beg, prev_end])
    return merged_intervals


import unittest


class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    #     expected = [[1, 2], [3, 8], [9, 10]]
    #     actual = mergeOverlappingIntervals(intervals)
    #     self.assertEqual(expected, actual)

    def test_case_2(self):
        intervals = [[1, 22], [-20, 30]]
        expected = [[-20, 30]]
        actual = mergeOverlappingIntervals(intervals)
        self.assertEqual(expected, actual)
