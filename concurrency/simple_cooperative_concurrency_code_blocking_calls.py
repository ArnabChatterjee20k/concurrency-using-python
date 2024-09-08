import queue
import time

def blocking_call():
    time.sleep(1000)

def async_task(name,q:queue.Queue):
    if q.empty():
        print(f"Task {name} nothing to do")
        return
    while not q.empty():
        count = q.get()
        total = 0
        print(f"Task {name} running")
        blocking_call()
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")

def main():
    work_queue = queue.Queue()
    for work in [10,12,5,4]:
        work_queue.put(work)

    # defined the generator function
    tasks = [async_task("One", work_queue), async_task("Two", work_queue)]
    done = False
    while not done:
        for task in tasks:
            try:
                # consuming the generators
                next(task)
            except StopIteration:
                tasks.remove(task)
            if len(tasks) == 0:
                done = True


main()
