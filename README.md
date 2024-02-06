# Task Scheduling Simulator

This Python project simulates task scheduling on a multi-core system using different scheduling algorithms. The project includes implementations for First-Come-First-Serve (FCFS), Shortest Job First (SJF), Round Robin (RR), and Highest Response Ratio Next (HRRN) scheduling algorithms.

## Files and Descriptions

### fcfs.py

This file contains the implementation of the First-Come-First-Serve (FCFS) scheduling algorithm. Tasks are processed in the order they arrive, without prioritization.

- `Task class:` Represents a CPU task with attributes such as name, type, duration, state, and remaining time.
- `get_resources and get_priority functions:` Define the resource allocation strategy.
- `update_queue function:` Manages the transition of tasks between the ready and waiting states.
- **`process_t function:`** Models the behavior of each CPU core. It selects the next task from the ready queue and executes it until completion.
- **`print_t function:`** Prints the status of CPU cores at each time step.

### sjf.py

This file contains the implementation of the Shortest Job First (SJF) scheduling algorithm. Tasks with the shortest remaining execution time are prioritized.

- **`Task class:`** Remains the same as in FCFS.
- **`update_queue function:`** Modified to prioritize tasks based on their remaining time.
- **`process_t function:`** Modified to implement SJF algorithm. It now selects the task with the shortest remaining time.
- **`print_t function:`** Prints the status of CPU cores at each time step.

### rr.py

This file contains the implementation of the Round Robin (RR) scheduling algorithm. Each core processes tasks in a cyclic order, allowing fair sharing of CPU time.

- **`Task class:`** Remains the same as in FCFS.
- **`update_queue function:`** Similar to FCFS.
- **`process_t function:`** Modified to implement round-robin task allocation. Each core executes tasks in a cyclic order with a fixed time slice.
- **`print_t function:`** Prints the status of CPU cores at each time step.

### hrrn.py

This file contains the implementation of the Highest Response Ratio Next (HRRN) scheduling algorithm. Tasks with the highest response ratio (waiting time + execution time / execution time) are prioritized.

- **`Task class:`** Remains the same as in FCFS.
- **`update_queue function:`** Modified to prioritize tasks based on their response ratio.
- **`process_t function:`** Modified to consider the highest response ratio when selecting tasks. It now calculates the response ratio for each task and prioritizes tasks with the highest ratio.
- **`print_t function:`** Prints the status of CPU cores at each time step.

## Running the Simulation

1. Execute the script for the desired scheduling algorithm.
2. Input the available resources and task details as prompted.
3. Note: The simulation assumes four processes/cores in the system.
4. Observe the simulation output, showing the status of each core at each time step.

## Synchronization Mechanisms

- `The mutex (Mutex Lock)` ensures thread safety when accessing shared resources and updating task queues.
- `The endEvent (Event)` signals the end of a processing unit, allowing threads to proceed.
- `The printEvent (Event)` signals when it's time to print the status of cores.
