# syscall -> fork
from multiprocessing import Process
import os

num_processes = os.cpu_count()
print("I am having", num_processes, "number of cores of CPU")

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

processes:list[Process] = []

# creating/forking child processes in all my cpus
# then waiting for all the child processes to complete by blocking the main process/program
for i in range(num_processes):
    p = Process(target=lambda: print(f"Fibonacci of {40+i} is {fib(40+i)}"), args=())
    processes.append(p)
    p.start()
    # p.join() # if called right after the start of the process in the loop it, 
            # the processes will spawn on separate cpus 
            # but they will not execute parallely
            # they will execute sequentially
            # as we are blocking the main program by join to continue the loop and create new process

# achieving true parallelism
for p in processes:    
    p.join() # waiting for the corresponding child process to complete before termination of the main program/process