"""
Given a distance array of distances between circular cities (miles to the next city), fuels at each cities,
the mpg of the car find the starting city index.
"""


# O(n^2) time O(1) space
def validStartingCity(distances, fuel, mpg):
    numOfCities = len(distances)
    # test each starting point
    for startCityIdx in range(numOfCities):
        canDriveMiles = 0
        for currentCityIdx in range(startCityIdx, startCityIdx + numOfCities):
            # if milesRemaining is no
            if canDriveMiles < 0:
                continue

            # prevent index over bound
            currentCityIdx = currentCityIdx % numOfCities
            fuelGained = fuel[currentCityIdx]
            distance = distances[currentCityIdx]
            canDriveMiles += fuelGained * mpg - distance

        if canDriveMiles == 0:
            return startCityIdx

    return -1


# O(n) time O(1) space
def validStartingCity2(distances, fuel, mpg):
    numOfCities = len(distances)
    remainingMiles = 0
    # start at first city with 0 miles
    lowestRemainingMiles = 0
    lowestRemainingMilesIdx = 0
    for currentCityIdx in range(1, numOfCities):
        # previous city fuel gained
        fuelGained = fuel[currentCityIdx - 1]
        # distance to current city
        distance = distances[currentCityIdx - 1]
        # remaining miles at current city
        remainingMiles += fuelGained * mpg - distance
        # keep track of lowest
        if remainingMiles < lowestRemainingMiles:
            lowestRemainingMiles = remainingMiles
            lowestRemainingMilesIdx = currentCityIdx

    return lowestRemainingMilesIdx


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity(distances, fuel, mpg)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        distances = [5, 25, 15, 10, 15]
        fuel = [1, 2, 1, 0, 3]
        mpg = 10
        expected = 4
        actual = validStartingCity2(distances, fuel, mpg)
        self.assertEqual(actual, expected)
