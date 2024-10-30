# This script demonstrates asynchronous function execution in Python.
# The goal is to run 10 asynchronous tasks concurrently, where each task
# has a random sleep time between 0.5 and 3 seconds. Each task is assigned
# a unique number (from 1 to 10) and, after completion, it displays which
# task finished and how long it took. Finally, the program summarizes the
# results by showing the completion time of each task.

import asyncio
import random

# Asynchronous function that performs a task with a random sleep time
async def task(number):
    sleep_time = random.uniform(0.5, 3.0)  # Random sleep time between 0.5 and 3 seconds
    await asyncio.sleep(sleep_time)
    print(f"Task {number} completed after {sleep_time:.2f} seconds")
    return number, sleep_time

# Main function that runs 10 asynchronous tasks concurrently
async def main():
    # Create a list of tasks with unique numbers from 1 to 10
    tasks = [task(i) for i in range(1, 11)]
    
    # Run all tasks concurrently and wait for their completion
    results = await asyncio.gather(*tasks)
    
    # Display summary of results
    print("\nSummary of results:")
    for number, sleep_time in results:
        print(f"Task {number} completed after {sleep_time:.2f} seconds")

# Run the main function
asyncio.run(main())