
n = int(input("enter number: "))

for i in range(10):
    print(n*(i+1))

# 2
arr = list(map(int, input().split()))

for num in arr:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)


# oops 1
class StringClass:
    st = ""

    def __init__(self, st):
        self.st = st

    def printstring(self):
        print(self.st)

    def stringLength(self):
        return len(self.st)

    def stringToList(self, s):
        lst = [i for i in s]
        return lst


# s = StringClass("hello world")
# print(s.stringToList("anshuman"))


class PairsPossible(StringClass):
    pairs = []

    def storePairs(self):
        # for i in self.str:
        #     for j in self.str:
        #         self.pairs.append([i,j])
        self.pairs = [[i, j] for i in self.st for j in self.st]

    def printPairs(self):
        for i in self.pairs:
            print(f"({i[0]},{i[1]})", end=" ")


c = PairsPossible("abc")
c.storePairs()
c.printPairs()