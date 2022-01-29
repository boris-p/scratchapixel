# a synchronization construct
# used to limit the access to the shared resources with limited capacity
# an example of a parking lot with a semaphore for syncing available resources

# semaphore can be released more times than its initial value
# a bounded semaphore cannot be raised above the starting value


import threading
import time


object_name = threading.Semaphore(3)

thread_list = []


def display(name):
    object_name.acquire()
    for _ in range(5):
        time.sleep(2)
        print(f'hello {name}')
        object_name.release()


for i in range(5):
    thread_list.append(threading.Thread(target=display, args=(f'Thread{i}',)))

for tr in thread_list:
    tr.start()

for tr in thread_list:
    tr.join()

print("exiting")
