# CPU Scheduling Algorithms Simulation

This project simulates three different CPU scheduling algorithms: First Come First Serve (FCFS), Shortest Job First (SJF), and Round Robin (RR). It uses multithreading to model the behavior of multiple CPU cores.

## Code Explanation

### `fcfs.py`

This script simulates the First Come First Serve (FCFS) CPU scheduling algorithm. FCFS is a simple scheduling algorithm that executes tasks in the order they arrive.

- The `Task` class represents a CPU task with attributes such as name, type, duration, state, and remaining time.
- The `get_resources` and `get_priority` functions define the resource allocation strategy.
- The `update_queue` function manages the transition of tasks between the ready and waiting states.
- The `process_t` function models the behavior of each CPU core. It selects the next task from the ready queue and executes it until completion.
- The `print_t` function prints the status of CPU cores at each time step.

### `sjf.py`

This script simulates the Shortest Job First (SJF) CPU scheduling algorithm. SJF selects the task with the shortest remaining time first.

- The `Task` class remains the same as in FCFS.
- The `update_queue` function is modified to prioritize tasks based on their remaining time.
- The `process_t` function remains similar to FCFS but now selects the task with the shortest remaining time.

### `rr.py`

This script simulates the Round Robin (RR) CPU scheduling algorithm. RR is a preemptive algorithm that allocates a fixed time slice to each task in a cyclic manner.

- The `Task` class remains the same as in FCFS.
- The `update_queue` function is similar to FCFS.
- The `process_t` function is modified to implement round-robin task allocation. Each core executes tasks in a cyclic order with a fixed time slice.
- The `print_t` function prints the status of CPU cores at each time step.

## Authors

- [Your Name]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Replace `[Your Name]` with your actual name. This README file includes an explanation for each scheduling algorithm.
