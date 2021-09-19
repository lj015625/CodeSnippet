from collections import defaultdict, Counter, deque

class Solution(object):

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # create a alphabet map
        order_map = {c: index for index, c in enumerate(order)}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False

                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break
        return True

    def isAlienSorted2(self, words, order):

        order_map = {c: index for index, c in enumerate(order)}

        def checkOrder(firstword, secondword):
            for a, b in zip(firstword, secondword):
                if order_map[a] != order_map[b]:
                    return order_map[a] < order_map[b]
            return len(firstword) <= len(secondword)

        # if all items are true then return true
        return all(checkOrder(word1, word2) for word1, word2 in zip(words, words[1:]))

    def isAlienSorted3(self, words, order):
	    order_map = {c: index for index, c in enumerate(order)}
	    words = [[order_map[c] for c in word] for word in words]
	    return all(word1 <= word2 for word1, word2 in zip(words, words[1:]))


    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Step 0: create data structures + the in_degree of each unique letter to 0.

        # The functionality of both dictionaries and defualtdict are almost the same.
        # defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""


        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        # find a those node with 0 in-edge
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                # delete adj list node's in-edge after removing current node
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)

    def alienOrder2(self, words):

        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c: [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # Step 2: Depth-first search.
        seen = {}  # False = grey, True = black.
        output = []

        def visit(node):  # Return True if there are no cycles.
            if node in seen:
                return seen[node]  # If this node was grey (False), a cycle was detected.
            seen[node] = False  # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False  # Cycle was detected lower down.
            seen[node] = True  # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)


solution = Solution()
# print(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
#
# print(solution.isAlienSorted2(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
#
# print(solution.isAlienSorted3(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))


print(solution.alienOrder(["wrt","wrf","er","ett","rftt"]))
# print(solution.alienOrder2(["wrt","wrf","er","ett","rftt"]))