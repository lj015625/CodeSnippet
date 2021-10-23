
class Solution(object):

    def searchSuggestions(self, repository, customerQuery):

        searchStrings = []
        if (len(customerQuery) > 1):
            # start with two char string
            for i in range(2, len(customerQuery)+1):
                searchStrings.append(customerQuery[:i].lower())
        else:
            return []
        #print('debug: ', searchStrings)

        returnString = []
        for index, search in enumerate(searchStrings):
            # Could use Word2Vec or other similar distance method to find similar words.
            if index == 0:
                filteredRepository = [word.lower() for word in repository if word.lower().startswith(search)]
                filteredRepository.sort()
            # only need to search through the filtered repository because it is already searched
            else:
                filteredRepository = [word.lower() for word in filteredRepository if word.lower().startswith(search)]
            # saved the top 3 item
            returnString.append(filteredRepository[:3])
        return returnString




repository = ["Bags","baggage","banner","box","cloths"]
customerQuery = "bags"

solution = Solution()
result = solution.searchSuggestions(repository, customerQuery)
print(result)
