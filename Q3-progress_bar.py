import time
import random

class ProgressTask:
    def __init__(self, steps=100):
        self.current = 0
        self.total = steps
        self.start = time.time()
    def percent(self):
        return self.current / self.total
    def complete(self, n=1):
        self.current += n
    def time_spent(self):
        return time.time() - self.start
    def time_remaining(self):
        time_r = self.time_spent()*(1.0/self.percent()-1.0)
        return time_r  # this is accurate!

fake_task = ProgressTask(10)
print("Begin!")
for i in range(fake_task.total):
    # delay for anywhere between 1..3 seconds:
    time.sleep(random.uniform(1,3))
    # update the task with one bit done!
    fake_task.complete()
    print("{:.1f}% complete; {:.1f} seconds spent... {:.1f}s remaining.".format(
        fake_task.percent() * 100.0, 
        fake_task.time_spent(), 
        fake_task.time_remaining()))
