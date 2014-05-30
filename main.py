class HashedDataRow(object):
    
    _data = []
    _cached_filters = {}
                
    @property
    def data(self): return self._data
   
    @data.setter        
    def data(self, data):
        if data is not None:
            self._data = data    
        else:                    
            self._data = []    
   
    def __init__(self, data = None): 
        self.data = data
   
    def filter(self, f, result = []):
        if f in self._cached_filters: 
          result += self._cached_filters[f]
        else:
          temp = [e for e in self._data if f(e)]
          result += temp
          self._cached_filters[f] = temp
        return result

if __name__ == "__main__":
    h = HashedDataRow(data=[1, 2, 3, 4, 5])
    
    greater_than_three = h.filter(lambda x: x > 3) # [4, 5]
    print(greater_than_three)
    
    lower_than_four = h.filter(lambda x: x < 4) # [1, 2, 3]
    print(lower_than_four)
