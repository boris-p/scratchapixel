# A thread is a set of instructions that forms a control flow within the same program/process
# the time duration in which instructions of a thread are inside the cpu and are executing are called a time slice

# there are two ways to construct multithreaded programs in python
# 1. passing a callable object
# 2. overridign the run method

from threading import Thread
import time


# 1 callable object

print("1 callable object")


def producePrimeNumbers(num):
    print(f'num is {num}')
    print("prime number thread started")
    print(2)
    for PrimeNumberCandidate in range(2, 20):
        time.sleep(0.1)
        IsPrime = False
        for divisor in range(2, PrimeNumberCandidate):
            # Skip the Composite Number
            if PrimeNumberCandidate % divisor == 0:
                IsPrime = False
                break
            else:
                # Mark the Prime Number
                IsPrime = True
        # Print the Prime Number
        if IsPrime == True:
            print(PrimeNumberCandidate)
    print("Prime number thread exiting")


primeNumberThread = Thread(target=producePrimeNumbers, args=(3,))
primeNumberThread2 = Thread(target=producePrimeNumbers, args=(3,))

print("main thread started")
primeNumberThread.start()
primeNumberThread2.start()

# Let the Main thread wait for the prime thread to complete
primeNumberThread.join()
primeNumberThread2.join()
print("main thread resumed")
print("main thread exiting")


# 2 override run

print("override run")


class FibonaccyThread(Thread):
    def __init(self):
        Thread.__init__(self)

    # override run
    def run(self):
        print("fibonacci thread started")
        firstTerm = 0
        secondTerm = 1
        nextTerm = 0

        for i in range(20):
            if (i <= 1):
                nextTerm = i
            else:
                nextTerm = firstTerm + secondTerm
                firstTerm = secondTerm
                secondTerm = nextTerm

            print(nextTerm)

        print("fibonacci thread ended")


print("main thread started")
fibThread = FibonaccyThread()
fibThread.start()
fibThread.join()
print("main thread resumed")
print("main thread ending")
