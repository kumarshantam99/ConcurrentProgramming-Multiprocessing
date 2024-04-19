"""
import time
import multiprocessing
def square(numbers):

    time.sleep(1)
    for number in numbers:
        result=number*number
        print(f"Square of the number {number} is {result}")

def cube(numbers):

    time.sleep(1)
    for number in numbers:
        result=number*number*number
        print(f"Cube of the number {number} is {result}")


if __name__ == '__main__':
    num_list=[1,2,3,4]

    p1=multiprocessing.Process(target=square,args=(num_list,))
    p2=multiprocessing.Process(target=cube,args=(num_list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('\nCompleted')

Output:
Square of the number 1 is 1
Square of the number 2 is 4
Square of the number 3 is 9
Square of the number 4 is 16
Cube of the number 1 is 1
Cube of the number 2 is 8
Cube of the number 3 is 27
Cube of the number 4 is 64
"""

# In the above example if we pass a global variable list to store squared values inside square() and print it in main() we will not get any
# value printed out as global variable instantiated is limited to the scope of the process and is not updated globally.

import threading
import time
squares=[]

def square(numbers):

    time.sleep(1)
    global squares
    for number in numbers:
        result=number*number
        print(f"Square of the number {number} is {result}")
        squares.append(result)


if __name__ == '__main__':
    num_list=[1,2,3,4]
    p1=threading.Thread(target=square,args=(num_list,))
    p1.start()
    p1.join()
    print('\nResult: ',squares)

    print('\nCompleted')
