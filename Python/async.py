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

# Asynchronous function that simulates downloading a file
async def download_file(file_name):
    print(f"Start downloading {file_name}...")
    await asyncio.sleep(random.randint(1, 3))  # Simulates download time (1-3 seconds)
    print(f"Finished downloading {file_name}!")

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

    print("\n\nSecond example:")
    # Second example 
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = [download_file(file) for file in files]  # Create a list of tasks
    await asyncio.gather(*tasks)  # Execute all tasks concurrently

# Run the main function
asyncio.run(main())