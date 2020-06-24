class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        difference=[]
        for m in range(0,len(a)+1):
            for n in range(m+1,len(a)):
                difference.append(abs(a[m]-a[n]))
        self.difference=difference
        self.maximumDifference=max(self.difference)

    # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)