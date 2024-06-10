class Intersection:
    def __init__(self, t, o):
        self._t = t
        self._o = o

    @property
    def t(self):
        return self._t
    
    @property
    def object(self):
        return self._o
    
    @staticmethod
    def hit(xs):
        if len(xs) == 0:
            return None
        else:
            valid_hits = sorted((x for x in xs if x.t >= 0), key=lambda x: x.t)
            return valid_hits[0] if valid_hits else None