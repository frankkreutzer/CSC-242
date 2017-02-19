class Mapping(dict):
    def __init__(self, mapping = {}):
        for key in mapping:
            self[key] = mapping[key]

    def __repr__(self):
        return "Mapping({})".format( dict.__repr__(self) )

    def __setitem__(self, key, value):
        for item in (key, value):
            if item in self:
                self.pop(item)
                   
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def pop(self, key):
        if key in self:
            dict.pop(self, self[key])
            if key in self:
                dict.pop(self, key)








if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab4TEST.py' ))
