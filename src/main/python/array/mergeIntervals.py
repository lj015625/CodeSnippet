class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        flat_list = [item for sublist in intervals for item in sublist]
        intervals.sort()
        new_list = []
        n = len(intervals)
        for i, sublist in enumerate(intervals):
            c_beg = sublist[0]
            c_end = sublist[1]
            # skip the first item in the loop
            if i > 0:
                # merge two list together
                chg = False
                if c_beg <= p_end:
                    c_beg = p_beg
                    chg = True
                if c_end <= p_end:
                    c_end = p_end
                    chg = True
                # stick with the same list
                if not chg:
                    new_list.append([p_beg, p_end])
            # add the last
            if i == n-1:
                new_list.append([c_beg, c_end])
            else:
                p_beg = c_beg
                p_end = c_end

        return new_list

    def merge2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        flat_list = [item for sublist in intervals for item in sublist]
        intervals.sort()
        new_list = []
        n = len(intervals)
        for i, sublist in enumerate(intervals):
            c_beg = sublist[0]
            c_end = sublist[1]
            # skip the first item in the loop
            if i > 0:
                # merge two list together
                if c_beg <= p_end or c_end <= p_end:
                    c_beg = min(p_beg, c_beg)
                    c_end = max(p_end, c_end)
                # stick with the same list
                else:
                    new_list.append([p_beg, p_end])
            # add the
            if i == n-1:
                new_list.append([c_beg, c_end])
            else:
                p_beg = c_beg
                p_end = c_end

        return new_list

solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# intervals = [[1,4],[2,3]]
# Output: [[1,4]]
print(solution.merge2(intervals))