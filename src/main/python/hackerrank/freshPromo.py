class Solution(object):


    def foo(codeList, shoppingCart):

        def sublist(lst1, lst2):
            # ls1 = [element for element in lst1 if element in lst2]
            # ls2 = [element for element in lst2 if element in lst1]
            # return ls1 == ls2
            indices = [i for i, x in enumerate(lst1) if x in lst2 or x == 'anything']
            print(indices, len(lst1)-1)
            for i, index in enumerate(indices):
                if i != index:
                    return False
            return True

        flag = True
        for i, codes in enumerate(codeList):
            flag &= sublist(codes, shoppingCart)
        return flag

codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]

result = Solution.foo(codeList, shoppingCart)
print(result)