class FourCal:
    def setData(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def sum(self):
        return self.v1 + self.v2
    def minus(self):
        return self.v1 - self.v2
    def mul(self):
        return self.v1 * self.v2
    def div(self):
        return self.v1 / self.v2

class MoreFourCal(FourCal):   #상속
    def pow(self):
        return self.v1 ** self.v2

class SafeFourCal(FourCal):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def div(self):
        if self.v2 == 0:
            return 0
        else:
            return self.v1 / self.v2

if __name__ == "__main__":
    c1 = FourCal()
    c1.setData(6,3)
    print("c1 class c1.sum(): %d" %c1.sum())

    c2 = MoreFourCal()
    c2.setData(8,2)
    print("c2 class c2.mul(): %d" %c2.mul())

    c3 = SafeFourCal(5,0)
    print("c3 class c3.div(): %d" %c3.div())
