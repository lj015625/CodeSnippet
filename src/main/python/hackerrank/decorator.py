
def person_lister(func):
    """sort persons by age"""
    def inner(persons):
        # for ps in sorted(persons, key=lambda x: int(x[2])):
        #     yield f(ps)
        return map(func, sorted(persons, key=lambda x: x[2]))
    return inner

@person_lister
def name_format(persons):
    return ("Mr. " if persons[3] == "M" else "Ms. ") + persons[0] + " " + persons[1]

if __name__ == '__main__':

    persons = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
    print(*name_format(persons), sep='\n')



def wrapper(sortFunc):
    """format phone number to add +91"""
    def fun(l):
        # from right to left las 5 digits, last 5 to last 10 digits, then add +91 to the left
        for c in l:
            sortFunc(["+91 "+c[-10:-5]+" "+c[-5:]])
        return l

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = ['07895462130',
         '919875641230',
         '9195969878']
    sort_phone(l)