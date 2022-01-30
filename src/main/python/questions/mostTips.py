"""Given two nonempty lists of user_ids and tips, write a function most_tips to find the user that tipped the most.
"""
import collections

def most_tips(user_ids, tips):
    userTips = collections.Counter()
    for id, tip in zip(user_ids, tips):
        if userTips[id]:
            userTips[id] += tip
        else:
            userTips[id] = tip
    return userTips.most_common()[0][0]

user_ids = [103, 105, 105, 107, 106, 103, 102, 108, 107, 103, 102]
tips = [2, 5, 1, 0, 2, 1, 1, 0, 0, 2, 2]

print(most_tips(user_ids, tips))
