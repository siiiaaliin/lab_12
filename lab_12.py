#тут одразу знаходяться три задачі: 7.3.1, 7.3.2 та 7.3.3
from math import gcd

class RationalError(ZeroDivisionError):
    def __init__(self,message):
        super().__init__()
        self._message=message

    def __str__(self):
        return str(self._message)
    

class RationalValueError(ValueError):
    def __init__(self, message):
        super().__init__(message)
        self._message=message

    def __str__(self):
        return "RationalValueError: " + str(self._message)
    
class Rational:
    def __init__(self, n, d=None):
        if isinstance(n, str):
            if '/' in n:
                n, d=map(int, n.strip().split('/'))
            else:
                n=int(n)
                d=1
            self._set(n, d)
        elif isinstance(n, int) and isinstance(d, int):
            self._set(n, d)
        else:
            raise RationalValueError("Некоректні типи для стврення Rational")

    def _set(self, n, d):
        if d==0:
            raise RationalError("Знаменник дорівнює нулю")
        if n*d<0:
            sign=-1
        else:
            sign=1
        n, d=abs(n), abs(d)
        g=gcd(n, d)
        self.n=sign*(n//g)
        self.d=d//g

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __call__(self):
        return self.n/self.d
    
    def __getitem__(self, key):
        if key=="n":
            return self.n
        elif key=="d":
            return self.d
        else:
            raise KeyError

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise RationalValueError("Значення повинно бути цілим числом")
        if key=="n":
            self._set(value, self.d)
        elif key=="d":
            self._set(self.n, value)
        else:
            raise KeyError

    def __add__(self, other):
        if isinstance(other, int):
            other=Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError("Спроба додати нераціональне значення")
        n=self.n*other.d+other.n*self.d
        d=self.d*other.d
        return Rational(n, d)

    def __sub__(self, other):
        if isinstance(other, int):
            other=Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError("Спроба відняти нераціональне значення")
        n=self.n*other.d-other.n*self.d
        d=self.d*other.d
        return Rational(n, d)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError("Спроба помножити на нераціональне значення")
        n=self.n*other.n
        d=self.d*other.d
        return Rational(n, d)

    def __truediv__(self, other):
        if isinstance(other, int):
            other=Rational(other, 1)
        if not isinstance(other, Rational):
            raise RationalValueError("Спроба поділити на нераціональне значення")
        if other.n==0:
            raise RationalError("Ділення на нуль")
        n=self.n*other.d
        d=self.d*other.n
        return Rational(n, d)

def solution(line):
    parts=line.strip().split()
    if '/' in parts[0]:
        res=Rational(parts[0])
    else:
        res=Rational(int(parts[0]), 1)
    i=1
    while i<len(parts):
        sign=parts[i]
        num=parts[i+1]
        if '/' in num:
            num=Rational(num)
        else:
            num=Rational(int(num), 1)
        if sign=='+':
            res=res+num
        elif sign=='-':
            res=res-num
        elif sign=='*':
            res=res*num
        elif sign=='/':
            res=res/num
        else:
            raise ValueError
        i+=2

    return res


# with open("/Users/alinastratiichuk/Desktop/input01(1).txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     if line.strip():
#         print(f"{line.strip()} = {solution(line)}")



class RationalList:
    def __init__(self):
        self.data=[]

    def append(self, value):
        if isinstance(value, int):
            value=Rational(value, 1)
        elif isinstance(value, str):
            value=Rational(value)
        elif not isinstance(value, Rational):
            raise RationalValueError("Спроба додати до списку некоректне значення")
        self.data.append(value)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value=Rational(value, 1)
        elif isinstance(value, str):
            value=Rational(value)
        elif not isinstance(value, Rational):
            raise RationalValueError("Спроба додати до списку некоректне значення")
        self.data[index]=value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        result=RationalList()
        result.data=self.data.copy()
        if isinstance(other, RationalList):
            result.data+=other.data
        elif isinstance(other, (int, str, Rational)):
            result.append(other)
        else:
            raise RationalValueError("Спроба об'єднати список з некоректним значенням")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for el in other.data:
                self.append(el)
        elif isinstance(other, (int, str, Rational)):
            self.append(other)
        else:
            raise RationalValueError("Спроба додати до списку некоректне значення")
        return self

    def sum(self):
        total=Rational(0, 1)
        for el in self.data:
            total+=el
        return total
    
# with open("/Users/alinastratiichuk/Desktop/input03.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     if line.strip():
#         list=RationalList()
#         for num in line.strip().split():
#             list.append(num)
#         result=list.sum()
#         print(result)


# num=Rational(1, 0)
# print(num())

num=Rational(1, 2)
result=num+"xyz"   
print(result)

