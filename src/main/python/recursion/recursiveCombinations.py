"""You have store credit of N dollars. However, you don’t want to walk a long distance with heavy books,
but you want to spend all of your store credit.

Let’s say we have a list of books in the format of tuples
where the first value is the price and the second value is the weight of the book -> (price,weight).

Write a function optimal_books to retrieve the combination allows you to spend all of your store credit
while getting at least two books at the lowest weight.

Note: you should spend all your credit and getting at least 2 books,
If no such condition satisfied just return empty list."""

def book_combinations(book_list, N):
    result_list = []
    min_weight = sum([book[0] for book in book_list])

    def recursive_traverse(index, remaining_credit, total_weight, choosen_books):
        nonlocal result_list, min_weight
        # Found the final results
        if remaining_credit == 0 and len(choosen_books) > 1 and total_weight < min_weight:
            result_list = choosen_books
            min_weight = total_weight
        # incorrect result
        if index >= len(book_list) or remaining_credit < 0 or total_weight > min_weight:
            return

        # current book
        recursive_traverse(index+1, remaining_credit,
                           total_weight, choosen_books)

        # continuous search for next book
        # add new book_list[index]
        recursive_traverse(index+1, remaining_credit - book_list[index][0],
                           total_weight + book_list[index][1], choosen_books+[book_list[index]])

    # call inner function first time
    recursive_traverse(0, N, 0, [])
    return result_list


N = 18
books = [(17,8), (9,4), (18,5), (11,9), (1,2), (13,7), (7,5), (3,6), (10,8)]
print(book_combinations(books, N))
