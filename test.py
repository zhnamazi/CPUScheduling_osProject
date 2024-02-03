
from threading import Event
import threading


# event = Event()
# event.clear()
# are_wait = [[False], [False]]

# def thread_func(number, is_wait):
#     while True:
#         print(number)
#         is_wait[0] = True
#         event.wait()
#         event.clear()
#         is_wait[0] = False

# print("t = ", x)
# t1 = threading.Thread(target=thread_func, args=(1, are_wait[0]))
# t2 = threading.Thread(target=thread_func, args=(2, are_wait[1]))

# x = 0
# t1.start()
# t2.start()
# while x < 5:
#     event.set()
#     while are_wait[0] == [False] or are_wait[1] == [False]:
#         pass
#     print("t = ", x)
#     x += 1
    

# t1.join()
# t2.join()

import threading
import time

# Events for synchronization
start_event = threading.Event()
print_event = threading.Event()

# Shared variable to simulate work results
work_results = [0, 0, 0]


def worker_thread(id, start_event, print_event):
    while True:
        start_event.wait()  # Wait for the signal to start
        # Simulate some work
        work_results[id] += 1
        print(f"Worker {id} done.")
        # Signal that this thread's work is done (in a real scenario, you might need a more robust check here)
        if all(result > work_results[id] - 1 for result in work_results):
            print_event.set()  # Signal that work is done
        start_event.clear()  # Wait for the next cycle

def print_thread(start_event, print_event):
    x = 0
    while True:
        print_event.wait()  # Wait for the signal to print
        x +=1
        # Print results
        print(f"Results: {work_results}")
        print_event.clear()  # Reset for the next cycle
        if x < 5:
            start_event.set()  # Signal workers to start the next cycle

# Create and start the printing thread
printing = threading.Thread(target=print_thread, args=(start_event, print_event))
printing.start()

# Create and start worker threads
workers = [threading.Thread(target=worker_thread, args=(i, start_event, print_event)) for i in range(3)]
for worker in workers:
    worker.start()

# Start the first cycle
start_event.set()

# In a real program, you would have a condition to break out of this loop
for _ in range(10):  # Simulate 10 cycles
    time.sleep(1)  # Simulate time passing
