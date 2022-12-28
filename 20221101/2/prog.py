class Triangle:
    counter = 0
    
    def __init__(self, x, y, z):
        self.x = x # 1
        self.y = y # 2
        self.z = z # 3
        self.exist = False
        self.square = abs(self)
    
    def __abs__(self):
        t = abs(
            (self.y[self.counter] - self.x[self.counter]) * (self.z[1] - self.x[1]) -
            (self.z[self.counter] - self.x[self.counter]) * (self.y[1] - self.x[1])
        )
        self.exist = t != self.counter
        return 0.5 * t

    def __lt__(self, other):
        return self.square < other.square

    def __gt__(self, other):
        return self.square  > other.square

    def __contains__(self, other):
        if other.square == self.counter or other.square == self.counter and self.square == self.counter:
            return True
        if self.square >= other.square:
            x1, y1 = self.x
            x2, y2 = self.y
            x3, y3 = self.z
            
            tmp = []
            for x0, y0 in (other.x, other.y, other.z):
                t1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
                t2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
                t3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
                if (t1 > self.counter and t2 > self.counter and t3 > self.counter) or (t1 < self.counter and t2 < self.counter and t3 < self.counter):
                    tmp.append(True)
                else:
                    tmp.append(False)
            return all(tmp)
        return False
 
    def __and__(self, other):
        if not self.exist or not other.exist:
            return False

        x1, y1 = self.x
        x2, y2 = self.y
        x3, y3 = self.z

        tmp = []
        for x0, y0 in (other.x, other.y, other.z):
            t1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
            t2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
            t3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
            if (t1 >= 0 and t2 >= 0 and t3 >= 0) or (t1 <= 0 and t2 <= 0 and t3 <= 0):
                tmp.append(True)
            else:
                tmp.append(False)

        x1, y1 = other.x
        x2, y2 = other.y
        x3, y3 = other.z

        tmp1 = []
        for x0, y0 in (self.x, self.y, self.z):
            t1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
            t2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
            t3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
            if (t1 >= 0 and t2 >= 0 and t3 >= 0) or (t1 <= 0 and t2 <= 0 and t3 <= 0):
                tmp1.append(True)
            else:
                tmp1.append(False)

        return any(tmp) or any(tmp1)

    def __matmul__(self, dot):
        x1, y1 = self.x
        x2, y2 = self.y
        x3, y3 = self.z

        x0, y0 = dot

        v1 = - x1 + x0, - y1 + y0
        v2 = - x2 + x0, - y2 + y0
        v3 = - x3 + x0, - y3 + y0

        x1, y1 = x1 + 2 * v1[self.counter], y1 + 2 * v1[1]
        x2, y2 = x2 + 2 * v2[self.counter], y2 + 2 * v2[1]
        x3, y3 = x3 + 2 * v3[self.counter], y3 + 2 * v3[1]

        return Triangle(
            (x1, y1),
            (x2, y2),
            (x3, y3)
        )

    def __str__(self):
        return f'''
        Triangle:
            {self.x}
            {self.y}
            {self.z}
        '''

    def __repr__(self):
        return str(self)

    def __bool__(self):
        return self.exist

import sys
try:
    exec(sys.stdin.read())
except:
    pass