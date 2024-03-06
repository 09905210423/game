class course:
    def __init__(self,name,teacher,namre1,namre2):
        self.teacher=teacher
        self.namre1=namre1
        self.namre2=namre2
        self.name=name
    def average(self):
        avg=(self.namre1+self.namre2)/2
        print(avg)
math=course("mr.jack"12,12)

science=course(13,10)

math.average()

print(math.teacher)