what is the effect in python if we run a non async support function inside the async with await?

> solution - run in executor

In Python's asyncio, if you run a non-async (blocking) function inside an async function using await, you will encounter a problem because await is meant to pause execution until the awaited operation (typically an awaitable like an async function or a coroutine) is complete. If you attempt to await a non-async/blocking function, it won't work directly and will likely raise an error.

Here are the potential effects of running a blocking function inside an async function:

1. Blocking the Event Loop
If the non-async function is blocking (e.g., a CPU-bound operation or I/O operation), it will block the entire event loop. This means no other asynchronous tasks can run while the blocking operation is being processed, which defeats the purpose of using asyncio. The event loop will not switch to other tasks until the blocking function completes.

2. Error: Trying to await a Non-Async Function
If you attempt to use await on a function that is not awaitable (i.e., a regular function), you will get an error like this:
```
TypeError: object int can't be used in 'await' expression
```

### Solution: Using run_in_executor
To avoid blocking the event loop with a blocking function, you can use asyncio's run_in_executor to run the blocking code in a separate thread or process, without blocking the event loop.

run_in_executor(None, blocking_task, ...): Offloads each blocking task into a separate thread. The first argument None specifies using the default thread pool executor. You can pass arguments to the blocking_task function after it.