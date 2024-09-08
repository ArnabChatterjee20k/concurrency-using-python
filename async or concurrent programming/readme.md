https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task

Async or concurrent programming is basically doing cpu bound tasks while waiting for IO bound operations


1. Event Loop: The central execution device provided by asyncio. It manages and distributes the execution of different tasks. It's responsible for handling events and scheduling asynchronous routines.

2. Coroutines: Asynchronous functions declared with async def. These functions can be paused and resumed at await points, allowing I/O operations to run in the background.

3. Futures: Objects that represent the result of work that has not yet been completed. They are returned from tasks scheduled by the event loop.

4. Tasks: Scheduled coroutines that are wrapped into a Future object by the event loop, allowing their execution.

### How async await helps server?
First of allow await does not make an async function to be synchronous.
The await expression never blocks the main thread and only defers execution of code that actually depends on the result, i.e. anything after the await expression.

Ex - If a server is async and in a route handler a db call is awaited. And clients are making the request. It will not get blocked for both clients. They will run concurrently.
As a result the clients will be handled without blocking the thread.

An async server remains asynchronous even when using await for function calls because of how asynchronous programming and event loops work. The key point is that await doesn't block the entire server or event loop. Instead, it pauses only the current task until the awaited operation completes, allowing other tasks to run during that time.

endpoint function - async give_data()
so client A and B makes request
Two functions get registered in the event loop


Here’s a breakdown of how it works:

1. Event Loop:
The event loop continuously cycles through the tasks in the server. When you await an async operation (such as a network request or file read), the server doesn't freeze or wait for the operation to finish. Instead, the event loop moves on to the next task while the awaited task is being processed in the background (e.g., I/O or network operations).

2. Task Switching:
When an async function encounters an await, it effectively tells the event loop, "I'm waiting on this task, feel free to handle other tasks." Once the awaited operation completes (like the response from a network request), the event loop revisits the original task to resume it.

3. Concurrency without Blocking:
Other requests or tasks can continue to be processed because the await only pauses the specific task it's called within, not the entire server. Therefore, the server can handle many requests concurrently without being blocked by one long-running operation.

4. Threading vs. Async:
In traditional synchronous servers, blocking I/O would stop the thread, preventing it from handling other requests. In contrast, asynchronous servers use the event loop and await to keep the server responsive even when awaiting results from non-blocking I/O operations.