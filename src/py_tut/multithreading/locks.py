# what are r-locks?

# this is not a very good example - should revise this

import threading
import random
import time


class SafeCounter(object):
    def __init__(self):
        self.lock = threading.Lock()  # create a lock object. Initial state is unlocked
        self.count_value = 0

    def coutner_increase(self):
        try:
            # acquire lock
            self.lock.acquire()

            # ran_sec = random.random()
            # time.sleep(ran_sec)

            # increment counter
            self.count_value += 1
            print(f'counter value is {self.count_value}')
        finally:
            # release the lock
            self.lock.release()
            pass


def session_thread(counter_object: SafeCounter):
    # increase the count after random duration
    # for _ in range(THREAD_COUNT):
    ran_sec = random.random()
    time.sleep(ran_sec)
    counter_object.coutner_increase()


THREAD_COUNT = 200
thread_list = []
my_counter = SafeCounter()

for _ in range(THREAD_COUNT):
    ThreadInstance = threading.Thread(
        target=session_thread, args=(my_counter,))
    thread_list.append(ThreadInstance)
    ThreadInstance.start()

for tr in thread_list:
    tr.join()
# my_thread = threading.Thread(target=session_thread, args=(my_counter,))
# my_thread.start()
# my_thread.join()
print(my_counter.count_value)
