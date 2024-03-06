class course:
    def __init__(self,nameteacher,namre1,namre2):
        self.nameteacher=nameteacher
        self.namre1=namre1
        self.namre2=namre2
    def average(self):
        avg=(self.namre1+self.namre2)/2
        print(avg)
math=course("mr.jack",20,12)

science=course("ahmad",20,10)

math.average()

science.average()

print(math.nameteacher)
print(science.nameteacher)