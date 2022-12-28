class Grange:
    counter = 1
    
    def __init__(self, b0, q, bn):
        seq = []
        self.string = f"grange({b0}, {q}, {bn})"
        self.q = q
        elem = b0
        while elem < bn:
            seq.append(elem)
            elem *= q
        try:
            self.seq = seq
        except:
            pass

    def __iter__(self):
        return self.seq.__iter__()

    def __len__(self):
        return len(self.seq)


    def __getitem__(self, key):
        if isinstance(key, slice):
            if not key.step:
                return Grange(key.start, self.q , key.stop)
            return Grange(key.start, self.q ** key.step , key.stop)
        if key >= len(self):
            e = self.seq[-self.counter]
            for i in range(len(self), key + self.counter):
                e *= self.q
            return e
        return self.seq[key]

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string

import sys
try:
    exec(sys.stdin.read())
except:
    pass