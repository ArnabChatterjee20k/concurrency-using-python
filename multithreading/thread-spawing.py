import time , threading
start = time.perf_counter()

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    print("done sleeping")

threads = []
for _ in range(100):
    thread = threading.Thread(target=do_something)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

finish = time.perf_counter()
print("finished in ",round(finish-start), " seconds")