import queue

def sync_task(name,q:queue.Queue):
    if q.empty():
        print(f"Task {name} nothing to do")
        return
    while not q.empty():
        count = q.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            print(f"Task {name} total: {total}")

def main():
    work_queue = queue.Queue()
    for work in [10,12,5,4]:
        work_queue.put(work)
    # synchronous tasks
    tasks = [(sync_task, "One", work_queue), (sync_task, "Two", work_queue)]
    for t,n,q in tasks:
        t(n,q)

main()
