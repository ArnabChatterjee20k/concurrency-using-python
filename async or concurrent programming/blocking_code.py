import asyncio
import time

# A blocking function (e.g., a CPU-bound task)
def blocking_task():
    time.sleep(5)  # This is a blocking call
    return "Blocking task done!"

# An async function that calls a blocking function
async def async_func():
    print("Starting blocking task")
    # Using run_in_executor to run the blocking task
    result = await asyncio.get_event_loop().run_in_executor(None, blocking_task)
    print(result)

# Running the async function
asyncio.run(async_func())