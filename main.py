class HashedDataRow(object):

    _data = []
    _cached_filters = {}

    @property
    def data(self): return self._data

    @data.setter
    def data(self, data):
        if data is not None:
            if data != self._data:
                self._cached_filters = {} #если поменяли data то и старые фильтры никуда не годятся
            self._data = data
        else:
            self._data = []

    def __init__(self, data = None):
        self.data = data

    def filter(self, f, result = []):       #Совсем не ожидал того, что result каким то образом сохраняется.
        if f in self._cached_filters:       #Должен же бы при каждом вызове функции обнуляться? Жажду объяснений ;D
          return result + self._cached_filters[f]
        else:
          temp = [e for e in self._data if f(e)]
          self._cached_filters[f] = temp
          return result + temp


if __name__ == "__main__":
    h = HashedDataRow(data=[1, 2, 3, 4, 5])

    greater_than_three = h.filter(lambda x: x > 3) # [4, 5]
    print(greater_than_three)

    lower_than_four = h.filter(lambda x: x < 4) # [1, 2, 3]
    print(lower_than_four)

    h.data = [1, 2, 2, 2, 1, 3, 4, 7, 8 ,9]         # MOAR TESTS!

    greater_than_three = h.filter(lambda x: x > 3) # [4, 7, 8, 9]
    print(greater_than_three)

    lower_than_four = h.filter(lambda x: x < 4) # [1, 2, 2, 2, 1, 3]
    print(lower_than_four)
