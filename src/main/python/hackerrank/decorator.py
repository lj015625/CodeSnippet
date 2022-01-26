
def person_lister(f):
    """sort persons by age"""
    def inner(persons):
        # return map(f, sorted(people, key=lambda x: x[2]))
        for ps in sorted(persons, key=lambda x: int(x[2])):
            yield f(ps)

    return inner

@person_lister
def name_format(persons):
    return ("Mr. " if persons[3] == "M" else "Ms. ") + persons[0] + " " + persons[1]

if __name__ == '__main__':

    persons = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
    print(*name_format(persons), sep='\n')