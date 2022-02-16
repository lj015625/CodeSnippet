def tournamentWinner(competitions, results):
    teamScores = {}
    maxScore = 0
    highestScoreTeam = None
    for c, r in zip(competitions, results):
        winner = c[1] if r == 0 else c[0]
        teamScores[winner] = teamScores.get(winner, 0) + 3
        if teamScores[winner] > maxScore:
            maxScore = teamScores[winner]
            highestScoreTeam = winner

    return highestScoreTeam


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)
