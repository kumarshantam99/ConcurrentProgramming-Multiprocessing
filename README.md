# Multi Processing in Python

Multiprocessing can make a program substantially more efficient by running multiple tasks in parallel instead of sequentially. A similar term is multithreading, but they are different.

A process is a program loaded into memory to run and does not share its memory with other processes. A thread is an execution unit within a process. Multiple threads run in a process and share the process’s memory space with each other.

Python’s Global Interpreter Lock (GIL) only allows one thread to be run at a time under the interpreter, which means you can’t enjoy the performance benefit of multithreading if the Python interpreter is required. This is what gives multiprocessing an upper hand over threading in Python. Multiple processes can be run in parallel because each process has its own interpreter that executes the instructions allocated to it. Also, the OS would see your program in multiple processes and schedule them separately, i.e., your program gets a larger share of computer resources in total. So, multiprocessing is faster when the program is CPU-bound. In cases where there is a lot of I/O in your program, threading may be more efficient because most of the time, your program is waiting for the I/O to complete. However, multiprocessing is generally more efficient because it runs concurrently.
