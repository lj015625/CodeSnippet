# There are two lists of dictionaries representing friendship beginnings and endings: friends_added and
# friends_removed. Each dictionary contains the user_ids and created_at time of the friendship beginning /ending.
#
# Write a function friendship_timeline to generate an output that lists the pairs of friends with their corresponding
# timestamps of the friendship beginning and then the timestamp of the friendship ending.

def friendship_timeline(friends_added, friends_removed):
    friendships = []
    for removed in friends_removed:
        for added in friends_added:
            removed_user_ids = sorted(removed['user_ids'])
            added_user_ids = sorted(added['user_ids'])
            if removed_user_ids == added_user_ids:
                friends_added.remove(added)
                friendships.append({
                    'user_ids': removed_user_ids,
                    'start_date': added['created_at'],
                    'end_date': removed['created_at']
                })
                break
    return sorted(friendships, key=lambda x: x['user_ids'])




import unittest


class TestProgram(unittest.TestCase):

    def test_case_2(self):
        friends_added = [
            {'user_ids': [1, 2], 'created_at': '2020-01-01'},
            {'user_ids': [3, 2], 'created_at': '2020-01-02'},
            {'user_ids': [2, 1], 'created_at': '2020-02-02'},
            {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

        friends_removed = [
            {'user_ids': [2, 1], 'created_at': '2020-01-03'},
            {'user_ids': [2, 3], 'created_at': '2020-01-05'},
            {'user_ids': [1, 2], 'created_at': '2020-02-05'}]
        expected  = [{
            'user_ids': [1, 2],
            'start_date': '2020-01-01',
            'end_date': '2020-01-03'
            },
            {
                'user_ids': [1, 2],
                'start_date': '2020-02-02',
                'end_date': '2020-02-05'
            },
            {
                'user_ids': [2, 3],
                'start_date': '2020-01-02',
                'end_date': '2020-01-05'
            },
        ]
        actual = friendship_timeline(friends_added, friends_removed)
        self.assertEqual(expected, actual)

