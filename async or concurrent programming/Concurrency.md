Concurrency:
Concurrency refers to the ability to run multiple tasks seemingly at the same time by switching between them. In Python, concurrency is often achieved using asynchronous programming (asyncio) or by using threads or processes to parallelize blocking operations.
asyncio.run_in_executor allows you to run blocking tasks concurrently with other tasks by delegating them to threads (or processes).
Threads vs. Processes:
Thread-based concurrency: By default, asyncio.run_in_executor(None, ...) uses a thread pool (via Python's ThreadPoolExecutor). This means each blocking task runs in a separate thread within the same process.
Process-based concurrency: You can also use a process pool (via ProcessPoolExecutor) if you want to use separate processes instead of threads, which is useful for CPU-bound tasks because of Python's Global Interpreter Lock (GIL).