class Statistics:
    def __init__(self):
        self.min = None
        self.max = None
        self.list=[]
        self.total = 0.0
        self.n = 0
        self.var = 0
    def observe(self, x):
        if self.n > 1:
            delta = x - self.mean()
        self.list.append(x)
        self.list.sort()
        self.total += x
        self.n += 1
        self.min = self.list[0]
        self.max = self.list[len(self.list)-1]
        if self.n > 2:
            self.var = (delta*(x-self.mean()))   
    def mean(self):
        return self.total / self.n
    def variance(self):
        n=0
        mean = 0.0
        M2 = 0.0
        for x in self.list:
            n+=1
            delta = x - mean
            mean+= delta/n
            M2 += delta*(x-mean)
        if n<2:
            return (None)
        else:
            return M2 / (n - 1)
    def __str__(self):
        if self.n == 0:
            return '- no data -'
        return 'mean: {}, max: {}, min: {}, variance: {}'.format(self.mean(), self.max, self.min, self.variance())

stats = Statistics()
for x in [4,2,1,3]:
    stats.observe(x)
print(stats)
# Expected: mean: 2.5, max: 4, min: 1