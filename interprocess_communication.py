import multiprocessing

def is_even(numbers,q):

    for n in numbers:
        if n%2==0:
            q.put(n)

def print_numbers(q):
    while not q.empty():
        