class Calc:
    def __init__(self, a, b):
        self.num1 = int(a)
        self.num2 = int(b)
    
    def sum(self):
        res = self.num1 + self.num2
        return res
    
    def min(self):
        res = self.num1 - self.num2
        return res


def sum(a,b):
    res = Calc(a, b)
    return res.sum()

def min(a, b):
    res = Calc(a, b)
    return res.min()


a = 2
b = 3

print(sum(a, b))
print(min(a, b))

