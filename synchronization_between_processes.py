import time
import multiprocessing

def deposit_without_mp(balance,amount):
    for i in range(100):
        time.sleep(0.01)
        balance+=amount
    return balance

def withdraw_without_mp(balance,amount):
    for i in range(100):
        time.sleep(0.01)
        balance-=amount
    return balance

balance=600

def deposit_without_lock(balance,amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value+=amount
    return balance

def withdraw_without_lock(balance,amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value-=amount
    return balance
def deposit_with_lock(balance,amount,lock):
    for i in range(100):
        time.sleep(0.01)

        lock.acquire()
        balance.value+=amount
        lock.release()
    #return balance

def withdraw_with_lock(balance,amount,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value-=amount
        lock.release()
    #return balance
balance=multiprocessing.Value('i',600)
lock=multiprocessing.Lock()
if __name__ == '__main__':
    #balance=deposit_without_mp(balance,5)

    d=multiprocessing.Process(target=deposit_with_lock,args=(balance,5,lock))
    w=multiprocessing.Process(target=withdraw_with_lock,args=(balance,5,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print('Final balance: ',balance.value)
