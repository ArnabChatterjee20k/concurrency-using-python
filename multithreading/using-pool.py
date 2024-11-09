import concurrent.futures , time

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    return "done sleeping"


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something) for _ in range(10)]
    for future in concurrent.futures.as_completed(results):
        print(future.result())

