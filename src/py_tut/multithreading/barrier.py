from threading import Barrier, Thread

my_barrier = Barrier(3)


class MyThread(Thread):
    def __init__(self, thread_ID):
        Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        print(str(self.thread_ID) + "\n")
        my_barrier.wait()


thread1 = MyThread(100)
thread2 = MyThread(101)

thread1.start()
thread2.start()
my_barrier.wait()


print("exiting")
