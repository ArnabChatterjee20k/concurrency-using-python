import asyncio
import time

# A blocking function (e.g., a CPU-bound or I/O-bound task)
def blocking_task(task_id, duration):
    print(f"Task {task_id} started (will take {duration} seconds)...")
    time.sleep(duration)  # This simulates a blocking operation
    print(f"Task {task_id} completed.")
    return f"Task {task_id} result"

# An async function that runs multiple blocking tasks concurrently
async def run_multiple_blocking_tasks():
    loop = asyncio.get_event_loop()
    
    # List of blocking tasks with different durations
    blocking_tasks = [
        loop.run_in_executor(None, blocking_task, 1, 3),  # Task 1, runs for 3 seconds
        loop.run_in_executor(None, blocking_task, 2, 2),  # Task 2, runs for 2 seconds
        loop.run_in_executor(None, blocking_task, 3, 1),  # Task 3, runs for 1 second
    ]
    
    # Use asyncio.gather to run all blocking tasks concurrently
    results = await asyncio.gather(*blocking_tasks)
    
    print("All tasks completed.")
    print("Results:", results)

# Run the async function
asyncio.run(run_multiple_blocking_tasks())
