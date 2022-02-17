import pytest

MAP = 0
FILTER = 1

class Datasource:

    name ="data source"

    def __init__(self, arr, functions=[]):
        self.arr = arr
        self.functions = functions

    def map(self, func):
        funcs = self.functions[::]
        funcs.append((func, MAP))
        return Datasource(self.arr, funcs)

    def filter(self, func):
        funcs = self.functions[::]
        funcs.append((func, FILTER))
        return Datasource(self.arr, funcs)

    def collect(self):
        # collect will return a copy of self.arr
        items = self.arr
        for func, fun_type in self.functions:
            c = []
            # chain on each items
            for i in items:
                # MAP apply functions to all items
                if fun_type == MAP:
                    num = func(i)
                    c.append(num)
                # FILTER
                elif fun_type == FILTER:
                    # filter item by the filter function if it is true then add original item
                    if func(i):
                        c.append(i)
            items = c
        return items


class TestDatasource(object):

    def test_collect_with_chained_maps_and_filters(self):
        d = Datasource([1,2,3]) \
            .map(lambda x: x*2) \
            .filter(lambda x: x == 4) \
            .map(lambda x: x*3)

        assert d.collect() == [12]


    def test_collect_with_a_single_map(self):
        d = Datasource([1,2,3]).map(lambda x: x*2)

        assert d.collect() == [2,4,6]

    def test_collect_with_two_maps(self):
        initial = Datasource([1,2,3])

        first = initial.map(lambda x: x*2)

        second = first.map(lambda x: x*3)

        assert initial.collect() == [1,2,3]
        assert first.collect() == [2,4,6]
        assert second.collect() == [6,12,18]

pytest.main()
